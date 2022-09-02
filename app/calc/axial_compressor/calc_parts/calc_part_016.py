import math
from .gas_table_data import TableData
from . import graph_save_data as gs


def add_variables(f):
    for i in range(1, f.v["i_int"] + 2):
        f.add_variable("pt1D_ср" + s(i), 1.0, "", "")
        f.add_variable("pt1r_ср_rel" + s(i), 1.0, "", "")
        f.add_variable("pt1alpha_1z" + s(i), 0.0, "", "")
        f.add_variable("pt1alpha_2z" + s(i), 0.0, "", "")
        f.add_variable("pt1alpha_3z" + s(i), 0.0, "", "")
        f.add_variable("pt1cos_alpha_3z" + s(i), 0.0, "", "")
        f.add_variable("pt1q" + s(i), 0.0, "", "")
        f.add_variable("pt1pi" + s(i), 0.0, "", "")
        f.add_variable("pt1tau" + s(i), 0.0, "", "")
        f.add_variable("pt1p" + s(i), 0.0, "", "")
        f.add_variable("pt1T" + s(i), 0.0, "", "")


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
    curr_str += "| " + to_fixed(f.v["D_вт" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_н" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["F_" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1D_ср" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_р" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["pt1r_ср_rel" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["pt1alpha_3z" + s(n_st)], n_sym)
    curr_str += "|       " + to_fixed(f.v["pt1cos_alpha_3z" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1q" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1pi" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1tau" + s(n_st)], n_sym)
    if f.v["pt1p" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["pt1p" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt1p" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1T" + s(n_st)], n_sym)
    print(curr_str)


def print_calc_la_res(f, n_st):
    n_sym = 3
    curr_str = ""
    curr_str += "|ЛА"
    if f.v["p_з*" + s(n_st - 1)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["p_з*" + s(n_st - 1)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["p_з*" + s(n_st - 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["T_з*" + s(n_st - 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_вт" + s(n_st - 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_н" + s(n_st - 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["F_" + s(n_st - 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1D_ср" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_р" + s(n_st - 1)], n_sym)
    curr_str += "|   " + to_fixed(f.v["pt1r_ср_rel" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["pt1alpha_3z" + s(n_st)], n_sym)
    curr_str += "|       " + to_fixed(f.v["pt1cos_alpha_3z" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1q" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1pi" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1tau" + s(n_st)], n_sym)
    if f.v["pt1p" + s(n_st)] < 100000.0:
        curr_str += "|  " + to_fixed(f.v["pt1p" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["pt1p" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1T" + s(n_st)], n_sym)
    print(curr_str)


def print_start_str():
    print("*********************************")
    print("calculation of static pressures and temperatures in front of the impeller (first method) (016):")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|p*         "
    curr_str += "|T*      "
    curr_str += "|D_вт  "
    curr_str += "|D_н   "
    curr_str += "|F_    "
    curr_str += "|D_ср  "
    curr_str += "|D_р   "
    curr_str += "|r_ср_rel"
    curr_str += "|alpha_3z"
    curr_str += "|cos_alpha_3z"
    curr_str += "|q     "
    curr_str += "|pi    "
    curr_str += "|tau   "
    curr_str += "|p          "
    curr_str += "|T        "
    print(curr_str)


def print_end_str(f):
    print("*********************************\n")


def deg_to_rad(x):
    return


def calc_part(f, is_print_res):
    tb_data = TableData(["lambda.csv", "q.csv", "tau.csv", "pi.csv"])
    for i in range(1, f.v["i_int"] + 2):
        if i == f.v["i_int"] + 1:
            f.v["pt1D_ср" + s(i)] = (f.v["D_вт" + s(i - 1)] + f.v["D_н" + s(i - 1)]) / 2.0
            f.v["pt1r_ср_rel" + s(i)] = f.v["pt1D_ср" + s(i - 1)] / f.v["D_р" + s(i - 1)]
        else:
            f.v["pt1D_ср" + s(i)] = (f.v["D_вт" + s(i)] + f.v["D_н" + s(i)]) / 2.0
            f.v["pt1r_ср_rel" + s(i)] = f.v["pt1D_ср" + s(i)] / f.v["D_р" + s(i)]
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["pt1alpha_1z" + s(i)] = gs.k_50_1_alpha_1_get(f, f.v["pt1r_ср_rel" + s(i)])
            if i == f.v["i_int"] + 1:
                f.v["pt1alpha_2z" + s(i)] = gs.k_50_1_alpha_2_get(f, f.v["phi*" + s(i - 1)], f.v["pt1r_ср_rel" + s(i)])
            else:
                f.v["pt1alpha_2z" + s(i)] = gs.k_50_1_alpha_2_get(f, f.v["phi*" + s(i)], f.v["pt1r_ср_rel" + s(i)])
            f.v["pt1alpha_3z" + s(i)] = gs.k_50_1_alpha_1_get(f, f.v["pt1r_ср_rel" + s(i)])
        elif f.v["тип ступени"] == 3:
            f.v["pt1alpha_1z" + s(i)] = gs.k_70_17_alpha_1_get(f, f.v["pt1r_ср_rel" + s(i)])
            if i == f.v["i_int"] + 1:
                f.v["pt1alpha_2z" + s(i)] = gs.k_70_17_alpha_2_get(f, f.v["phi*" + s(i - 1)], f.v["pt1r_ср_rel" + s(i)])
            else:
                f.v["pt1alpha_2z" + s(i)] = gs.k_70_17_alpha_2_get(f, f.v["phi*" + s(i)], f.v["pt1r_ср_rel" + s(i)])
            f.v["pt1alpha_3z" + s(i)] = gs.k_70_17_alpha_3_get(f, f.v["pt1r_ср_rel" + s(i)])
        elif f.v["тип ступени"] == 4:
            f.v["pt1alpha_1z" + s(i)] = gs.k_100_2l_alpha_1_get(f, f.v["pt1r_ср_rel" + s(i)])
            f.v["pt1alpha_2z" + s(i)] = 0.0
            f.v["pt1alpha_3z" + s(i)] = gs.k_100_2l_alpha_3_get(f, f.v["pt1r_ср_rel" + s(i)])
        f.v["pt1cos_alpha_3z" + s(i)] = math.cos(math.radians(f.v["pt1alpha_3z" + s(i)]))
        if i == f.v["i_int"] + 1:
            h_1 = f.v["p_з*" + s(i - 1)] * f.v["F_" + s(i - 1)] * f.v["pt1cos_alpha_3z" + s(i)]
        else:
            h_1 = f.v["p*" + s(i)] * f.v["F_" + s(i)] * f.v["pt1cos_alpha_3z" + s(i)]
        if i == f.v["i_int"] + 1:
            f.v["pt1q" + s(i)] = 24.74 * f.v["m"] * math.sqrt(f.v["T_з*" + s(i - 1)]) / h_1
        else:
            f.v["pt1q" + s(i)] = 24.74 * f.v["m"] * math.sqrt(f.v["T*" + s(i)]) / h_1
        f.v["pt1pi" + s(i)] = tb_data.find_nearest_x_point_in_list(1, 3, f.v["pt1q" + s(i)])
        f.v["pt1tau" + s(i)] = tb_data.find_nearest_x_point_in_list(1, 2, f.v["pt1q" + s(i)])
        if i == f.v["i_int"] + 1:
            f.v["pt1p" + s(i)] = f.v["p_з*" + s(i - 1)] * f.v["pt1pi" + s(i)]
            f.v["pt1T" + s(i)] = f.v["T_з*" + s(i - 1)] * f.v["pt1tau" + s(i)]
        else:
            f.v["pt1p" + s(i)] = f.v["p*" + s(i)] * f.v["pt1pi" + s(i)]
            f.v["pt1T" + s(i)] = f.v["T*" + s(i)] * f.v["pt1tau" + s(i)]
        if is_print_res is True:
            if i == f.v["i_int"] + 1:
                print_calc_la_res(f, i)
            else:
                print_calc_st_res(f, i)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_start_str()
    calc_part(field, is_print_res)
    if is_print_res:
        print_end_str(field)
