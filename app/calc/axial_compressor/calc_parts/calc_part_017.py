import math
from .gas_table_data import TableData
from .graph_data import GraphData
from . import graph_save_data as gs


W_W = 2560
W_H = 1440
pad = 0.05
SCALE = 0.4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)
YELLOW = (255, 255, 0)
CUSTOM1 = (255, 102, 103)
CUSTOM2 = (103, 102, 255)
LL = False
CURR_POS = [0, 0]
X_START = W_W * 0.05
Y_START = W_H // 2
D_SCALE = 0.02
PB = [0, 0]
PE = [0, 0]
TH = 2


def add_variables(f):
    for i in range(1, f.v["i_int"] + 1):
        f.add_variable("D_нз" + s(i), f.v["D_н" + s(i)], "", "")
    for i in range(1, f.v["i_int"] + 2):
        f.add_variable("pt1F_" + s(i), 1.0, "", "")
        f.add_variable("pt1D_ср" + s(i), 1.0, "", "")
        f.add_variable("pt1r_ср_rel" + s(i), 1.0, "", "")
        f.add_variable("pt1alpha_1z" + s(i), 0.0, "", "")
        f.add_variable("pt1alpha_2z" + s(i), 0.0, "", "")
        f.add_variable("pt1alpha_3z" + s(i), 0.0, "", "")
        f.add_variable("pt1cos_alpha_2z" + s(i), 0.0, "", "")
        f.add_variable("pt1q" + s(i), 0.0, "", "")
        f.add_variable("pt1pi" + s(i), 0.0, "", "")
        f.add_variable("pt1tau" + s(i), 0.0, "", "")
        f.add_variable("pt1p" + s(i), f.v["pt1p" + s(i)], "", "")
        f.add_variable("pt1T" + s(i), f.v["pt1T" + s(i)], "", "")


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
        if n_st == f.v["i_int"]:
            curr_str += "|  " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
        else:
            curr_str += "|  " + to_fixed(f.v["p*" + s(n_st + 1)], n_sym)
    else:
        if n_st == f.v["i_int"]:
            curr_str += "| " + to_fixed(f.v["p_з*" + s(n_st)], n_sym)
        else:
            curr_str += "| " + to_fixed(f.v["p*" + s(n_st + 1)], n_sym)
    if n_st == f.v["i_int"]:
        curr_str += "| " + to_fixed(f.v["T_з*" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["T*" + s(n_st + 1)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_вт" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_нз" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1F_" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["pt1D_ср" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["D_р" + s(n_st)], n_sym)
    curr_str += "|   " + to_fixed(f.v["pt1r_ср_rel" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["pt1alpha_2z" + s(n_st)], n_sym)
    curr_str += "|       " + to_fixed(f.v["pt1cos_alpha_2z" + s(n_st)], n_sym)
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
    print("calculation of static pressures and temperatures behind the impeller (first method) (017):")
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


def w_to_r(x):
    global SCALE
    return x / SCALE


def r_to_w(x):
    global SCALE
    return SCALE * x


def get_part_list(n_st, n_parts):
    st_list = []
    delta_list = []
    h1 = n_st - n_parts - 1
    p1 = h1 // n_parts
    p2 = h1 % n_parts
    for i in range(n_parts):
        if p2 > 0:
            delta_list.append(p1 + 1)
            p2 -= 1
        else:
            delta_list.append(p1)
    for i in range(n_parts + 1):
        if i == 0:
            st_list.append(1)
        else:
            st_list.append(st_list[-1] + delta_list[i - 1] + 1)
    return st_list


def get_center_point(f, n_st):
    global PB, PE, RED, X_START, Y_START
    pb = [X_START + r_to_w(f.v["Sz1" + s(1)] * 1000.0 + f.v["bz1ср" + s(1)] + f.v["az2ср" + s(1)]), Y_START]
    for i in range(1, n_st + 1):
        if i > 1:
            l_h = ((f.v["D_н" + s(i - 1)] - f.v["D_вт" + s(i - 1)]) - (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
            delta_y = r_to_w(1000.0 * l_h / 2.0)
            pb[1] += delta_y
        if i == n_st:
            break
        pb[0] += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz2ср" + s(i)] + f.v["az3ср" + s(i)])
        if i < f.v["i_int"]:
            if f.v["тип ступени"] == 3:
                pb[0] += r_to_w(f.v["Sz2" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
            else:
                pb[0] += r_to_w(f.v["Sz3" + s(i)] * 1000.0 + f.v["bz3ср" + s(i)] + f.v["az2ср" + s(i + 1)])
    return pb


def get_enter_blade_point(f, n_st):
    pe = get_center_point(f, n_st)
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    an = r_to_w(f.v["az2н" + s(n_st)])
    p = (pe[0] - an, pe[1] - len / 2.0)
    p_int = (int(p[0]), int(p[1]))
    return p


def get_back_rk(f, n_st):
    pc = get_center_point(f, n_st)
    bn = r_to_w(f.v["bz2н" + s(n_st)])
    bvt = r_to_w(f.v["bz2вт" + s(n_st)])
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    pb1 = (int(pc[0] + bvt), int(pc[1] + len / 2.0))
    pb2 = (int(pc[0] + bn), int(pc[1] - len / 2.0))
    return pb1, pb2


def get_front_rk(f, n_st):
    pc = get_center_point(f, n_st)
    an = r_to_w(f.v["az1н" + s(1)])
    avt = r_to_w(f.v["az1вт" + s(1)])
    len = r_to_w(1000.0 * (f.v["D_н" + s(n_st)] - f.v["D_вт" + s(n_st)])) / 2.0
    pb1 = (int(pc[0] - avt), int(pc[1] + len / 2.0))
    pb2 = (int(pc[0] - an), int(pc[1] - len / 2.0))
    return pb1, pb2


def smoothing(f):
    global RED, BLUE, CUSTOM1, CUSTOM2, Y_START, P_1_Y, TH
    n_parts = 3
    st_list = get_part_list(f.v["i_int"], n_parts)
    for i_n in range(1, n_parts + 1):
        n_curr = st_list[i_n - 1]
        p1 = get_enter_blade_point(f, n_curr)
        p1_int = (int(p1[0]), int(p1[1]))
        p2 = get_enter_blade_point(f, st_list[i_n])
        p2_int = (int(p2[0]), int(p2[1]))
        a1 = p1[1] - p2[1]
        b1 = p2[0] - p1[0]
        c1 = p1[0] * p2[1] - p2[0] * p1[1]
        for i in range(st_list[i_n - 1], st_list[i_n]):
            pb1, pb2 = get_back_rk(f, i)
            a2 = pb1[1] - pb2[1]
            b2 = pb2[0] - pb1[0]
            c2 = pb1[0] * pb2[1] - pb2[0] * pb1[1]
            y_find = (a2 * c1 - c2 * a1) / (a1 * b2 - a2 * b1)
            x_find = (-c1 - b1 * y_find) / a1
            p_new = (int(x_find), int(y_find))
            if p_new[1] > pb2[1]:
                len = r_to_w(1000.0 * (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
                diff = get_enter_blade_point(f, i)[1] + len - y_find
                diff_r = w_to_r(diff) / 1000.0
                f.v["D_нз" + s(i)] = f.v["D_вт" + s(i)] + diff_r * 2.0
        for i in range(st_list[i_n - 1], st_list[i_n]):
            pb1, pb2 = get_front_rk(f, i)
            a2 = pb1[1] - pb2[1]
            b2 = pb2[0] - pb1[0]
            c2 = pb1[0] * pb2[1] - pb2[0] * pb1[1]
            y_find = (a2 * c1 - c2 * a1) / (a1 * b2 - a2 * b1)
            x_find = (-c1 - b1 * y_find) / a1
            p_new = (int(x_find), int(y_find))
            if p_new[1] > pb2[1]:
                len = r_to_w(1000.0 * (f.v["D_н" + s(i)] - f.v["D_вт" + s(i)])) / 2.0
                diff = get_enter_blade_point(f, i)[1] + len - y_find
                diff_r = w_to_r(diff) / 1000.0
                f.v["D_н" + s(i)] = f.v["D_вт" + s(i)] + diff_r * 2.0


def calc_part(f, is_print_res):
    smoothing(f)
    tb_data = TableData(["lambda.csv", "q.csv", "tau.csv", "pi.csv"])
    for i in range(1, f.v["i_int"] + 1):
        f.v["pt1F_" + s(i)] = f.v["pi"] * (math.pow(f.v["D_нз" + s(i)], 2.0) - math.pow(f.v["D_вт" + s(i)], 2.0)) / 4.0
        if i == f.v["i_int"] + 1:
            f.v["pt1D_ср" + s(i)] = (f.v["D_вт" + s(i - 1)] + f.v["D_нз" + s(i - 1)]) / 2.0
            f.v["pt1r_ср_rel" + s(i)] = f.v["pt1D_ср" + s(i - 1)] / f.v["D_р" + s(i - 1)]
        else:
            f.v["pt1D_ср" + s(i)] = (f.v["D_вт" + s(i)] + f.v["D_нз" + s(i)]) / 2.0
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
        f.v["pt1cos_alpha_2z" + s(i)] = math.cos(math.radians(f.v["pt1alpha_2z" + s(i)]))
        if i == f.v["i_int"]:
            h_1 = f.v["p_з*" + s(i)] * f.v["pt1F_" + s(i)] * f.v["pt1cos_alpha_2z" + s(i)]
        else:
            h_1 = f.v["p*" + s(i + 1)] * f.v["pt1F_" + s(i)] * f.v["pt1cos_alpha_2z" + s(i)]
        if i == f.v["i_int"]:
            f.v["pt1q" + s(i)] = 24.74 * f.v["m"] * math.sqrt(f.v["T_з*" + s(i)]) / h_1
        else:
            f.v["pt1q" + s(i)] = 24.74 * f.v["m"] * math.sqrt(f.v["T*" + s(i + 1)]) / h_1
        f.v["pt1pi" + s(i)] = tb_data.find_nearest_x_point_in_list(1, 3, f.v["pt1q" + s(i)])
        f.v["pt1tau" + s(i)] = tb_data.find_nearest_x_point_in_list(1, 2, f.v["pt1q" + s(i)])
        if i == f.v["i_int"]:
            f.v["pt1p" + s(i)] = f.v["p_з*" + s(i)] * f.v["pt1pi" + s(i)]
            f.v["pt1T" + s(i)] = f.v["T_з*" + s(i)] * f.v["pt1tau" + s(i)]
        else:
            f.v["pt1p" + s(i)] = f.v["p*" + s(i + 1)] * f.v["pt1pi" + s(i)]
            f.v["pt1T" + s(i)] = f.v["T*" + s(i + 1)] * f.v["pt1tau" + s(i)]
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
