from objective_function import ObjectiveFunction
from constraint import Constraint
from optimiser_2d import optimise

# Example usage

constraints = [
    Constraint(0, 1, 2, sign=">="), # y >= 2
    Constraint(1, 2, 25, sign="<="), # x + 2*y <= 25
    Constraint(-2, 4, -8, sign=">="), # -2*x + 4*y >= 8
    Constraint(-2, 1, -5, sign="<=") # -2*x + y >= -5
]

objective_function = ObjectiveFunction(3, 2)
optimise(objective_function, constraints, type="max", visual=True, integer_only=True)
