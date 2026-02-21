from typing import Dict, List, Tuple
from .energy_engine import AgentState


def build_phase_space(history: Dict[str, List[AgentState]],
                      coord_map: Dict[str, str]) -> Dict[str, List[Tuple[float, float, float]]]:
    """
    Returns: agent_id -> list[(t, x, dx)]
    """
    result: Dict[str, List[Tuple[float, float, float]]] = {}
    for agent_id, states in history.items():
        coord = coord_map.get(agent_id)
        if not coord:
            continue
        pts: List[Tuple[float, float, float]] = []
        for st in states:
            x = st.q.get(coord, 0.0)
            dx = st.dq.get(coord, 0.0)
            pts.append((st.t, x, dx))
        result[agent_id] = pts
    return result
