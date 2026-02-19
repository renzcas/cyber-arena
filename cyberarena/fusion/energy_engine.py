from dataclasses import dataclass
from typing import Dict, List, Tuple
import time


@dataclass
class AgentState:
    t: float
    q: Dict[str, float]
    dq: Dict[str, float]


class EnergyEngine:
    """
    Lagrangian + Hamiltonian energy tracking per agent.
    """

    def __init__(self):
        self.last_state: Dict[str, AgentState] = {}
        self.energy_history: Dict[str, List[Tuple[float, float, float]]] = {}
        self.state_history: Dict[str, List[AgentState]] = {}

        self.w_red = {"campaign_intensity": 1.0, "anomaly_pressure": 0.7}
        self.w_blue = {"control_effort": 1.0, "conflict_tension": 0.8}
        self.w_purple = {"symbolic_load": 1.0}

        self.v_red = {"defense_pressure": 1.0, "honeypot_risk": 0.5}
        self.v_blue = {"system_risk": 1.0, "cred_risk": 1.2}
        self.v_purple = {"system_entropy": 1.0}

        self.alpha = 1.0
        self.beta = 1.0

    def update_agent(self, agent_id: str, role: str, q: Dict[str, float]):
        now = time.time()
        prev = self.last_state.get(agent_id)

        if prev is None:
            dq = {k: 0.0 for k in q.keys()}
        else:
            dt = max(now - prev.t, 1e-6)
            dq = {k: (q.get(k, 0.0) - prev.q.get(k, 0.0)) / dt for k in q.keys()}

        state = AgentState(t=now, q=q, dq=dq)
        self.last_state[agent_id] = state
        self.state_history.setdefault(agent_id, []).append(state)
        self.state_history[agent_id] = self.state_history[agent_id][-500:]

        T, V = self._compute_T_V(role, q, dq)
        L = self.alpha * T - self.beta * V
        H = T + V

        self.energy_history.setdefault(agent_id, []).append((now, L, H))

    def _compute_T_V(self, role: str, q: Dict[str, float], dq: Dict[str, float]) -> Tuple[float, float]:
        if role == "RED":
            T = sum(self.w_red.get(k, 0.0) * (dq.get(k, 0.0) ** 2)
                    for k in ["campaign_intensity", "anomaly_pressure"])
            V = (self.v_red["defense_pressure"] * q.get("defense_pressure", 0.0) +
                 self.v_red["honeypot_risk"] * q.get("honeypot_risk", 0.0))
        elif role == "BLUE":
            T = sum(self.w_blue.get(k, 0.0) * (dq.get(k, 0.0) **2)
                    for k in ["control_effort", "conflict_tension"])
            V = (self.v_blue["system_risk"] * q.get("system_risk", 0.0) +
                 self.v_blue["cred_risk"] * q.get("cred_risk", 0.0))
        elif role == "PURPLE":
            T = self.w_purple["symbolic_load"] * (dq.get("symbolic_load", 0.0) ** 2)
            V = self.v_purple["system_entropy"] * q.get("system_entropy", 0.0)
        else:
            T = 0.0
            V = 0.0
        return T, V

    def get_all_series(self) -> Dict[str, List[Tuple[float, float, float]]]:
        return self.energy_history

    def get_state_history(self) -> Dict[str, List[AgentState]]:
        return self.state_history
