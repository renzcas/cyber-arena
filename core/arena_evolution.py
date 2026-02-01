from dataclasses import dataclass
from typing import List, Dict, Any, Callable
import random


@dataclass
class ArenaIndividual:
  id: str
  config: Dict[str, Any]
  fitness: float = 0.0


class ArenaEvolutionEngine:
  def __init__(
    self,
    evaluate_fn: Callable[[Dict[str, Any]], float],
    mutation_rate: float = 0.1,
  ):
    self.evaluate_fn = evaluate_fn
    self.mutation_rate = mutation_rate
    self.population: List[ArenaIndividual] = []

  def initialize_population(self, seeds: List[Dict[str, Any]]):
    self.population = [
      ArenaIndividual(id=f"ind_{i}", config=cfg) for i, cfg in enumerate(seeds)
    ]

  def evaluate_population(self):
    for ind in self.population:
      ind.fitness = self.evaluate_fn(ind.config)

  def select_top_k(self, k: int) -> List[ArenaIndividual]:
    return sorted(self.population, key=lambda x: x.fitness, reverse=True)[:k]

  def mutate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
    new_cfg = dict(config)
    for key, value in config.items():
      if isinstance(value, (int, float)) and random.random() < self.mutation_rate:
        new_cfg[key] = value * (0.8 + 0.4 * random.random())
    return new_cfg

  def evolve_step(self, k: int = 5):
    self.evaluate_population()
    elites = self.select_top_k(k)
    new_population: List[ArenaIndividual] = elites.copy()

    while len(new_population) < len(self.population):
      parent = random.choice(elites)
      child_cfg = self.mutate_config(parent.config)
      new_population.append(
        ArenaIndividual(id=f"ind_{len(new_population)}", config=child_cfg)
      )

    self.population = new_population
