# cyberarena/director/scheduler.py

from typing import Callable, Dict, List, Any
import asyncio


class Scheduler:
    """
    Runs timed tasks every N ticks.
    """

    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []

    def every(self, n: int, fn: Callable):
        """Schedule a function to run every n ticks."""
        self.tasks.append({"interval": n, "fn": fn})

    async def run(self, env_state: Dict[str, Any]):
        t = env_state.get("t", 0)

        for task in self.tasks:
            if t % task["interval"] == 0:
                await task["fn"](env_state)
