from enum import Enum
from dataclasses import dataclass, field

class Mode(str, Enum):
    OBSERVE = "observe"
    PROBE = "probe"
    ATTACK = "attack"
    DEFEND = "defend"
    EXPLAIN = "explain"

@dataclass
class CybernautState:
    id: str
    mode: Mode = Mode.OBSERVE
    perspective: str = "neutral"
    memory: dict = field(default_factory=dict)
    focus: list = field(default_factory=list)

class CybernautStateMachine:
    def __init__(self):
        self._states = {}

    def get(self, cid: str) -> CybernautState:
        if cid not in self._states:
            self._states[cid] = CybernautState(id=cid)
        return self._states[cid]

    def set_mode(self, cid: str, mode: Mode):
        state = self.get(cid)
        state.mode = mode
        return state

    def set_focus(self, cid: str, targets: list):
        state = self.get(cid)
        state.focus = targets
        return state

    def snapshot(self, cid: str):
        s = self.get(cid)
        return {
            "id": s.id,
            "mode": s.mode.value,
            "perspective": s.perspective,
            "focus": s.focus,
        }
