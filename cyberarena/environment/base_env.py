# cyberarena/environment/base_env.py

import asyncio
from typing import Any, Dict

from cyberarena.telemetry.events import Event
from cyberarena.telemetry.stream import stream
from cyberarena.libs.infophyzx.field_adapter import FieldAdapter


class BaseEnvironment:
    """
    Base class for all CyberArena environments.
    Provides:
      - reset()
      - step(action)
      - async tick() loop
      - InfoPhyzx → CyberArena field adapter integration
    """

    def __init__(self):
        self.t = 0
        self.field_adapter = FieldAdapter()
        self.state: Dict[str, Any] = {}

    # ---------------------------------------------------------
    # Classic Gym-style API
    # ---------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        """
        Reset the environment to its initial state.
        Override in subclasses.
        """
        self.t = 0
        self.state = {"t": self.t}
        return self.state

    def step(self, action: Any) -> Dict[str, Any]:
        """
        Apply an action and update the environment.
        Override in subclasses.
        """
        self.t += 1
        self.state["t"] = self.t
        return self.state

    # ---------------------------------------------------------
    # Async heartbeat loop
    # ---------------------------------------------------------
    async def tick(self):
        """
        Called every loop iteration by the orchestrator.
        Override to integrate InfoPhyzx physics/biology.
        """
        self.t += 1

        # Convert InfoPhyzx field state → CyberArena format
        field_state = getattr(self, "field_state", None)
        converted = self.field_adapter.from_infophyzx(field_state)
        event = self.field_adapter.to_environment_tick(converted)

        # Broadcast to cockpit
        await stream.broadcast(Event.make("env.tick", event["payload"]))

        await asyncio.sleep(1)
