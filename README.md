# dwavexp - Experiment Tracking for D-Wave Solvers

A D-Wave utility for tracking runs and sweeps with WandB.

## Usage

```python
from dwavexp import TrackedSolver, SolverConfig

config = SolverConfig(...)
solver = MockSolver(...)
solver = TrackedSolver(solver, config)

solver.my_method(x)
```
