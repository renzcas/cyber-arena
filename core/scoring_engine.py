class ScoringEngine:
    def __init__(self):
        self.scores = {"RED": 0, "BLUE": 0, "PURPLE": 0}

    def on_event(self, event: dict):
        etype = event.get("type")
        if etype == "CREDENTIALS_CAPTURED":
            self.scores["RED"] += 50
        elif etype == "EARLY_DETECTION":
            self.scores["BLUE"] += 30
        elif etype == "CRITICAL_BLOCK":
            self.scores["BLUE"] += 50
        elif etype == "HONEYPOT_DEPLOYED":
            self.scores["BLUE"] += 20
        elif etype == "ANNOTATION_ADDED":
            self.scores["PURPLE"] += 10

    def snapshot(self):
        return dict(self.scores)
