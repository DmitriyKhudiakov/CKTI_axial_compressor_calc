import app.calc.axial_compressor.set_param as sp


def run(calc_name, setup_list, enter_list, var_setup_list, var_enter_list,  f):
    set_param = sp
    ret_list, is_ok = set_param.set_vars(f, setup_list, enter_list)
    var_ret_list, var_is_ok = set_param.set_var_vars(f, var_setup_list, var_enter_list)
    if (is_ok is False) or (var_is_ok is False):
        return False, ret_list, var_ret_list, f
    else:
        return True, ret_list, var_ret_list, f
