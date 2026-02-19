# cyberarena/libs/infophyzx/field_adapter.py

from typing import Dict, Any

class FieldAdapter:
    """
    Bridges InfoPhyzx cosmos_field → CyberArena environment state.
    Converts field tensors, energy maps, and particle states into
    CyberArena-friendly telemetry + environment snapshots.
    """

    def __init__(self):
        self.last_state = None

    def from_infophyzx(self, field_state: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx field_state object into a CyberArena dictionary.
        """
        if field_state is None:
            return {"status": "no_field"}

        return {
            "status": "ok",
            "t": getattr(field_state, "t", None),
            "energy": getattr(field_state, "energy", None),
            "particles": getattr(field_state, "particles", []),
            "dimensions": getattr(field_state, "dimensions", None),
        }

    def to_environment_tick(self, converted: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert the normalized field state into an environment tick payload.
        """
        return {
            "type": "field.tick",
            "payload": converted
        }
