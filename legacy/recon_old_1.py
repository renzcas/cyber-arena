import random

def simulated_recon_scan(target: str):
    if not target:
        return ["No target provided"]

    fake_ports = [22, 80, 443, 3306, 8080]
    open_ports = random.sample(fake_ports, random.randint(1, len(fake_ports)))

    return [
        f"Scanning {target}...",
        f"Open ports detected: {open_ports}",
        "Service fingerprinting (simulated)...",
        "OS guess: Linux (simulated)",
        "Recon complete."
    ]
