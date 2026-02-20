# cyberarena/director/director.py

from typing import Any, Dict, List

from cyberarena.director.scheduler import Scheduler
from cyberarena.director.narrative_hooks import NarrativeHooks
from cyberarena.organ_factory.loader import load_all_organs
from cyberarena.organ_factory.factory import OrganFactory
from cyberarena.organ_factory.registry import OrganRegistry


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

        # Load all organ modules (auto-discovers organs)
        load_all_organs()

        # Instantiate all registered organs
        for name, organ_cls in OrganRegistry.all().items():
            self.organs.append(organ_cls())

    def register_organ(self, organ):
        """Manually attach an organ to the simulation."""
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
