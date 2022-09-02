from .calc_parts.calc_part_013 import calc_part as cp13
from .calc_parts.calc_part_013 import add_variables as av13
from .calc_parts.calc_part_014 import calc_part as cp14
from .calc_parts.calc_part_014 import add_variables as av14
from .calc_parts.calc_part_015 import calc_part as cp15
from .calc_parts.calc_part_015 import add_variables as av15


def calc(f, is_init_vars, calc_name, nv):
    if is_init_vars is False:
        av13(f)
    cp13(f, False)
    if is_init_vars is False:
        av14(f)
    cp14(f, False)
    if is_init_vars is False:
        av15(f)
    cp15(f, False)
    if is_init_vars is False:
        is_init_vars = True
    return is_init_vars
