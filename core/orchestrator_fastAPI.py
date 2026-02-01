# core/orchestrator.py

import threading
import time
from typing import Dict, Any


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
            "events": [],
        }

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

            # Future hooks:
            # self._run_evolution()
            # self._run_scenarios()
            # self._update_entities()
            # self._emit_telemetry()

    # -------------------------
    # State Access
    # -------------------------
    def get_state(self) -> Dict[str, Any]:
        with self._state_lock:
            return dict(self._state)  # return a safe copy
