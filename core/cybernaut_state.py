from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List


class CybernautMode(str, Enum):
  OBSERVE = "observe"
  PROBE = "probe"
  ATTACK = "attack"
  DEFEND = "defend"
  EXPLAIN = "explain"


@dataclass
class CybernautContext:
  id: str
  mode: CybernautMode
  perspective: str  # e.g. "red", "blue", "grey", "teacher"
  memory: Dict[str, Any]
  focus_targets: List[str]


class CybernautStateMachine:
  def __init__(self):
    self._contexts: Dict[str, CybernautContext] = {}

  def get_or_create(self, cybernaut_id: str) -> CybernautContext:
    if cybernaut_id not in self._contexts:
      self._contexts[cybernaut_id] = CybernautContext(
        id=cybernaut_id,
        mode=CybernautMode.OBSERVE,
        perspective="teacher",
        memory={},
        focus_targets=[],
      )
    return self._contexts[cybernaut_id]

  def transition_mode(self, cybernaut_id: str, new_mode: CybernautMode):
    ctx = self.get_or_create(cybernaut_id)
    # simple guardrail example
    if ctx.mode == CybernautMode.ATTACK and new_mode == CybernautMode.EXPLAIN:
      # allow, but log
      pass
    ctx.mode = new_mode
    return ctx

  def update_focus(self, cybernaut_id: str, targets: List[str]):
    ctx = self.get_or_create(cybernaut_id)
    ctx.focus_targets = targets
    return ctx

  def snapshot(self, cybernaut_id: str) -> Dict[str, Any]:
    ctx = self.get_or_create(cybernaut_id)
    return {
      "id": ctx.id,
      "mode": ctx.mode.value,
      "perspective": ctx.perspective,
      "focus_targets": ctx.focus_targets,
    }
