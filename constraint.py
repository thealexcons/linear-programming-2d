
constraint_relations = ("<", "<=", "=", ">", ">=")
latex_symbols = ("\l", "\leq", "\eq", "\g", "\geq")

class Constraint:

    '''
        Format passed in: x_coeffcient * x + y_coefficient * y sign constant
            eg: Constraint(3, 4, 5, sign='<')   ->  3*x + 4*y < 5
            eg: Constraint(-3, 5, 0, sign='>=')   ->  -3*x + 5*y >= 0
    '''
    def __init__(self, x_coefficient, y_coefficient, constant, sign="<"):
        self.x_coefficient = x_coefficient
        self.y_coefficient = y_coefficient
        self.constant = constant

        if sign not in constraint_relations:
            raise ValueError("Sign should be one of " + str(constraint_relations))
        self.sign = sign

    # Used to plot the constraint region
    def evaluate(self, x_var, y_var):
        if self.sign == constraint_relations[0]:
            return self.y_coefficient * y_var < - self.x_coefficient * x_var + self.constant
        elif self.sign == constraint_relations[1]:
            return self.y_coefficient * y_var <= - self.x_coefficient * x_var + self.constant
        elif self.sign == constraint_relations[2]:
            return self.y_coefficient * y_var == - self.x_coefficient * x_var + self.constant
        elif self.sign == constraint_relations[3]:
            return self.y_coefficient * y_var > - self.x_coefficient * x_var + self.constant
        elif self.sign == constraint_relations[4]:
            return self.y_coefficient * y_var >= - self.x_coefficient * x_var + self.constant

    # Returns the constraint as a linear function given the x_var values
    def as_line(self, x_var):
        return (-self.x_coefficient * x_var + self.constant) / float(self.y_coefficient)

    # Latex string representation of the constraint
    def to_latex_string(self):
        x_str = ""
        if self.x_coefficient == 1:
            x_str = "x"
        elif self.x_coefficient != 0:
            x_str = str(self.x_coefficient) + "x"

        y_str = ""
        if self.y_coefficient == 1:
            y_str = "y"
        elif self.y_coefficient != 0:
            y_str = str(self.y_coefficient) + "y"

        if self.y_coefficient > 0:
            if self.x_coefficient != 0:
                y_str = "+ " + y_str

        sign = latex_symbols[constraint_relations.index(self.sign)]
        return r"${0} {1} {2} {3}$".format(x_str, y_str, sign, self.constant)
