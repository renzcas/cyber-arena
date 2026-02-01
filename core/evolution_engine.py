# core/evolution_engine.py

import random
import time
from typing import Dict, Any, List


class EvolutionEngine:
    def __init__(self):
        self.last_mutation_time = time.time()

    def evolve(self, state: Dict[str, Any]) -> None:
        """
        Mutate entities slightly every tick.
        If no entities exist, create a starter one.
        """

        # Initialize if empty
        if not state["entities"]:
            state["entities"].append({
                "id": "entity_1",
                "energy": 100,
                "fitness": 1.0,
                "mutation_rate": 0.05,
            })
            return

        # Mutate each entity
        for entity in state["entities"]:
            mutation = (random.random() - 0.5) * entity["mutation_rate"]
            entity["fitness"] = max(0.0, entity["fitness"] + mutation)

            # Energy decay
            entity["energy"] = max(0, entity["energy"] - 1)

        # Emit event
        state["events"].append({
            "type": "evolution_tick",
            "timestamp": time.time(),
            "entities": len(state["entities"]),
        })
