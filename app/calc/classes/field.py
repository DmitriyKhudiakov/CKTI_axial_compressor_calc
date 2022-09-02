import random as rnd
from app.calc.classes.variable import Variable


class Field:
    def __init__(self, calc_name):
        self.variable_dict = {}
        self.v = {}
        self.d = {}
        self.id_num = {}
        self.tex_name = {}
        self.calc_name = calc_name

    @staticmethod
    def gen_variable_id_num(variable_dict):
        while True:
            is_unique = True
            id_num = rnd.randint(0, 99999999)
            for curr_variable in variable_dict.items():
                if id_num == curr_variable[1].id_num:
                    is_unique = False
            if is_unique is True:
                break
        return id_num

    def add_variable(self, name, value, dim, tex_name):
        var = Variable(name, value, self.gen_variable_id_num(self.variable_dict), dim, tex_name)
        self.variable_dict.update({var.name: var})
        self.v.update({var.name: var.value})
        self.d.update({var.name: var.dim})
        self.id_num.update({var.name: var.id_num})
        self.tex_name.update({var.name: var.tex_name})
        with open("app\\calc\\" + self.calc_name + "\\id.csv", "a") as file:
            file.write(str(var.id_num) + ",")

    def delete_data(self):
        full_path = "app\\calc\\" + self.calc_name + "\\id.csv"
        file = open(full_path)
        text = file.read()
        for curr_id_num in self.id_num:
            text = text.replace(str(self.id_num[curr_id_num]) + ",", "")
        file.close()
        file = open(full_path, "w")
        file.write(text)
        file.close()
