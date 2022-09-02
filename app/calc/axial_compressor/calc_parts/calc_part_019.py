import math
from . import graph_save_data as gs


def add_variables(f):
    f.add_variable("cz*" + s(f.v["i_int"] + 1), 1.0, "", "")
    for i in range(1, f.v["i_int"] + 2):
        f.add_variable("pt2F_" + s(i), 1.0, "", "")
        f.add_variable("pt2D_ср" + s(i), 1.0, "", "")
        f.add_variable("pt2r_ср_rel" + s(i), 1.0, "", "")
        f.add_variable("pt2alpha_1z" + s(i), 0.0, "", "")
        f.add_variable("pt2alpha_2z" + s(i), 0.0, "", "")
        f.add_variable("pt2alpha_3z" + s(i), 0.0, "", "")
        f.add_variable("pt2cos_alpha_3z" + s(i), 0.0, "", "")
        f.add_variable("pt2p" + s(i), 0.0, "", "")
        f.add_variable("pt2T" + s(i), 0.0, "", "")
        f.add_variable("pt2rho" + s(i), 0.0, "", "")
        f.add_variable("pt2c2*" + s(i), 1.0, "", "")
        f.add_variable("pt2cz" + s(i), 1.0, "", "")
        f.add_variable("pt2c1" + s(i), 1.0, "", "")
        f.add_variable("pt2p_res" + s(i), 0.0, "", "")
        f.add_variable("pt2T_res" + s(i), 0.0, "", "")


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
    if f.v["p_з*" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["T_з*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_вт" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_нз" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt2F_" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt2D_ср" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_р" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["pt2r_ср_rel" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["pt2alpha_2z" + s(n_st)], n_sym)
    curr_str += "|       " + to_fixed(f.v["pt2cos_alpha_2z" + s(n_st)], n_sym)
    if f.v["cz*" + s(n_st)] < 100.0:
        curr_str += "|  " + to_fixed(f.v["cz*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["cz*" + s(n_st)], n_sym)
    if f.v["pt2c2*" + s(n_st)] < 100.0:
        curr_str += "|  " + to_fixed(f.v["pt2c2*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt2c2*" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt2T" + s(n_st)], n_sym)
    if f.v["pt2p" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["pt2p" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt2p" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt2rho" + s(n_st)], n_sym)
    if f.v["pt2cz" + s(n_st)] < 100000.0:
        curr_str += "| " + to_fixed(f.v["pt2cz" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt2cz" + s(n_st)], n_sym)
    if f.v["pt2c2" + s(n_st)] < 100.0:
        curr_str += "|  " + to_fixed(f.v["pt2c2" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt2c2" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt2T_res" + s(n_st)], n_sym)
    if f.v["pt2p" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["pt2p_res" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt2p_res" + s(n_st)], n_sym)
    print(curr_str)


def print_start_str():
    print("*********************************")
    print("calculation of static pressures and temperatures behind the impeller (second method) (019):")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|p*         "
    curr_str += "|T*      "
    curr_str += "|D_вт  "
    curr_str += "|D_нз  "
    curr_str += "|F_    "
    curr_str += "|D_ср  "
    curr_str += "|D_р   "
    curr_str += "|r_ср_rel"
    curr_str += "|alpha_2z"
    curr_str += "|cos_alpha_2z"
    curr_str += "|cz*     "
    curr_str += "|c2*     "
    curr_str += "|T       "
    curr_str += "|p          "
    curr_str += "|rho   "
    curr_str += "|cz      "
    curr_str += "|c2      "
    curr_str += "|T      "
    curr_str += "|p          "
    print(curr_str)


def print_end_str(f):
    print("*********************************\n")


def deg_to_rad(x):
    return


def calc_part(f, is_print_res):
    for i in range(1, f.v["i_int"] + 1):
        f.v["pt2F_" + s(i)] = f.v["pi"] * (math.pow(f.v["D_нз" + s(i)], 2.0) - math.pow(f.v["D_вт" + s(i)], 2.0)) / 4.0
        if i == f.v["i_int"] + 1:
            f.v["pt2D_ср" + s(i)] = (f.v["D_вт" + s(i - 1)] + f.v["D_нз" + s(i - 1)]) / 2.0
            f.v["pt2r_ср_rel" + s(i)] = f.v["pt2D_ср" + s(i - 1)] / f.v["D_р" + s(i - 1)]
        else:
            f.v["pt2D_ср" + s(i)] = (f.v["D_вт" + s(i)] + f.v["D_нз" + s(i)]) / 2.0
            f.v["pt2r_ср_rel" + s(i)] = f.v["pt2D_ср" + s(i)] / f.v["D_р" + s(i)]
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["pt2alpha_1z" + s(i)] = gs.k_50_1_alpha_1_get(f, f.v["pt2r_ср_rel" + s(i)])
            if i == f.v["i_int"] + 1:
                f.v["pt2alpha_2z" + s(i)] = gs.k_50_1_alpha_2_get(f, f.v["phi*" + s(i - 1)], f.v["pt2r_ср_rel" + s(i)])
            else:
                f.v["pt2alpha_2z" + s(i)] = gs.k_50_1_alpha_2_get(f, f.v["phi*" + s(i)], f.v["pt2r_ср_rel" + s(i)])
            f.v["pt2alpha_3z" + s(i)] = gs.k_50_1_alpha_1_get(f, f.v["pt2r_ср_rel" + s(i)])
        elif f.v["тип ступени"] == 3:
            f.v["pt2alpha_1z" + s(i)] = gs.k_70_17_alpha_1_get(f, f.v["pt2r_ср_rel" + s(i)])
            if i == f.v["i_int"] + 1:
                f.v["pt2alpha_2z" + s(i)] = gs.k_70_17_alpha_2_get(f, f.v["phi*" + s(i - 1)], f.v["pt2r_ср_rel" + s(i)])
            else:
                f.v["pt2alpha_2z" + s(i)] = gs.k_70_17_alpha_2_get(f, f.v["phi*" + s(i)], f.v["pt2r_ср_rel" + s(i)])
            f.v["pt2alpha_3z" + s(i)] = gs.k_70_17_alpha_3_get(f, f.v["pt2r_ср_rel" + s(i)])
        elif f.v["тип ступени"] == 4:
            f.v["pt2alpha_1z" + s(i)] = gs.k_100_2l_alpha_1_get(f, f.v["pt2r_ср_rel" + s(i)])
            f.v["pt2alpha_2z" + s(i)] = 0.0
            f.v["pt2alpha_3z" + s(i)] = gs.k_100_2l_alpha_3_get(f, f.v["pt2r_ср_rel" + s(i)])
        f.v["pt2cos_alpha_2z" + s(i)] = math.cos(math.radians(f.v["pt2alpha_2z" + s(i)]))
        f.v["pt2c2*" + s(i)] = f.v["cz*" + s(i)] / f.v["pt2cos_alpha_2z" + s(i)]
        f.v["pt2T" + s(i)] = f.v["T_з*" + s(i)] - math.pow(f.v["pt2c2*" + s(i)], 2.0) / (2.0 * 1005.0)
        h1 = f.v["k"] / (f.v["k"] - 1.0)
        f.v["pt2p" + s(i)] = f.v["p_з*" + s(i)] * math.pow(f.v["pt2T" + s(i)] / f.v["T_з*" + s(i)], h1)
        f.v["pt2rho" + s(i)] = f.v["pt2p" + s(i)] / (f.v["R"] * f.v["pt2T" + s(i)])
        f.v["pt2cz" + s(i)] = f.v["m"] / (f.v["pt2rho" + s(i)] * f.v["pt2F_" + s(i)])
        f.v["pt2c2" + s(i)] = f.v["pt2cz" + s(i)] / f.v["pt2cos_alpha_2z" + s(i)]
        f.v["pt2T_res" + s(i)] = f.v["T_з*" + s(i)] - math.pow(f.v["pt2c1" + s(i)], 2.0) / (2.0 * 1005.0)
        f.v["pt2p_res" + s(i)] = f.v["p_з*" + s(i)] * math.pow(f.v["pt2T" + s(i)] / f.v["T_з*" + s(i)], h1)
        if is_print_res is True:
            print_calc_st_res(f, i)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_start_str()
    calc_part(field, is_print_res)
    if is_print_res:
        print_end_str(field)
