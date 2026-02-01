# core/orchestrator.py

import threading
import time
from typing import Dict, Any

from core.evolution_engine import EvolutionEngine
from core.scenario_runner import ScenarioRunner
from core.telemetry import Telemetry
from core.entity_engine import EntityEngine
from core.console import Console
from core.resource_nodes import ResourceNodes


class ArenaOrchestrator:
    def __init__(self, tick_rate: float = 0.1):
        """
        tick_rate: seconds between ticks (0.1 = 100ms)
        """
        self.tick_rate = tick_rate
        self._running = False
        self._thread = None

        # Shared arena state
        self._state_lock = threading.Lock()
        self._state: Dict[str, Any] = {
            "tick": 0,
            "timestamp": time.time(),
            "entities": [],
            "nodes": [],
            "events": [],
        }

        # Organs
        self.evolution = EvolutionEngine()
        self.scenarios = ScenarioRunner()
        self.telemetry = Telemetry()
        self.entities = EntityEngine()
        self.console = Console()
        self.nodes = ResourceNodes()

    # -------------------------
    # Lifecycle
    # -------------------------
    def start(self):
        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)

    # -------------------------
    # Main Loop
    # -------------------------
    def _loop(self):
        while self._running:
            self._tick()
            time.sleep(self.tick_rate)

    # -------------------------
    # Tick Logic
    # -------------------------
    def _tick(self):
        with self._state_lock:
            self._state["tick"] += 1
            self._state["timestamp"] = time.time()

            # Evolution engine (internal adaptation)
            self.evolution.evolve(self._state)

            # Scenario runner (missions, phases, triggers)
            self.scenarios.run(self._state)

            # Resource nodes (ecosystem)
            self.nodes.update(self._state)

            # Entity engine (agents move, sense, react)
            self.entities.update(self._state)

            # Team console (apply queued commands)
            self.console.flush(self._state)

            # Telemetry (broadcast live state)
            self.telemetry.broadcast(self._state)

    # -------------------------
    # Console API
    # -------------------------
    def submit_command(self, channel: str, command: Dict[str, Any]) -> None:
        self.console.enqueue(channel, command)

    # -------------------------
    # State Access
    # -------------------------
    def get_state(self) -> Dict[str, Any]:
        with self._state_lock:
            return dict(self._state)  # safe copy
