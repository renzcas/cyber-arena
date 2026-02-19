# cyberarena/director/narrative_hooks.py

from typing import Dict, Any
from cyberarena.telemetry.events import Event
from cyberarena.telemetry.stream import stream


class NarrativeHooks:
    """
    Simple narrative engine.
    Fires events when conditions are met.
    """

    async def check_triggers(self, env_state: Dict[str, Any]):
        t = env_state.get("t", 0)

        # Example trigger: send a narrative event at t=5
        if t == 5:
            await stream.broadcast(Event.make(
                "narrative.event",
                {"msg": "The simulation reaches its first milestone."}
            ))
