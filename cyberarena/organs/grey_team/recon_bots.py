import random

def automated_recon(target: str):
    if not target:
        return ["No target provided"]

    fake_findings = [
        "Simulated DNS lookup",
        "Simulated WHOIS query",
        "Simulated subdomain scan",
        "Simulated directory enumeration",
        "Simulated metadata extraction"
    ]

    sample = random.sample(fake_findings, random.randint(1, len(fake_findings)))

    return [f"Recon bot scanning {target}..."] + sample + ["Recon bot complete."]
