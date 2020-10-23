import matplotlib.pyplot as plt
import numpy as np
from objective_function import ObjectiveFunction
from constraint import Constraint

# Solves a linear programming problem
def optimise(objective_function, constraints, type="min", visual=False):
    check_args_valid(objective_function, constraints, type)

    if visual:
        visualise(constraints)

    # get the (x, y) coords of all the intersections of the contraints as lines
    # evalute the objective function at each coord and keep the minimum

def check_args_valid(objective_function, constraints, type):
    if not type in ("min", "max"):
        raise ValueError("Optimisation type should be 'min' for minimisation or 'max' for maximisation")

    if len(constraints) == 0:
        raise ValueError("Please provide a list of constraints")

    if not isinstance(objective_function, ObjectiveFunction):
        raise ValueError("Please provide a valid objective function")

 
def visualise(constraints):
    # c1 = Constraint(0, 1, 2, sign=">=") # y >= 2
    # c2 = Constraint(1, 2, 25, sign="<=") # x + 2*y <= 25
    # c3 = Constraint(-2, 4, -8, sign=">=") # -2*x + 4*y >= 8
    # c4 = Constraint(-2, 1, -5, sign="<=") # -2*x + y >= -5

    d = np.linspace(-2,16,300)
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
    x = np.linspace(0, 16, 2000)
    ys = [(c.as_line(x), c.to_latex_string()) for c in constraints]

    # # y >= 2
    # y1 = c1.as_line(x)
    # # 2y <= 25 - x
    # y2 = c2.as_line(x)
    # # 4y >= 2x - 8 
    # y3 = c3.as_line(x)
    # # y <= 2x - 5 
    # y4 = c4.as_line(x)

    # Plot each line (maybe keep the label as well in ys variable)
    for y in ys:
        plt.plot(x, y[0], label=y[1])
    # plt.plot(x, y1, label=c1.to_latex_string())
    # plt.plot(x, y2, label=r'$2y\leq25-x$')
    # plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
    # plt.plot(x, y4, label=r'$y\leq 2x-5$')
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
    optimise(objective_function, constraints, type="min", visual=True)

main()