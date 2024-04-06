import time
from dwavexp import TrackedSolver, SolverConfig


class MockSolver:
    def my_method(self, x):
        time.sleep(1)
        return x


config = SolverConfig()
solver = MockSolver()
solver = TrackedSolver(solver, config)

solver.my_method(5)
