from typing import Dict
from .energy_engine import EnergyEngine

ENERGY_ENGINE = EnergyEngine()

AGENT_ROLES = {
    "agent_red_1": "RED",
    "agent_blue_1": "BLUE",
    "agent_purple_1": "PURPLE",
}


def update_from_metrics(metrics: Dict[str, float]):
    """
    metrics: flat dict from CyberArena telemetry, e.g.:
      {
        "red_active_campaigns": ...,
        "red_stage_sum": ...,
        "red_max_anomaly": ...,
        "red_any_blocked": 0/1,
        "red_honeypot": 0/1,
        "blue_defense_actions": ...,
        "blue_conflicts": ...,
        "blue_system_risk": ...,
        "blue_cred_risk": ...,
        "purple_symbolic_events": ...,
        "purple_distinct_symbols": ...,
      }
    """

    # RED
    max_campaigns = max(metrics.get("red_max_campaigns", 1), 1)
    max_stage = max(metrics.get("red_max_stage", 1), 1)
    active = metrics.get("red_active_campaigns", 0.0)
    stage_sum = metrics.get("red_stage_sum", 0.0)
    lambda_weight = 0.3

    if active > 0:
        stage_term = (stage_sum / (max_stage * active))
    else:
        stage_term = 0.0

    campaign_intensity = (active / max_campaigns) + lambda_weight * stage_term
    anomaly_pressure = metrics.get("red_max_anomaly", 0.0)
    defense_pressure = metrics.get("red_any_blocked", 0.0) + 0.5 * metrics.get("red_honeypot", 0.0)
    honeypot_risk = metrics.get("red_honeypot", 0.0)

    q_red = {
        "campaign_intensity": campaign_intensity,
        "anomaly_pressure": anomaly_pressure,
        "defense_pressure": defense_pressure,
        "honeypot_risk": honeypot_risk,
    }
    ENERGY_ENGINE.update_agent("agent_red_1", "RED", q_red)

    # BLUE
    window = max(metrics.get("blue_window", 10.0), 1.0)
    control_effort = metrics.get("blue_defense_actions", 0.0) / window
    conflict_tension = metrics.get("blue_conflicts", 0.0)
    system_risk = metrics.get("blue_system_risk", 0.0)
    cred_risk = metrics.get("blue_cred_risk", 0.0)

    q_blue = {
        "control_effort": control_effort,
        "conflict_tension": conflict_tension,
        "system_risk": system_risk,
        "cred_risk": cred_risk,
    }
    ENERGY_ENGINE.update_agent("agent_blue_1", "BLUE", q_blue)

    # PURPLE
    sym_window = max(metrics.get("purple_window", 10.0), 1.0)
    symbolic_load = metrics.get("purple_symbolic_events", 0.0) / sym_window
    max_symbols = max(metrics.get("purple_max_symbols", 10.0), 1.0)
    system_entropy = metrics.get("purple_distinct_symbols", 0.0) / max_symbols

    q_purple = {
        "symbolic_load": symbolic_load,
        "system_entropy": system_entropy,
    }
    ENERGY_ENGINE.update_agent("agent_purple_1", "PURPLE", q_purple)
