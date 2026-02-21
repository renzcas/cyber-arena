# cyberarena/fusion/fusion_engine.py

from cyberarena.libs.infophyzx.physics_adapter import PhysicsAdapter
from cyberarena.telemetry.events import Event
from cyberarena.telemetry.stream import stream


class FusionEngine:
    """
    The Fusion Engine merges InfoPhyzx physics output with CyberArena state.
    It converts:
      - energy flows
      - interactions
      - symbolic physics state
    into CyberArena telemetry events.
    """

    def __init__(self):
        self.adapter = PhysicsAdapter()

    async def process_energy(self, energy_obj):
        """Convert InfoPhyzx energy → cockpit event."""
        payload = self.adapter.energy_flow(energy_obj)
        await stream.broadcast(Event.make("fusion.energy", payload["payload"]))

    async def process_interaction(self, interaction_obj):
        """Convert InfoPhyzx interaction → cockpit event."""
        payload = self.adapter.interaction_event(interaction_obj)
        await stream.broadcast(Event.make("fusion.interaction", payload["payload"]))

    async def process_symbolic(self, state_obj):
        """Convert InfoPhyzx symbolic state → cockpit event."""
        payload = self.adapter.symbolic_state(state_obj)
        await stream.broadcast(Event.make("fusion.symbolic", payload))
