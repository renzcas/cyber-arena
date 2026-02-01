# core/agent_memory.py

import time
from typing import Dict, Any, List


class AgentMemory:
    """
    Non-harmful cognitive layer for agents.
    Agents gain short-term sensory traces and long-term tendencies.
    """

    def __init__(self):
        self.short_term_window = 5      # seconds
        self.long_term_decay = 0.99     # slow decay of tendencies

    def update(self, entity: Dict[str, Any]) -> None:
        """
        Update memory for a single entity.
        """

        now = time.time()

        # Initialize memory if missing
        if "memory" not in entity:
            entity["memory"] = {
                "short_term": [],
                "long_term": {},
                "last_update": now,
            }

        mem = entity["memory"]

        # -------------------------
        # Short-term memory
        # -------------------------
        # Store sensed signals with timestamps
        if "signals" in entity:
            for sig in entity["signals"]:
                mem["short_term"].append({
                    "signal": sig,
                    "timestamp": now,
                })

        # Remove old short-term memories
        mem["short_term"] = [
            item for item in mem["short_term"]
            if now - item["timestamp"] <= self.short_term_window
        ]

        # -------------------------
        # Long-term tendencies
        # -------------------------
        # Count how often each signal type appears
        for item in mem["short_term"]:
            sig_id = item["signal"]["id"]
            mem["long_term"][sig_id] = mem["long_term"].get(sig_id, 0) + 1

        # Apply decay
        for key in list(mem["long_term"].keys()):
            mem["long_term"][key] *= self.long_term_decay
            if mem["long_term"][key] < 0.01:
                del mem["long_term"][key]

        mem["last_update"] = now
