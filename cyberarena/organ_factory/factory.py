# cyberarena/organ_factory/factory.py

from cyberarena.organ_factory.registry import OrganRegistry


class OrganFactory:
    """
    Creates organ instances by name.
    """

    @staticmethod
    def create(name, **kwargs):
        organ_cls = OrganRegistry.get(name)
        if not organ_cls:
            raise ValueError(f"Organ '{name}' not found in registry.")
        return organ_cls(**kwargs)
