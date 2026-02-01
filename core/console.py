# core/console.py

import time
from typing import Any, Dict, List


class Console:
    """
    Team consoles for red/blue/grey/system command channels.
    Commands are queued and safely applied inside the orchestrator tick.
    """

    def __init__(self):
        self._queue: List[Dict[str, Any]] = []

    def enqueue(self, channel: str, command: Dict[str, Any]) -> None:
        """
        Queue a command to be applied on the next tick.
        """
        self._queue.append({
            "channel": channel,
            "command": command,
            "timestamp": time.time(),
        })

    def flush(self, state: Dict[str, Any]) -> None:
        """
        Apply all queued commands to the arena state and emit events.
        """
        if not self._queue:
            return

        # For now, we log commands as events and leave
        # interpretation to higher-level organs (scenarios/entities).
        for item in self._queue:
            state["events"].append({
                "type": "console_command",
                "channel": item["channel"],
                "command": item["command"],
                "timestamp": item["timestamp"],
            })

        # Clear queue after applying
        self._queue.clear()
