# cyberarena/libs/infophyzx/physics_adapter.py

from typing import Dict, Any

class PhysicsAdapter:
    """
    Bridges InfoPhyzx physics engine → CyberArena fusion engine.
    Handles energy flows, interaction laws, and symbolic physics state.
    """

    def __init__(self):
        pass

    def energy_flow(self, energy_obj: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx energy engine output → CyberArena fusion payload.
        """
        return {
            "type": "physics.energy_flow",
            "payload": {
                "total": getattr(energy_obj, "total", None),
                "density_map": getattr(energy_obj, "density_map", None),
                "gradients": getattr(energy_obj, "gradients", None),
            }
        }

    def interaction_event(self, interaction_obj: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx interaction law event → CyberArena telemetry.
        """
        return {
            "type": "physics.interaction",
            "payload": {
                "a": getattr(interaction_obj, "a", None),
                "b": getattr(interaction_obj, "b", None),
                "force": getattr(interaction_obj, "force", None),
                "timestamp": getattr(interaction_obj, "timestamp", None),
            }
        }

    def symbolic_state(self, state_obj: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx symbolic physics state → CyberArena reasoning layer.
        """
        return {
            "symbols": getattr(state_obj, "symbols", None),
            "invariants": getattr(state_obj, "invariants", None),
            "phase": getattr(state_obj, "phase", None),
        }
