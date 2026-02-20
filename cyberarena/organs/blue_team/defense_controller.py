from typing import Dict


class DefenseController:
    def __init__(self):
        self.defense_actions_window = 0
        self.conflicts = 0
        self.system_risk = 0.0
        self.cred_risk = 0.0

    def record_defense_action(self, action_type: str):
        self.defense_actions_window += 1
        if action_type in ("BLOCK_CAMPAIGN", "DEPLOY_HONEYPOT"):
            self.conflicts += 1

    def update_risk(self, system_risk: float, cred_risk: float):
        self.system_risk = system_risk
        self.cred_risk = cred_risk

    def metrics(self) -> Dict[str, float]:
        return {
            "blue_defense_actions": float(self.defense_actions_window),
            "blue_conflicts": float(self.conflicts),
            "blue_system_risk": float(self.system_risk),
            "blue_cred_risk": float(self.cred_risk),
            "blue_window": 10.0,
        }

    def reset_window(self):
        self.defense_actions_window = 0
        self.conflicts = 0
