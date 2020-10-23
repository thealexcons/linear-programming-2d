import matplotlib.pyplot as plt
import numpy as np
from objective_function import ObjectiveFunction
from constraint import Constraint

# Solves a 2D linear programming problem
def optimise(objective_function, constraints, type="min", visual=False):
    check_args_valid(objective_function, constraints, type)

    # Get the (x, y) coords of all the intersections of the contraints as lines
    intersections = []
    for i, c1 in enumerate(constraints):
        for j in range(i + 1, len(constraints)):
            coords = c1.intersection_with(constraints[j])
            if coords:
                intersections.append(coords)

    # Filter all the coords that lie in the feasible region
    filter_helper = lambda coord: within_feasible_region(constraints, coord)
    intersections = list(filter(filter_helper, intersections))

    # Find the min/max value and coordinate (should also check if integer values are required (check ceil and floor))
    optimal_coord = ()
    if type == "min":
        optimal_val = np.Infinity
        for coord in intersections:
            val = objective_function.evaluate_at(coord[0], coord[1])
            if val < optimal_val:
                optimal_val = val
                optimal_coord = coord
    else:
        optimal_val = -np.Infinity
        for coord in intersections:
            val = objective_function.evaluate_at(coord[0], coord[1])
            if val > optimal_val:
                optimal_val = val
                optimal_coord = coord

    print(list(intersections))
    print("Optimal objective function: " + str(optimal_val))
    print("Optimal coordinate (x = {0}, y = {1})".format(optimal_coord[0], optimal_coord[1]))

    if visual:
        visualise(constraints)


def within_feasible_region(constraints, coord):
    for c in constraints:
        if not c.evaluate(coord[0], coord[1]):
            return False
    return True

def check_args_valid(objective_function, constraints, type):
    if not type in ("min", "max"):
        raise ValueError("Problem type should be 'min' for minimisation or 'max' for maximisation")

    if len(constraints) == 0:
        raise ValueError("Please provide a list of constraints")

    if not isinstance(objective_function, ObjectiveFunction):
        raise ValueError("Please provide a valid objective function")

 
def visualise(constraints):
    plt.rcParams['toolbar'] = 'None' # hide toolbar

    d = np.linspace(0, 16, 300, endpoint=False)
    x, y = np.meshgrid(d,d)

    # Plot the shaded region based on all of the constraints
    combine_constraints = constraints[0].evaluate(x, y)
    iterconstraints = iter(constraints)
    next(iterconstraints)
    for c in iterconstraints:
        combine_constraints &= c.evaluate(x, y)

    plt.imshow(combine_constraints.astype(int), 
                extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha=0.3)

    # Plot the lines defining the constraints
    x = np.linspace(0, x.max(), 2000)
    ys = [(c.as_line(x), c.to_latex_string()) for c in constraints]

    # Plot each line (maybe keep the label as well in ys variable)
    for y in ys:
        plt.plot(x, y[0], label=y[1])

    plt.xlim(0,16)
    plt.ylim(0,11)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()


def main():
    constraints = [
        Constraint(0, 1, 2, sign=">="), # y >= 2
        Constraint(1, 2, 25, sign="<="), # x + 2*y <= 25
        Constraint(-2, 4, -8, sign=">="), # -2*x + 4*y >= 8
        Constraint(-2, 1, -5, sign="<=") # -2*x + y >= -5
    ]

    objective_function = ObjectiveFunction(3, 2)
    optimise(objective_function, constraints, type="max", visual=True)

main()