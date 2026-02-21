# cyberarena/environment/cyber_env.py

import asyncio
from typing import Any, Dict

from cyberarena.environment.base_env import BaseEnvironment
from cyberarena.libs.infophyzx.field_adapter import FieldAdapter
from cyberarena.fusion.fusion_engine import FusionEngine


class CyberEnvironment(BaseEnvironment):
    """
    The main CyberArena environment.
    Integrates:
      - InfoPhyzx engine (optional)
      - FieldAdapter
      - FusionEngine
    """

    def __init__(self, infophyzx_engine=None):
        super().__init__()
        self.infophyzx_engine = infophyzx_engine
        self.field_adapter = FieldAdapter()
        self.fusion = FusionEngine()

    # ---------------------------------------------------------
    # Reset the environment
    # ---------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        self.t = 0
        self.state = {"t": self.t}

        if self.infophyzx_engine:
            self.field_state = self.infophyzx_engine.reset()

        return self.state

    # ---------------------------------------------------------
    # Step the environment with an action
    # ---------------------------------------------------------
    def step(self, action: Any) -> Dict[str, Any]:
        self.t += 1
        self.state["t"] = self.t

        if self.infophyzx_engine:
            self.field_state = self.infophyzx_engine.step(action)

        return self.state

    # ---------------------------------------------------------
    # Async heartbeat loop
    # ---------------------------------------------------------
    async def tick(self):
        """
        Called every second by the orchestrator.
        Pulls InfoPhyzx state → converts → broadcasts → fusion.
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

        # Fusion Engine: process physics → cockpit
        if self.field_state:
            if hasattr(self.field_state, "energy"):
                await self.fusion.process_energy(self.field_state.energy)

            if hasattr(self.field_state, "interactions"):
                for interaction in self.field_state.interactions:
                    await self.fusion.process_interaction(interaction)

            if hasattr(self.field_state, "symbolic"):
                await self.fusion.process_symbolic(self.field_state.symbolic)

        await asyncio.sleep(1)
