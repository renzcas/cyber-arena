# cyberarena/organ_factory/registry.py

class OrganRegistry:
    """
    Holds a list of all available organs.
    Organs register themselves here at import time.
    """

    _organs = {}

    @classmethod
    def register(cls, name, organ_cls):
        cls._organs[name] = organ_cls

    @classmethod
    def get(cls, name):
        return cls._organs.get(name)

    @classmethod
    def all(cls):
        return cls._organs
