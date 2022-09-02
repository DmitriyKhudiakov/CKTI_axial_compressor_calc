import glob
from app.calc.classes.field import Field
import app.calc.scripts.formula as formula
import app.calc.axial_compressor.add_vars as av


def init_calc(calc_name):
    f = Field(calc_name)
    add = av
    add.add_variables(f)
    for curr_name in f.tex_name:
        tn = f.tex_name[curr_name]
        image_name = f.variable_dict[curr_name].image_name
        path = "app\\calc\\" + calc_name + "\\source\\display_images\\" + str(image_name)
        is_exist = False
        if len(glob.glob(path + ".png")) > 0:
            is_exist = True
        if is_exist is False:
            formula.create_formula(formula="$" + str(tn) + "$", font_size=14, path=path)
    return f
