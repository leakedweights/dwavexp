
from dataclasses import dataclass
import inspect
import time
from typing import Any, Optional, Sequence

AgentParam = [Sequence | Any]


@dataclass
class SolverConfig:
    track_runtimes: bool = True


@dataclass
class AgentConfig(SolverConfig):
    pass


class TrackedSolver:

    """
    Solver with WandB experiment-tracking.

    Usage:
    ```
    config = SolverConfig(...)
    solver = MockSolver(...)
    solver = TrackedSolver(solver, config)

    solver.my_method(x)
    ```
    """

    def __init__(self, solver: Any, config: Optional[SolverConfig] = None):
        self._dwave_solver = solver
        self.config = config or SolverConfig()

        self._tracked_methods = self.get_solver_methods(solver)

    def auth(self, wandb):
        pass

    @staticmethod
    def get_solver_methods(solver: Any):
        methods = [member[0] for member in inspect.getmembers(
            solver.__class__, predicate=inspect.isfunction)]
        return methods

    def __getattr__(self, name):
        try:
            orig_attr = getattr(self._dwave_solver, name)
        except AttributeError:
            raise AttributeError(
                f"{name} not found in {type(self._dwave_solver).__name__}")

        if callable(orig_attr) and name in self._tracked_methods:
            def wrapped(*args, **kwargs):
                start_time = time.time()

                result = orig_attr(*args, **kwargs)

                end_time = time.time()
                elapsed_time_ms = (end_time - start_time) * 1000

                if self.config.track_runtimes:
                    print(f"Execution time: {elapsed_time_ms:.3f} ms.")

                return result

            return wrapped
        else:
            return orig_attr


class SolverAgent:
    def __init__(self, solver: Any, config: AgentConfig):
        pass

    def run(self):
        pass
