import math
from . import graph_save_data as gs


def add_variables(f):
    for i in range(1, f.v["i_int"] + 1):
        f.add_variable("D_р" + s(i), 1.0, "", "D_{р" + str(i) + "}")
        f.add_variable("b" + s(i), 1.0, "", "b_{" + str(i) + "}")
        f.add_variable("bD_р" + s(i), 1.0, "", "b")
        f.add_variable("Sr" + s(i), 1.0, "", "")
        f.add_variable("Sr_rel" + s(i), 1.0, "", "")
        f.add_variable("k_psi_зl" + s(i), 1.0, "", "")
        f.add_variable("k_eta_зl" + s(i), 1.0, "", "")
        f.add_variable("k_psi_м" + s(i), 1.0, "", "")
        f.add_variable("k_eta_м" + s(i), 1.0, "", "")
        f.add_variable("k_psi_z" + s(i), 1.0, "", "")
        f.add_variable("k_eta_z" + s(i), 1.0, "", "")
        f.add_variable("drн_rel" + s(i), 1.0, "", "")
        f.add_variable("drвт_rel" + s(i), 1.0, "", "")
        f.add_variable("k_eta_dr_вт" + s(i), 1.0, "", "")
        f.add_variable("k_eta_dr_н" + s(i), 1.0, "", "")
        f.add_variable("k_eta_dr" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr_вт" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr_н" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr" + s(i), 1.0, "", "")
        f.add_variable("k_eta" + s(i), 1.0, "", "")
        f.add_variable("k_psi'" + s(i), 1.0, "", "")


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def s(to_string):
    return str(to_string)


def print_calc_st_res_1(f, n_st):
    n_sym = 3
    curr_str = ""
    if n_st < 10:
        curr_str += "| " + s(n_st)
    else:
        curr_str += "|" + s(n_st)
    curr_str += "| " + to_fixed(f.v["D_р" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["b" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["bD_р" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["l_" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["l_rel" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["Sr" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["Sr_rel" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["k_psi_зl" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["k_eta_зl" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["k_psi_z" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["k_eta_z" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["k_psi_м" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["k_eta_м" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_н" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["drн_rel" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_вт" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["drвт_rel" + s(n_st)], n_sym)
    curr_str += "|      " + to_fixed(f.v["k_eta_dr_вт" + s(n_st)], n_sym)
    curr_str += "|     " + to_fixed(f.v["k_eta_dr_н" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["k_eta_dr" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["k_eta" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["k_psi'" + s(n_st)], n_sym)
    curr_str += "|"
    print(curr_str)


def print_start_str():
    print("*********************************")
    print("calculation of coefficients - k_psi and k_eta (014):")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|Dр    "
    curr_str += "|b     "
    curr_str += "|bDр   "
    curr_str += "|l_    "
    curr_str += "|l_rel "
    curr_str += "|Sr    "
    curr_str += "|Sr_rel"
    curr_str += "|k_psi_зl"
    curr_str += "|k_eta_зl"
    curr_str += "|k_psi_z"
    curr_str += "|k_eta_z"
    curr_str += "|k_psi_м"
    curr_str += "|k_eta_м"
    curr_str += "|D_н   "
    curr_str += "|drн_rel"
    curr_str += "|D_вт  "
    curr_str += "|drвт_rel"
    curr_str += "|k_eta_dr_вт"
    curr_str += "|k_eta_dr_н"
    curr_str += "|k_eta_dr"
    curr_str += "|k_eta "
    curr_str += "|k_psi'"
    curr_str += "|"
    print(curr_str)


def print_end_str():
    print("*********************************\n")


def coefficients_func_2(f, i):
    # k_psi_зl, k_eta_зl
    h_psi_2 = 1.0
    h_eta_2 = 1.0
    if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
        h_psi_2 = 0.990
        h_eta_2 = 0.989
    elif f.v["тип ступени"] == 3:
        h_psi_2 = 0.987
        h_eta_2 = 0.985
    elif f.v["тип ступени"] == 4:
        h_psi_2 = 0.988
        h_eta_2 = 0.982
    h_psi_1 = 1.0 - 0.045 * math.sqrt(f.v["OmegaТ"]) * f.v["Sr_rel" + s(i)] / f.v["l_rel" + s(i)]
    h_eta_1 = 1.0 - 0.024 * math.sqrt(f.v["OmegaТ"]) * f.v["Sr_rel"+s(i)] / (1.0 - f.v["l_"+s(i)] / f.v["D_р"+s(i)])
    f.v["k_psi_зl" + s(i)] = h_psi_1 / h_psi_2
    f.v["k_eta_зl" + s(i)] = h_eta_1 / h_eta_2


def coefficients_func_4(f, i):
    # k_psi_dr, k_eta_dr
    if f.v["dr_вт"] == 0.0:
        f.v["k_eta_dr_вт" + s(i)] = 1.0
    else:
        f.v["k_eta_dr_вт" + s(i)] = gs.rk_eta_plus_get_k_14(f, f.v["drвт_rel" + s(i)])
    if f.v["dr_н"] == 0.0:
        f.v["k_eta_dr_н" + s(i)] = 1.0
    else:
        f.v["k_eta_dr_н" + s(i)] = gs.rk_eta_minus_get_k_14(f, f.v["drн_rel" + s(i)])
    f.v["k_eta_dr" + s(i)] = f.v["k_eta_dr_вт" + s(i)] * f.v["k_eta_dr_н" + s(i)]


def calc_part(f, is_print_res):
    for i in range(1, f.v["i_int"] + 1):
        f.v["D_р" + s(i)] = f.v["Dн1"]
        f.v["b" + s(i)] = f.v["b_aver"]
        f.v["bD_р" + s(i)] = f.v["b" + s(i)] / f.v["D_р" + s(i)]
        f.v["Sr" + s(i)] = f.v["Sr_aver_rel"] * f.v["b" + s(i)] * 2.0 * 1000.0
        f.v["Sr_rel" + s(i)] = 100.0 * f.v["Sr" + s(i)] / (f.v["l_" + s(i)] * 1000.0)
        coefficients_func_2(f, i)
        f.v["k_psi_м" + s(i)] = f.v["k_psi_м"]
        f.v["k_eta_м" + s(i)] = f.v["k_eta_м"]
        f.v["k_psi_z" + s(i)] = f.v["k_psi_z"]
        f.v["k_eta_z" + s(i)] = f.v["k_eta_z"]
        if f.v["тип проточной части"] == 1:
            f.v["drн_rel" + s(i)] = f.v["D_н" + s(i)] / f.v["D_р" + s(i)] - 1.0
            f.v["drвт_rel" + s(i)] = f.v["dr_вт"]
        elif f.v["тип проточной части"] == 2:
            f.v["drн_rel" + s(i)] = f.v["D_н" + s(i)] / f.v["D_р" + s(i)] - 1.0
            f.v["drвт_rel" + s(i)] = f.v["dr_вт"]
        coefficients_func_4(f, i)
        f.v["k_eta" + s(i)] = f.v["k_eta_dr"+s(i)] * f.v["k_eta_z"+s(i)] * f.v["k_eta_м"+s(i)] * f.v["k_eta_зl"+s(i)]
        f.v["k_psi'" + s(i)] = f.v["k_psi_z" + s(i)] * f.v["k_psi_м" + s(i)] * f.v["k_psi_зl" + s(i)]
        if is_print_res is True:
            print_calc_st_res_1(f, i)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_start_str()
    calc_part(field, is_print_res)
    if is_print_res:
        print_end_str()
