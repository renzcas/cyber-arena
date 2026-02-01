# core/resource_nodes.py

import random
import time
from typing import Dict, Any, List


class ResourceNodes:
    """
    Non-harmful ecosystem nodes that agents can sense and interact with.
    """

    def __init__(self):
        self.spawn_interval = 10  # seconds
        self.last_spawn = time.time()

    def update(self, state: Dict[str, Any]) -> None:
        """
        Update resource nodes each tick.
        Spawn new nodes periodically.
        """

        if "nodes" not in state:
            state["nodes"] = []

        # Spawn new nodes periodically
        if time.time() - self.last_spawn >= self.spawn_interval:
            new_node = self._spawn_node()
            state["nodes"].append(new_node)
            self.last_spawn = time.time()

            state["events"].append({
                "type": "node_spawned",
                "node": new_node,
                "timestamp": time.time(),
            })

        # Update existing nodes (e.g., decay, pulse)
        for node in state["nodes"]:
            node["pulse"] = random.uniform(0.8, 1.2)

    # -------------------------
    # Node Creation
    # -------------------------
    def _spawn_node(self) -> Dict[str, Any]:
        node_type = random.choice(["energy_well", "signal_beacon", "data_cache", "anomaly_field"])
        return {
            "id": f"node_{int(time.time() * 1000)}",
            "type": node_type,
            "x": random.uniform(-15, 15),
            "y": random.uniform(-15, 15),
            "pulse": 1.0,
        }
