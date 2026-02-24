from typing import Dict
from .models import Target

targets: Dict[str, Target] = {}

def register_target(target: Target):
    targets[target.name] = target

def list_targets():
    return list(targets.values())
