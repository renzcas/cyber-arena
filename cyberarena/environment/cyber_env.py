# cyberarena/environment/cyber_env.py

import asyncio
from typing import Any, Dict

from cyberarena.environment.base_env import BaseEnvironment
from cyberarena.libs.infophyzx.field_adapter import FieldAdapter


class CyberEnvironment(BaseEnvironment):
    """
    The main CyberArena environment.
    Extends BaseEnvironment with:
      - InfoPhyzx field integration
      - async tick loop
      - action handling
    """

    def __init__(self, infophyzx_engine=None):
        super().__init__()
        self.infophyzx_engine = infophyzx_engine
        self.field_adapter = FieldAdapter()

    # ---------------------------------------------------------
    # Reset the environment
    # ---------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        self.t = 0
        self.state = {"t": self.t}

        # Reset InfoPhyzx engine if present
        if self.infophyzx_engine:
            self.field_state = self.infophyzx_engine.reset()

        return self.state

    # ---------------------------------------------------------
    # Step the environment with an action
    # ---------------------------------------------------------
    def step(self, action: Any) -> Dict[str, Any]:
        self.t += 1
        self.state["t"] = self.t

        # Apply action to InfoPhyzx engine if present
        if self.infophyzx_engine:
            self.field_state = self.infophyzx_engine.step(action)

        return self.state

    # ---------------------------------------------------------
    # Async heartbeat loop
    # ---------------------------------------------------------
    async def tick(self):
        """
        Called every second by the orchestrator.
        Pulls InfoPhyzx field state → converts → broadcasts.
        """
        self.t += 1

        # Pull physics state if engine exists
        if self.infophyzx_engine:
            self.field_state = self.infophyzx_engine.get_state()
        else:
            self.field_state = None

        # Convert InfoPhyzx → CyberArena
        converted = self.field_adapter.from_infophyzx(self.field_state)
        event = self.field_adapter.to_environment_tick(converted)

        # Broadcast to cockpit
        from cyberarena.telemetry.events import Event
        from cyberarena.telemetry.stream import stream

        await stream.broadcast(Event.make("env.tick", event["payload"]))

        await asyncio.sleep(1)
