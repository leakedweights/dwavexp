
from dataclasses import dataclass
import inspect
from typing import Any, Optional, Sequence

AgentParam = [Sequence | Any]


@dataclass
class SolverConfig:
    pass


@dataclass
class AgentConfig(SolverConfig):
    pass


class TrackedSolver:
    def __init__(self, solver: Any, config: Optional[SolverConfig] = None):
        if config is not None:
            self.tracked_methods = []
        else:
            self.tracked_methods = self.get_solver_methods(solver)

    def auth(self, wandb):
        pass

    @staticmethod
    def get_solver_methods(solver: Any):
        methods = [member[0] for member in inspect.getmembers(
            solver, predicate=inspect.isfunction)]
        return methods

    def __getattr__(self, name):
        orig_attr = getattr(self._dwave_solver, name)

        if callable(orig_attr) and name in self._tracked_methods:
            def wrapped(*args, **kwargs):
                print(f"Before calling {name}")

                result = orig_attr(*args, **kwargs)

                print(f"After calling {name}")
                return result

            return wrapped
        return orig_attr


class SolverAgent:
    def __init__(self, solver: Any, config: AgentConfig):
        pass

    def run(self):
        pass
