class Variable:
    def __init__(self, name, value, id, latex_name):
        self.name = name
        self.id = id
        if value is None:
            self.value = None
        else:
            self.value = float(value)
        self.latex_name = latex_name
