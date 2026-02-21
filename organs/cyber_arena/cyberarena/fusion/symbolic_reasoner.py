from typing import Dict


def regime_symbol(agent_id: str, role: str, regime: str) -> Dict[str, str]:
    """
    Returns a simple symbolic event dict you can push into your narrative/telemetry.
    """
    return {
        "type": "REGIME_UPDATE",
        "agent_id": agent_id,
        "role": role,
        "regime": regime,
        "symbol": f"REGIME:{role}_{regime}"
    }
