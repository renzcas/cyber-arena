import random

def evaluate_zero_trust(identity: str):
    if not identity:
        return "No identity provided."

    score = round(random.uniform(0.1, 0.95), 2)

    return f"Identity '{identity}' trust score: {score} (simulated)"
