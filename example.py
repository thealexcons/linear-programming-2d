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
