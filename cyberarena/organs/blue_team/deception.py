import random

def generate_deception_events(count: int = 5):
    events = []
    for i in range(count):
        events.append(f"Decoy triggered at honeypot-{i}: simulated event")
    return events
