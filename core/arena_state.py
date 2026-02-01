'''def get_arena_state():
    return {
        "red_team": {"status": "active"},
        "blue_team": {"status": "defending"},
        "grey_team": {"status": "idle"},
        "metrics": {
            "attack_intensity": 0.42,
            "defense_load": 0.31
        },
        "scenario": {
            "name": "Basic Recon",
            "phase": "initial"
        }
    }

# core/arena_state.py

def get_arena_state(orchestrator):
    return orchestrator.get_state()
'''

# core/arena_state.py

from typing import Dict, Any
from core.orchestrator import ArenaOrchestrator

# Global reference (optional pattern)
_orchestrator: ArenaOrchestrator | None = None


def bind_orchestrator(orchestrator: ArenaOrchestrator) -> None:
    """
    Bind the global orchestrator reference so other modules
    can query arena state without circular imports.
    """
    global _orchestrator
    _orchestrator = orchestrator


def get_arena_state() -> Dict[str, Any]:
    """
    Return the current live arena state from the orchestrator.
    If the orchestrator is not yet bound, return a safe default.
    """
    if _orchestrator is None:
        return {
            "tick": 0,
            "timestamp": 0.0,
            "entities": [],
            "events": [],
            "status": "orchestrator_not_bound",
        }

    return _orchestrator.get_state()

