import math
from .graph_data import GraphData
from . import graph_save_data as gs


def add_variables(f):
    for i in range(1, f.v["i_int"] + 1):
        f.add_variable("F_" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr_вт" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr_н" + s(i), 1.0, "", "")
        f.add_variable("k_psi_dr" + s(i), 1.0, "", "")


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def s(to_string):
    return str(to_string)


def print_calc_st_res(f, n_st):
    n_sym = 3
    curr_str = ""
    if n_st < 10:
        curr_str += "| " + s(n_st)
    else:
        curr_str += "|" + s(n_st)
    if f.v["p*" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["p*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["p*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["T*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["rho*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["F_" + s(n_st)], n_sym)
    if f.v["cz*" + s(n_st)] < 100.0:
        curr_str += "|  " + to_fixed(f.v["cz*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["cz*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["phi*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["uр'" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["psi" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["eta" + s(n_st)], n_sym)
    curr_str += "|      " + to_fixed(f.v["k_psi_dr_вт" + s(n_st)], n_sym)
    curr_str += "|     " + to_fixed(f.v["k_psi_dr_н" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["k_psi_dr" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["k_psi'" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["k_psi" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["k_eta" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["psi_р" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["eta_р" + s(n_st)], n_sym)
    if f.v["H*" + s(n_st)] < 10000.0:
        curr_str += "|  " + to_fixed(f.v["H*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["H*" + s(n_st)], n_sym)
    if f.v["dTад*" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["dTад*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["dTад*" + s(n_st)], n_sym)
    if f.v["dT*" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["dT*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["dT*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["П*" + s(n_st)], n_sym)
    if f.v["p_з*" + s(n_st)] > 100000.0:
        curr_str += "| " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
    else:
        curr_str += "|  " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["T_з*" + s(n_st)], n_sym)
    print(curr_str)


def print_start_str():
    print("*********************************")
    print("second step calculation (015):")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|p*         "
    curr_str += "|T*      "
    curr_str += "|rho*  "
    curr_str += "|F     "
    curr_str += "|cz*     "
    curr_str += "|phi*   "
    curr_str += "|uр'     "
    curr_str += "|psi   "
    curr_str += "|eta  "
    curr_str += "|k_psi_dr_вт"
    curr_str += "|k_psi_dr_н"
    curr_str += "|k_psi_dr"
    curr_str += "|k_psi'"
    curr_str += "|k_psi "
    curr_str += "|k_eta "
    curr_str += "|psi_р "
    curr_str += "|eta_р "
    curr_str += "|H*        "
    curr_str += "|dTад*  "
    curr_str += "|dT*    "
    curr_str += "|П*    "
    curr_str += "|p_з*       "
    curr_str += "|T_з*    "
    print(curr_str)


def print_end_str(f):
    print("         П_ЛА* = ", f.v["П_ЛА*"])
    print("         H_ЛА* = ", f.v["H_ЛА*"])
    print("         dTад_ЛА* = ", f.v["dTад_ЛА*"])
    print("         dT_ЛА* = ", f.v["dT_ЛА*"])
    print("         eta_ЛА = ", f.v["eta_ЛА"])
    print("         N_ЛА = ", f.v["N_ЛА"])
    print("*********************************\n")


def coefficients_func_4(f, i):
    # k_psi_dr, k_eta_dr
    if f.v["dr_вт"] == 0.0:
        f.v["k_psi_dr_вт" + s(i)] = 1.0
    else:
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["k_psi_dr_вт" + s(i)] = gs.k_psi_dr_plus_50_get_k_15(f, f.v["drвт_rel" + s(i)], f.v["phi*" + s(i)])
        elif f.v["тип ступени"] == 3:
            f.v["k_psi_dr_вт" + s(i)] = gs.k_psi_dr_plus_70_get_k_15(f, f.v["drвт_rel" + s(i)], f.v["phi*" + s(i)])
        elif f.v["тип ступени"] == 4:
            f.v["k_psi_dr_вт" + s(i)] = gs.k_psi_dr_plus_100_get_k_15(f, f.v["drвт_rel" + s(i)], f.v["phi*" + s(i)])
    if f.v["dr_н"] == 0.0:
        f.v["k_psi_dr_н + s(i)" + s(i)] = 1.0
    else:
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["k_psi_dr_н" + s(i)] = gs.k_psi_dr_minus_50_get_k_15(f, f.v["drн_rel" + s(i)], f.v["phi*" + s(i)])
        elif f.v["тип ступени"] == 3:
            f.v["k_psi_dr_н" + s(i)] = gs.k_psi_dr_minus_70_get_k_15(f, f.v["drн_rel" + s(i)], f.v["phi*" + s(i)])
        elif f.v["тип ступени"] == 4:
            f.v["k_psi_dr_н" + s(i)] = gs.k_psi_dr_minus_100_get_k_15(f, f.v["drн_rel" + s(i)], f.v["phi*" + s(i)])
    f.v["k_psi_dr" + s(i)] = f.v["k_psi_dr_вт" + s(i)] * f.v["k_psi_dr_н" + s(i)]


def calc_part(f, is_print_res):
    for i in range(1, f.v["i_int"] + 1):
        if i == 1:
            f.v["p*" + s(i)] = f.v["p1*"]
            f.v["T*" + s(i)] = f.v["TВ*"]
        else:
            f.v["p*" + s(i)] = f.v["p_з*" + s(i - 1)]
            f.v["T*" + s(i)] = f.v["T_з*" + s(i - 1)]
        f.v["rho*" + s(i)] = f.v["p*" + s(i)] / (f.v["R"] * f.v["T*" + s(i)])
        f.v["F_" + s(i)] = f.v["pi"] * (pow(f.v["D_н" + s(i)], 2.0) - pow(f.v["D_вт" + s(i)], 2.0)) / 4.0
        f.v["cz*" + s(i)] = f.v["m"] / (f.v["rho*" + s(i)] * f.v["F_" + s(i)])
        f.v["phi*" + s(i)] = f.v["cz*" + s(i)] / f.v["uр" + s(i)]
        if f.v["тип ступени"] == 3:
            f.v["uр'" + s(i)] = f.v["uр" + s(i)] * math.sqrt(298.0 / f.v["T*" + s(i)])
        else:
            f.v["uр'" + s(i)] = f.v["uр" + s(i)] * math.sqrt(295.0 / f.v["T*" + s(i)])
        if f.v["тип ступени"] == 1:
            f_list = gs.st_k_50_1_eta(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["eta" + s(i)] = f_point[1]
            f_list = gs.st_k_50_1_psi(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["psi" + s(i)] = f_point[1]
        elif f.v["тип ступени"] == 2:
            f_list = gs.st_k_50_5_eta(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["eta" + s(i)] = f_point[1]
            f_list = gs.st_k_50_5_psi(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["psi" + s(i)] = f_point[1]
        elif f.v["тип ступени"] == 3:
            f_list = gs.st_k_70_17_eta(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["eta" + s(i)] = f_point[1]
            f_list = gs.st_k_70_17_psi(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["psi" + s(i)] = f_point[1]
        elif f.v["тип ступени"] == 4:
            f_list = gs.st_k_100_2l_eta(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["eta" + s(i)] = f_point[1]
            f_list = gs.st_k_100_2l_psi(f.v["uр'" + s(i)])
            f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi*" + s(i)])
            f.v["psi" + s(i)] = f_point[1]
        coefficients_func_4(f, i)
        f.v["k_psi" + s(i)] = f.v["k_psi_dr" + s(i)] * f.v["k_psi'" + s(i)]
        f.v["psi_р" + s(i)] = f.v["psi" + s(i)] * f.v["k_psi" + s(i)]
        f.v["eta_р" + s(i)] = f.v["eta" + s(i)] * f.v["k_eta" + s(i)]
        h_1 = pow(f.v["uр" + s(i)], 2.0) / 2.0
        f.v["H*" + s(i)] = f.v["psi_р" + s(i)] * h_1
        f.v["dTад*" + s(i)] = f.v["H*" + s(i)] / ((f.v["k"] / (f.v["k"] - 1.0)) * f.v["R"])
        f.v["dT*" + s(i)] = f.v["dTад*" + s(i)] / f.v["eta_р" + s(i)]
        h_2 = f.v["k"] / (f.v["k"] - 1.0)
        f.v["П*" + s(i)] = pow(1.0 + f.v["H*" + s(i)] / (h_2 * f.v["R"] * f.v["T*" + s(i)]), h_2)
        f.v["p_з*" + s(i)] = f.v["p*" + s(i)] * f.v["П*" + s(i)]
        f.v["T_з*" + s(i)] = f.v["T*" + s(i)] + f.v["dT*" + s(i)]
        if is_print_res is True:
            print_calc_st_res(f, i)
    f.v["П_ЛА*"] = f.v["p_з*" + s(f.v["i_int"])] / f.v["p*" + s(1)]
    h_1 = f.v["k"] / (f.v["k"] - 1.0)
    f.v["H_ЛА*"] = h_1 * f.v["R"] * f.v["T*" + s(1)] * (pow(f.v["П_ЛА*"], 1.0 / h_1) - 1.0)
    f.v["dTад_ЛА*"] = f.v["H_ЛА*"] / (h_1 * f.v["R"])
    f.v["dT_ЛА*"] = f.v["T_з*" + s(f.v["i_int"])] - f.v["T*" + s(1)]
    f.v["eta_ЛА"] = f.v["dTад_ЛА*"] / f.v["dT_ЛА*"]
    f.v["N_ЛА"] = f.v["m"] * f.v["H_ЛА*"] / (1000.0 * f.v["eta_ЛА"])


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_start_str()
    calc_part(field, is_print_res)
    if is_print_res:
        print_end_str(field)
