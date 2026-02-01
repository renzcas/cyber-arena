# core/entity_engine.py

import random
import time
from typing import Dict, Any, List

from core.agent_memory import AgentMemory


class EntityEngine:
    """
    Non-harmful adaptive agents that move, sense, and react.
    """

    def __init__(self):
        self.default_speed = 0.5
        self.sense_range = 5.0
        self.memory = AgentMemory()

    def update(self, state: Dict[str, Any]) -> None:
        """
        Update all entities each tick.
        """

        entities = state["entities"]

        # If no entities exist, spawn one
        if not entities:
            entities.append(self._spawn_entity("agent_1"))
            return

        # Update each entity
        for entity in entities:
            self._update_energy(entity)
            self._update_state(entity, entities)
            self._move(entity)
            self._sense(entity, entities, state.get("nodes", []))
            self.memory.update(entity)

        # Emit event
        state["events"].append({
            "type": "entity_update",
            "timestamp": time.time(),
            "count": len(entities),
        })

    # -------------------------
    # Entity Creation
    # -------------------------
    def _spawn_entity(self, eid: str) -> Dict[str, Any]:
        return {
            "id": eid,
            "x": random.uniform(-10, 10),
            "y": random.uniform(-10, 10),
            "vx": 0.0,
            "vy": 0.0,
            "energy": 100,
            "state": "idle",
            "last_state_change": time.time(),
            "signals": [],
            "memory": {
                "short_term": [],
                "long_term": {},
                "last_update": time.time(),
            },
        }

    # -------------------------
    # Energy System
    # -------------------------
    def _update_energy(self, entity: Dict[str, Any]) -> None:
        entity["energy"] = max(0, entity["energy"] - 0.1)

    # -------------------------
    # State Machine
    # -------------------------
    def _update_state(self, entity: Dict[str, Any], entities: List[Dict[str, Any]]) -> None:
        # Simple non-harmful state transitions
        if entity["energy"] < 20:
            entity["state"] = "resting"
        else:
            entity["state"] = random.choice(["idle", "exploring"])

    # -------------------------
    # Movement
    # -------------------------
    def _move(self, entity: Dict[str, Any]) -> None:
        if entity["state"] == "exploring":
            entity["vx"] = random.uniform(-self.default_speed, self.default_speed)
            entity["vy"] = random.uniform(-self.default_speed, self.default_speed)
        else:
            entity["vx"] = 0
            entity["vy"] = 0

        entity["x"] += entity["vx"]
        entity["y"] += entity["vy"]

    # -------------------------
    # Sensing
    # -------------------------
    def _sense(
        self,
        entity: Dict[str, Any],
        entities: List[Dict[str, Any]],
        nodes: List[Dict[str, Any]],
    ) -> None:
        sensed: List[Dict[str, Any]] = []

        # Sense other entities
        for other in entities:
            if other["id"] == entity["id"]:
                continue

            dx = other["x"] - entity["x"]
            dy = other["y"] - entity["y"]
            dist = (dx * dx + dy * dy) ** 0.5

            if dist <= self.sense_range:
                sensed.append({
                    "type": "entity",
                    "id": other["id"],
                    "distance": dist,
                })

        # Sense resource nodes
        for node in nodes:
            dx = node["x"] - entity["x"]
            dy = node["y"] - entity["y"]
            dist = (dx * dx + dy * dy) ** 0.5

            if dist <= self.sense_range:
                sensed.append({
                    "type": "node",
                    "id": node["id"],
                    "node_type": node["type"],
                    "distance": dist,
                })

        entity["signals"] = sensed
