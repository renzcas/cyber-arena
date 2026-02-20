import random
from cyberarena.organ_factory.registry import OrganRegistry
from cyberarena.telemetry.events import Event
from cyberarena.telemetry.stream import stream


# ---------------------------------------------------------
# Standalone recon function (your original code)
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Organ wrapper so CyberArena can run recon every tick
# ---------------------------------------------------------
class ReconOrgan:
    def __init__(self, target="localhost"):
        self.target = target

    async def update(self, env_state):
        """
        Called every environment tick by the Director.
        Runs a simulated recon scan and sends results to cockpit.
        """
        results = simulated_recon_scan(self.target)

        await stream.broadcast(Event.make(
            "recon.update",
            {"target": self.target, "results": results}
        ))


# Register organ with the factory
OrganRegistry.register("recon", ReconOrgan)
