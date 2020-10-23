class ObjectiveFunction:

    def __init__(self, x_coefficient, y_coefficient):
        self.x_coefficient = x_coefficient
        self.y_coefficient = y_coefficient

    def evaluate_at(self, x_val, y_val):
        return self.x_coefficient * x_val + self.y_coefficient * y_val

    def __str__(self):
        y_sign = "+"
        y_str = str(self.y_coefficient)
        if self.y_coefficient < 0:
            y_sign = "-"
            y_str = y_str[1:]

        return "P(x, y) = {0}x {1} {2}y".format(self.x_coefficient, y_sign, y_str)
