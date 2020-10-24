## 2D Linear Programming Solver

A simple Python program to solve 2D Linear Programming optimisation problems and can also
plot the constraints and feasible region to aid learning.

The program takes in a set of constraints and the objective function.
Note that the constraints must be inclusive relations (ie: '<=', '>=' or '==') because
strict inequalities do not make sense in a continuous setting. If you want integer solutions only, then just
convert your strict inequality into an inclusive one yourself, eg: change '5x - 2y < 3' to '5x - 2y <= 2'.

Here's an example (``example.py``) of its usage:

```
from objective_function import ObjectiveFunction
from constraint import Constraint2D
from optimiser_2d import optimise

# Example usage:

constraints = [
    Constraint2D(0, 1, 2, sign=">="),   # y >= 2
    Constraint2D(1, 2, 25, sign="<="),  # x + 2y <= 25
    Constraint2D(-2, 4, -8, sign=">="), # -2x + 4y >= 8
    Constraint2D(-2, 1, -5, sign="<="), # -2x + y >= -5
    Constraint2D(1, 0, 5, sign=">=")    # x >= 5
]

optimise(ObjectiveFunction(3, 2), constraints, type="max", visual=True, integer_only=True)
```
- The ``type`` argument can take either ``"max"`` or ``"min"`` depending on your objective.
- The ``visual`` argument can be set to ``True`` if you want a visual plot of the feasible region and constraints
- The ``integer_only`` argument can be set to ``True`` if you want an integer only solution
