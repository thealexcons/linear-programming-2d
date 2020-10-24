import matplotlib.pyplot as plt
import numpy as np
from objective_function import ObjectiveFunction
from constraint import Constraint
from math import ceil, floor

# Solves a 2D linear programming problem
def optimise(objective_function, constraints, type="min", visual=False, integer_only=False):
    check_args_valid(objective_function, constraints, type)

    # Get the (x, y) coords of all the intersections of the contraints as lines
    intersections = []
    for i, c1 in enumerate(constraints):
        for j in range(i + 1, len(constraints)):
            coords = c1.intersection_with(constraints[j])
            if coords:
                intersections.append(coords)

    # Filter all the coords that lie in the feasible region
    filter_feasible_points = lambda coord: within_feasible_region(constraints, coord)
    intersections = list(filter(filter_feasible_points, intersections))

    # Find the min/max value and coordinate 
    optimal_coord, optimal_val = get_optimal_solution(intersections, type, objective_function)

    # Check if optimal coordinate is non-integer and if integer_only mode is set, then test
    # all integer points around the original point
    if integer_only:
        if not (isinstance(optimal_coord[0], int) and isinstance(optimal_coord[1], int)): 
            optimal_coord, optimal_val = get_optimal_integer_solution(optimal_coord, type, objective_function, constraints)
            print("Results have been restricted to integer values:")  
    
    print("\tOptimal value: " + str(objective_function) + " = " + str(optimal_val))
    print("\tOptimal coordinate: (x = {0}, y = {1})".format(optimal_coord[0], optimal_coord[1]))

    if visual:
        visualise(constraints, optimal_coord)


# Get the optimal coordinate and value
def get_optimal_solution(coordinates, type, objective_function):
    optimal_coord = ()
    optimal_val = 0
    if type == "min":
        optimal_val = float('inf')
        for coord in coordinates:
            val = objective_function.evaluate_at(coord[0], coord[1])
            if val < optimal_val:
                optimal_val = val
                optimal_coord = coord
    else:
        optimal_val = - float('inf')
        for coord in coordinates:
            val = objective_function.evaluate_at(coord[0], coord[1])
            if val > optimal_val:
                optimal_val = val
                optimal_coord = coord
    
    return optimal_coord, optimal_val


# Checks the four integer points around the given coordinate and returns the optimal one
def get_optimal_integer_solution(coord, type, objective_function, constraints):
    integer_coords = [
        (ceil(coord[0]), ceil(coord[1])),
        (ceil(coord[0]), floor(coord[1])),
        (floor(coord[0]), ceil(coord[1])),
        (floor(coord[0]), floor(coord[1])),
    ]

    filter_feasible_points = lambda coord: within_feasible_region(constraints, coord)
    integer_coords = list(filter(filter_feasible_points, integer_coords))

    return get_optimal_solution(integer_coords, type, objective_function)


# Checks if a coordinate lies within the feasible region bounded by the constraints
def within_feasible_region(constraints, coord):
    for c in constraints:
        if not c.evaluate(coord[0], coord[1]):
            return False
    return True

# Helper function to check that the arguments are valid
def check_args_valid(objective_function, constraints, type):
    if not type in ("min", "max"):
        raise ValueError("Problem type should be 'min' for minimisation or 'max' for maximisation")

    if len(constraints) == 0:
        raise ValueError("Please provide a list of constraints")

    if not isinstance(objective_function, ObjectiveFunction):
        raise ValueError("Please provide a valid objective function")


# Show the graph in a plot
def visualise(constraints, optimal_coord):
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

    # Plot the optimal intersection 
    plt.plot(optimal_coord[0], optimal_coord[1], 'ro')
    # plt.annotate(str(optimal_coord), optimal_coord)

    plt.xlim(0,16)
    plt.ylim(0,11)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.show()
