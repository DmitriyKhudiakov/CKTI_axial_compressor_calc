from . import graph_save_data as gs


def add_variables(f):
    for i in range(1, f.v["i_int"] + 1):
        f.add_variable("rн_rel" + s(i), 1.0, "", "")
        f.add_variable("rср_rel" + s(i), 1.0, "", "")
        f.add_variable("az1вт" + s(i), 1.0, "", "")
        f.add_variable("bz1вт" + s(i), 1.0, "", "")
        f.add_variable("az1н" + s(i), 1.0, "", "")
        f.add_variable("bz1н" + s(i), 1.0, "", "")
        f.add_variable("az1ср" + s(i), 1.0, "", "")
        f.add_variable("bz1ср" + s(i), 1.0, "", "")
        f.add_variable("az2вт" + s(i), 1.0, "", "")
        f.add_variable("bz2вт" + s(i), 1.0, "", "")
        f.add_variable("az2н" + s(i), 1.0, "", "")
        f.add_variable("bz2н" + s(i), 1.0, "", "")
        f.add_variable("az2ср" + s(i), 1.0, "", "")
        f.add_variable("bz2ср" + s(i), 1.0, "", "")
        f.add_variable("az3вт" + s(i), 1.0, "", "")
        f.add_variable("bz3вт" + s(i), 1.0, "", "")
        f.add_variable("az3н" + s(i), 1.0, "", "")
        f.add_variable("bz3н" + s(i), 1.0, "", "")
        f.add_variable("az3ср" + s(i), 1.0, "", "")
        f.add_variable("bz3ср" + s(i), 1.0, "", "")
        f.add_variable("az4вт" + s(i), 1.0, "", "")
        f.add_variable("bz4вт" + s(i), 1.0, "", "")
        f.add_variable("az4н" + s(i), 1.0, "", "")
        f.add_variable("bz4н" + s(i), 1.0, "", "")
        f.add_variable("az4ср" + s(i), 1.0, "", "")
        f.add_variable("bz4ср" + s(i), 1.0, "", "")
        f.add_variable("Sr1" + s(i), 1.0, "", "")
        f.add_variable("Sr2" + s(i), 1.0, "", "")
        f.add_variable("Sr3" + s(i), 1.0, "", "")
        f.add_variable("Sr4" + s(i), 1.0, "", "")
        f.add_variable("Sz1" + s(i), 1.0, "", "")
        f.add_variable("Sz2" + s(i), 1.0, "", "")
        f.add_variable("Sz3" + s(i), 1.0, "", "")
        f.add_variable("Sz4" + s(i), 1.0, "", "")
    f.add_variable("b_мод", 1.0, "", "")
    f.add_variable("b_k", 1.0, "", "")


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
    curr_str += "|   " + to_fixed(f.v["r_вт_rel" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["rн_rel" + s(n_st)], n_sym)
    curr_str += "|  " + to_fixed(f.v["rср_rel" + s(n_st)], n_sym)
    curr_str += "| " + to_fixed(f.v["b_k"], n_sym)
    if f.v["az1вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az1вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az1вт" + s(n_st)], n_sym)
    if f.v["az1н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az1н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az1н" + s(n_st)], n_sym)
    if f.v["az1ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az1ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az1ср" + s(n_st)], n_sym)
    if f.v["az2вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az2вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az2вт" + s(n_st)], n_sym)
    if f.v["az2н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az2н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az2н" + s(n_st)], n_sym)
    if f.v["az2ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az2ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az2ср" + s(n_st)], n_sym)
    if f.v["az3вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az3вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az3вт" + s(n_st)], n_sym)
    if f.v["az3н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az3н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az3н" + s(n_st)], n_sym)
    if f.v["az3ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az3ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az3ср" + s(n_st)], n_sym)
    if f.v["az4вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az4вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az4вт" + s(n_st)], n_sym)
    if f.v["az4н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az4н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az4н" + s(n_st)], n_sym)
    if f.v["az4ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["az4ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["az4ср" + s(n_st)], n_sym)
    ##############
    if f.v["bz1вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz1вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz1вт" + s(n_st)], n_sym)
    if f.v["bz1н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz1н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz1н" + s(n_st)], n_sym)
    if f.v["bz1ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz1ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz1ср" + s(n_st)], n_sym)
    if f.v["bz2вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz2вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz2вт" + s(n_st)], n_sym)
    if f.v["bz2н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz2н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz2н" + s(n_st)], n_sym)
    if f.v["bz2ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz2ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz2ср" + s(n_st)], n_sym)
    if f.v["bz3вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz3вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz3вт" + s(n_st)], n_sym)
    if f.v["bz3н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz3н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz3н" + s(n_st)], n_sym)
    if f.v["bz3ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz3ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz3ср" + s(n_st)], n_sym)
    if f.v["bz4вт" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz4вт" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz4вт" + s(n_st)], n_sym)
    if f.v["bz4н" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz4н" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz4н" + s(n_st)], n_sym)
    if f.v["bz4ср" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["bz4ср" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["bz4ср" + s(n_st)], n_sym)
    curr_str += "|"
    print(curr_str)


def print_calc_st_res_2(f, n_st):
    n_sym = 3
    curr_str = ""
    s_add = ""
    if n_st < 10:
        curr_str += "| " + s(n_st)
    else:
        curr_str += "|" + s(n_st)
    if f.v["Sr1" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sr1" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sr1" + s(n_st)], n_sym)
    if f.v["Sr2" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sr2" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sr2" + s(n_st)], n_sym)
    if f.v["Sr3" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sr3" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sr3" + s(n_st)], n_sym)
    if f.v["Sr4" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sr4" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sr4" + s(n_st)], n_sym)
    if f.v["Sz1" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sz1" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sz1" + s(n_st)], n_sym)
    if f.v["Sz2" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sz2" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sz2" + s(n_st)], n_sym)
    if f.v["Sz3" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sz3" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sz3" + s(n_st)], n_sym)
    if f.v["Sz4" + s(n_st)] < 10.0:
        curr_str += "|  " + to_fixed(f.v["Sz4" + s(n_st)], n_sym)
    else:
        curr_str += "| " + to_fixed(f.v["Sz4" + s(n_st)], n_sym)
    curr_str += "|"
    print(curr_str)


def print_start_str():
    print("*********************************")
    print("geometric parameters (013):")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|r_вт_rel"
    curr_str += "|rн_rel"
    curr_str += "|rср_rel"
    curr_str += "|b_k   "
    curr_str += "|az1вт  "
    curr_str += "|az1н   "
    curr_str += "|az1ср  "
    curr_str += "|az2вт  "
    curr_str += "|az2н   "
    curr_str += "|az2ср  "
    curr_str += "|az3вт  "
    curr_str += "|az3н   "
    curr_str += "|az3ср  "
    curr_str += "|az4вт  "
    curr_str += "|az4н   "
    curr_str += "|az4ср  "
    curr_str += "|bz1вт  "
    curr_str += "|bz1н   "
    curr_str += "|bz1ср  "
    curr_str += "|bz2вт  "
    curr_str += "|bz2н   "
    curr_str += "|bz2ср  "
    curr_str += "|bz3вт  "
    curr_str += "|bz3н   "
    curr_str += "|bz3ср  "
    curr_str += "|bz4вт  "
    curr_str += "|bz4н   "
    curr_str += "|bz4ср  "
    curr_str += "|"
    print(curr_str)


def print_intermediate_str():
    print("\n")
    curr_str = ""
    curr_str += "|№ "
    curr_str += "|Sr1    "
    curr_str += "|Sr2    "
    curr_str += "|Sr3    "
    curr_str += "|Sr4    "
    curr_str += "|Sz1    "
    curr_str += "|Sz2    "
    curr_str += "|Sz3    "
    curr_str += "|Sz4    "
    curr_str += "|"
    print(curr_str)


def print_end_str():
    print("*********************************\n")


def calc_part(f, is_print_res):
    f.v["b_мод"] = 0.03
    f.v["b_k"] = f.v["b_aver"] / f.v["b_мод"]
    for i in range(1, f.v["i_int"] + 1):
        f.v["rн_rel" + s(i)] = f.v["D_н" + s(i)] / f.v["Dн1"]
        f.v["rср_rel" + s(i)] = (f.v["rн_rel" + s(i)] + f.v["r_вт_rel" + s(i)]) / 2.0
        if f.v["тип ступени"] == 1:
            f.v["az1вт" + s(i)] = gs.k_50_1_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az1н" + s(i)] = gs.k_50_1_a1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az1ср" + s(i)] = gs.k_50_1_a1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az2вт" + s(i)] = gs.k_50_1_a2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az2н" + s(i)] = gs.k_50_1_a2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az2ср" + s(i)] = gs.k_50_1_a2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az3вт" + s(i)] = gs.k_50_1_a2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az3н" + s(i)] = gs.k_50_1_a2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az3ср" + s(i)] = gs.k_50_1_a2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az4вт" + s(i)] = gs.k_50_1_a4z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az4н" + s(i)] = gs.k_50_1_a4z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az4ср" + s(i)] = gs.k_50_1_a4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1вт" + s(i)] = gs.k_50_1_b1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1н" + s(i)] = gs.k_50_1_b1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1ср" + s(i)] = gs.k_50_1_b1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2вт" + s(i)] = gs.k_50_1_b2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2н" + s(i)] = gs.k_50_1_b2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2ср" + s(i)] = gs.k_50_1_b2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3вт" + s(i)] = gs.k_50_1_b2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3н" + s(i)] = gs.k_50_1_b2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3ср" + s(i)] = gs.k_50_1_b2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4вт" + s(i)] = gs.k_50_1_b4z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4н" + s(i)] = gs.k_50_1_b4z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4ср" + s(i)] = gs.k_50_1_b4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
        elif f.v["тип ступени"] == 2:
            f.v["az1вт" + s(i)] = gs.k_50_1_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az1н" + s(i)] = gs.k_50_1_a1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az1ср" + s(i)] = gs.k_50_1_a1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az2вт" + s(i)] = gs.k_50_1_a2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az2н" + s(i)] = gs.k_50_1_a2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az2ср" + s(i)] = gs.k_50_1_a2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az3вт" + s(i)] = gs.k_50_5_a3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az3н" + s(i)] = gs.k_50_5_a3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az3ср" + s(i)] = gs.k_50_5_a3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az4вт" + s(i)] = gs.k_50_1_a4z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az4н" + s(i)] = gs.k_50_1_a4z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az4ср" + s(i)] = gs.k_50_1_a4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1вт" + s(i)] = gs.k_50_1_b1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1н" + s(i)] = gs.k_50_1_b1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1ср" + s(i)] = gs.k_50_1_b1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2вт" + s(i)] = gs.k_50_1_b2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2н" + s(i)] = gs.k_50_1_b2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2ср" + s(i)] = gs.k_50_1_b2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3вт" + s(i)] = gs.k_50_5_b3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3н" + s(i)] = gs.k_50_5_b3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3ср" + s(i)] = gs.k_50_5_b3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4вт" + s(i)] = gs.k_50_1_b4z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4н" + s(i)] = gs.k_50_1_b4z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4ср" + s(i)] = gs.k_50_1_b4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
        elif f.v["тип ступени"] == 3:
            f.v["az1вт" + s(i)] = gs.k_70_17_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az1н" + s(i)] = gs.k_70_17_a1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az1ср" + s(i)] = gs.k_70_17_a1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az2вт" + s(i)] = gs.k_70_17_a2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az2н" + s(i)] = gs.k_70_17_a2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az2ср" + s(i)] = gs.k_70_17_a2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az3вт" + s(i)] = gs.k_70_17_a3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az3н" + s(i)] = gs.k_70_17_a3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az3ср" + s(i)] = gs.k_70_17_a3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az4вт" + s(i)] = 0.0 * f.v["b_k"]
            f.v["az4н" + s(i)] = 0.0 * f.v["b_k"]
            f.v["az4ср" + s(i)] = 0.0 * f.v["b_k"]
            f.v["bz1вт" + s(i)] = gs.k_70_17_b1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1н" + s(i)] = gs.k_70_17_b1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1ср" + s(i)] = gs.k_70_17_b1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2вт" + s(i)] = gs.k_70_17_b2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2н" + s(i)] = gs.k_70_17_b2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2ср" + s(i)] = gs.k_70_17_b2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3вт" + s(i)] = gs.k_70_17_b3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3н" + s(i)] = gs.k_70_17_b3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3ср" + s(i)] = gs.k_70_17_b3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4вт" + s(i)] = 0.0 * f.v["b_k"]
            f.v["bz4н" + s(i)] = 0.0 * f.v["b_k"]
            f.v["bz4ср" + s(i)] = 0.0 * f.v["b_k"]
        elif f.v["тип ступени"] == 4:
            f.v["az1вт" + s(i)] = gs.k_100_2l_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az1н" + s(i)] = gs.k_100_2l_a1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az1ср" + s(i)] = gs.k_100_2l_a1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az2вт" + s(i)] = gs.k_100_2l_a2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az2н" + s(i)] = gs.k_100_2l_a2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az2ср" + s(i)] = gs.k_100_2l_a2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az3вт" + s(i)] = gs.k_100_2l_a3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az3н" + s(i)] = gs.k_100_2l_a3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["az3ср" + s(i)] = gs.k_100_2l_a3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["az4вт" + s(i)] = gs.k_100_2l_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az4н" + s(i)] = gs.k_100_2l_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["az4ср" + s(i)] = gs.k_100_2l_a1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1вт" + s(i)] = gs.k_100_2l_b1z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1н" + s(i)] = gs.k_100_2l_b1z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz1ср" + s(i)] = gs.k_100_2l_b1z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2вт" + s(i)] = gs.k_100_2l_b2z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2н" + s(i)] = gs.k_100_2l_b2z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz2ср" + s(i)] = gs.k_100_2l_b2z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3вт" + s(i)] = gs.k_100_2l_b3z_get(f.v["r_вт_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3н" + s(i)] = gs.k_100_2l_b3z_get(f.v["rн_rel" + s(i)]) * f.v["b_k"]
            f.v["bz3ср" + s(i)] = gs.k_100_2l_b3z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4вт" + s(i)] = gs.k_100_2l_b4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4н" + s(i)] = gs.k_100_2l_b4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
            f.v["bz4ср" + s(i)] = gs.k_100_2l_b4z_get(f.v["rср_rel" + s(i)]) * f.v["b_k"]
        if is_print_res is True:
            print_calc_st_res_1(f, i)
    if is_print_res is True:
        print_intermediate_str()
    for i in range(1, f.v["i_int"] + 1):
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["Sr1" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr2" + s(i)] = 0.51 * f.v["b_aver"]
            f.v["Sr3" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr4" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sz1" + s(i)] = 0.24 * f.v["b_aver"]
            f.v["Sz2" + s(i)] = 0.24 * f.v["b_aver"]
            f.v["Sz3" + s(i)] = 0.24 * f.v["b_aver"]
            f.v["Sz4" + s(i)] = 0.0 * f.v["b_aver"]
        elif f.v["тип ступени"] == 3:
            f.v["Sr1" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr2" + s(i)] = 0.6 * f.v["b_aver"]
            f.v["Sr3" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr4" + s(i)] = 0.0 * f.v["b_aver"]
            f.v["Sz1" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sz2" + s(i)] = 0.4 * f.v["b_aver"]
            f.v["Sz3" + s(i)] = 0.0 * f.v["b_aver"]
            f.v["Sz4" + s(i)] = 0.0 * f.v["b_aver"]
        elif f.v["тип ступени"] == 4:
            f.v["Sr1" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr2" + s(i)] = 0.57 * f.v["b_aver"]
            f.v["Sr3" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sr4" + s(i)] = 0.5 * f.v["b_aver"]
            f.v["Sz1" + s(i)] = 0.8 * f.v["b_aver"]
            f.v["Sz2" + s(i)] = 0.8 * f.v["b_aver"]
            f.v["Sz3" + s(i)] = 0.8 * f.v["b_aver"]
            f.v["Sz4" + s(i)] = 0.0 * f.v["b_aver"]
        if is_print_res is True:
            print_calc_st_res_2(f, i)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_start_str()
    calc_part(field, is_print_res)
    if is_print_res:
        print_end_str()
    dr.draw(field, True)
