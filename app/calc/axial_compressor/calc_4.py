from .calc_parts.calc_part_016 import calc_part as cp16
from .calc_parts.calc_part_016 import add_variables as av16
from .calc_parts.calc_part_017 import calc_part as cp17
from .calc_parts.calc_part_017 import add_variables as av17
from .calc_parts.calc_part_018 import calc_part as cp18
from .calc_parts.calc_part_018 import add_variables as av18
from .calc_parts.calc_part_019 import calc_part as cp19
from .calc_parts.calc_part_019 import add_variables as av19


def calc(f, is_init_vars, calc_name, type_calc):
    if type_calc == 1:
        if is_init_vars is False:
            av16(f)
        cp16(f, False)
    elif type_calc == 2:
        if is_init_vars is False:
            av16(f)
        cp16(f, False)
        if is_init_vars is False:
            av17(f)
        cp17(f, False)
    elif type_calc == 3:
        if is_init_vars is False:
            av16(f)
        cp16(f, False)
        if is_init_vars is False:
            av17(f)
        cp17(f, False)
        if is_init_vars is False:
            av18(f)
        cp18(f, False)
    elif type_calc == 4:
        if is_init_vars is False:
            av16(f)
        cp16(f, False)
        if is_init_vars is False:
            av17(f)
        cp17(f, False)
        if is_init_vars is False:
            av18(f)
        cp18(f, False)
        if is_init_vars is False:
            av19(f)
        cp19(f, False)
    if is_init_vars is False:
        is_init_vars = True
    return is_init_vars
