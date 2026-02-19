# cyberarena/director/director.py

from typing import Any, Dict, List
from cyberarena.director.scheduler import Scheduler
from cyberarena.director.narrative_hooks import NarrativeHooks


class Director:
    """
    The Director orchestrates the entire CyberArena simulation.
    It receives environment ticks, evaluates triggers, activates organs,
    and pushes narrative events.
    """

    def __init__(self):
        self.scheduler = Scheduler()
        self.narrative = NarrativeHooks()
        self.organs: List[Any] = []

    def register_organ(self, organ):
        """Attach an organ to the simulation."""
        self.organs.append(organ)

    async def on_tick(self, env_state: Dict[str, Any]):
        """
        Called every environment tick.
        Runs:
          - scheduled tasks
          - narrative triggers
          - organ updates
        """
        await self.scheduler.run(env_state)
        await self.narrative.check_triggers(env_state)

        for organ in self.organs:
            await organ.update(env_state)
