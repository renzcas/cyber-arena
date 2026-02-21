# cyberarena/libs/infophyzx/bio_adapter.py

from typing import Dict, Any

class BioAdapter:
    """
    Bridges InfoPhyzx biological engine → CyberArena evolution engine.
    Handles genome, mutation, energy metabolism, and biological signals.
    """

    def __init__(self):
        pass

    def genome_to_agent(self, genome: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx genome object into CyberArena agent attributes.
        """
        return {
            "genes": getattr(genome, "genes", {}),
            "mutation_rate": getattr(genome, "mutation_rate", 0.0),
            "fitness": getattr(genome, "fitness", None),
        }

    def mutation_event(self, mutation_obj: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx mutation event → CyberArena telemetry event.
        """
        return {
            "type": "bio.mutation",
            "payload": {
                "gene": getattr(mutation_obj, "gene", None),
                "delta": getattr(mutation_obj, "delta", None),
                "timestamp": getattr(mutation_obj, "timestamp", None),
            }
        }

    def energy_to_agent(self, energy_obj: Any) -> Dict[str, Any]:
        """
        Convert InfoPhyzx biological energy → CyberArena agent energy.
        """
        return {
            "energy": getattr(energy_obj, "value", None),
            "metabolism": getattr(energy_obj, "metabolism", None),
        }
