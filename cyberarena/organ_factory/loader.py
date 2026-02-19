# cyberarena/organ_factory/loader.py

import pkgutil
import importlib
import cyberarena.organs as organs_pkg


def load_all_organs():
    """
    Auto-import all modules inside cyberarena.organs.*
    Any organ that calls OrganRegistry.register() will be available.
    """
    for module in pkgutil.walk_packages(organs_pkg.__path__, organs_pkg.__name__ + "."):
        importlib.import_module(module.name)
