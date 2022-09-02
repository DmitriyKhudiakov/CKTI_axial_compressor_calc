

class PointsGraph:
    def __init__(self, val):
        self.list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.list_y = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        for i in self.list_y:
            self.list_y[self.list_y.index(i)] = i * val
        self.color = "#cc317e"
        self.name = "график1"
        self.add_arrow = True
        self.type_gr = "points"


class FuncGraph:
    def __init__(self, func_x, func_y, f, color, name):
        self.var_x = func_x(f)
        self.var_y = func_y(f)
        self.color = color
        self.name = name
        self.add_arrow = True
        self.type_gr = "func"


def get_dict(f, calc_name):
    elem_dict = {'html': "display_4.html"}
    return elem_dict
