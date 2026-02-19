"""
Simple OpenClaw-style phishing campaign organ.
"""

from dataclasses import dataclass, field
from typing import List, Dict


STAGES = ["PLANNING", "LINK_GENERATED", "DELIVERED", "VICTIM_INTERACTED", "CREDENTIALS_CAPTURED"]


@dataclass
class Campaign:
    id: str
    stage_index: int = 0
    anomaly_score: float = 0.0
    blocked: bool = False
    honeypot: bool = False
    metadata: Dict = field(default_factory=dict)


class OpenClawOrgan:
    def __init__(self):
        self.campaigns: Dict[str, Campaign] = {}

    def start_campaign(self, cid: str, anomaly_score: float = 0.1):
        self.campaigns[cid] = Campaign(id=cid, anomaly_score=anomaly_score)

    def advance_stage(self, cid: str):
        camp = self.campaigns.get(cid)
        if not camp or camp.blocked:
            return
        if camp.stage_index < len(STAGES) - 1:
            camp.stage_index += 1

    def block_campaign(self, cid: str):
        camp = self.campaigns.get(cid)
        if camp:
            camp.blocked = True

    def mark_honeypot(self, cid: str):
        camp = self.campaigns.get(cid)
        if camp:
            camp.honeypot = True

    def metrics(self) -> Dict[str, float]:
        active = [c for c in self.campaigns.values() if not c.blocked]
        if not active:
            return {
                "red_active_campaigns": 0.0,
                "red_stage_sum": 0.0,
                "red_max_anomaly": 0.0,
                "red_any_blocked": 0.0,
                "red_honeypot": 0.0,
                "red_max_campaigns": 10.0,
                "red_max_stage": float(len(STAGES) - 1),
            }

        stage_sum = sum(c.stage_index for c in active)
        max_anomaly = max(c.anomaly_score for c in active)
        any_blocked = 1.0 if any(c.blocked for c in self.campaigns.values()) else 0.0
        any_honeypot = 1.0 if any(c.honeypot for c in self.campaigns.values()) else 0.0

        return {
            "red_active_campaigns": float(len(active)),
            "red_stage_sum": float(stage_sum),
            "red_max_anomaly": float(max_anomaly),
            "red_any_blocked": any_blocked,
            "red_honeypot": any_honeypot,
            "red_max_campaigns": 10.0,
            "red_max_stage": float(len(STAGES) - 1),
        }
