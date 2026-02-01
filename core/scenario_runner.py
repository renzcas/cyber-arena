# core/scenario_runner.py

import time
from typing import Dict, Any


class ScenarioRunner:
    """
    Drives missions, phases, triggers, and scripted Arena behavior.
    """

    def __init__(self):
        self.active_scenario = None
        self.phase = 0
        self.last_phase_change = time.time()

    def load_scenario(self, scenario: Dict[str, Any]) -> None:
        """
        Load a scenario definition.
        """
        self.active_scenario = scenario
        self.phase = 0
        self.last_phase_change = time.time()

    def run(self, state: Dict[str, Any]) -> None:
        """
        Execute scenario logic each tick.
        """
        if not self.active_scenario:
            return

        phases = self.active_scenario.get("phases", [])
        if not phases:
            return

        # Current phase definition
        current = phases[self.phase]

        # Execute phase action
        action = current.get("action")
        if callable(action):
            action(state)

        # Phase duration check
        duration = current.get("duration", 5)
        if time.time() - self.last_phase_change >= duration:
            self.phase += 1
            self.last_phase_change = time.time()

            # Loop or end
            if self.phase >= len(phases):
                self.phase = 0  # loop scenario

            state["events"].append({
                "type": "scenario_phase_change",
                "phase": self.phase,
                "timestamp": time.time(),
            })
