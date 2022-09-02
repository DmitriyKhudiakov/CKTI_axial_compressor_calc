from .calc_parts.calc_part_002 import calc_part as cp2
from .calc_parts.calc_part_002 import add_variables as av2
from .calc_parts.calc_part_003 import calc_part as cp3
from .calc_parts.calc_part_003 import add_variables as av3
from .calc_parts.calc_part_004 import calc_part as cp4
from .calc_parts.calc_part_004 import add_variables as av4
from .calc_parts.calc_part_005 import calc_part as cp5
from .calc_parts.calc_part_005 import add_variables as av5
from .calc_parts.calc_part_006 import calc_part as cp6
from .calc_parts.calc_part_006 import add_variables as av6
from .calc_parts.calc_part_007 import calc_part as cp7
from .calc_parts.calc_part_007 import add_variables as av7
from .calc_parts.calc_part_008 import calc_part as cp8
from .calc_parts.calc_part_008 import add_variables as av8
from .calc_parts.calc_part_009 import calc_part as cp9
from .calc_parts.calc_part_009 import add_variables as av9
from .calc_parts.calc_part_010 import calc_part as cp10
from .calc_parts.calc_part_010 import add_variables as av10
import glob
import app.calc.scripts.formula as formula


def calc(f, is_init_vars, calc_name):
    if is_init_vars is False:
        av2(f)
    cp2(f)

    if is_init_vars is False:
        av3(f)
    cp3(f)
    if is_init_vars is False:
        av4(f)
    cp4(f)
    if is_init_vars is False:
        av5(f)
    cp5(f)
    if is_init_vars is False:
        av6(f)
    cp6(f)
    if is_init_vars is False:
        av7(f)
    cp7(f)
    if is_init_vars is False:
        av8(f)
    cp8(f)
    if is_init_vars is False:
        av9(f)
    cp9(f)
    if is_init_vars is False:
        for curr_name in f.tex_name:
            tn = f.tex_name[curr_name]
            image_name = f.variable_dict[curr_name].image_name
            path = "app\\calc\\" + calc_name + "\\source\\display_images\\" + str(image_name)
            is_exist = False
            if len(glob.glob(path + ".png")) > 0:
                is_exist = True
            if is_exist is False:
                formula.create_formula(formula="$" + str(tn) + "$", font_size=14, path=path)
    if is_init_vars is False:
        av10(f)
    cp10(f, False)
    if is_init_vars is False:
        is_init_vars = True
    return is_init_vars
