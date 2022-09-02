import math
from . import calc_part_005 as clc5
from . import calc_part_007 as clc7
from . import calc_part_008 as clc8
from . import calc_part_009 as clc9
from . import graph_save_data as gs
from .graph_data import GraphData


def add_variables(f):
    f.add_variable("n_variants", 0, "", "-")


def add_variant_variables(f, i):
    f.add_variable("phi1" + str(i), 0.0, "", "\\varphi_{1}")
    f.add_variable("rвт" + str(i), 0.0, "", "r_{вт}")
    f.add_variable("Dн" + str(i), 0.0, "", "D_{н}")
    f.add_variable("uн" + str(i), 0.0, "", "u_{н}")
    # for next parts
    f.add_variable("Dн_посл" + str(i), None, "", "D_{н.посл}")
    f.add_variable("eta_посл" + str(i), None, "", "\eta_{посл}")
    f.add_variable("psi_посл" + str(i), None, "", "\psi_{посл}")
    f.add_variable("OmegaТ" + str(i), 0.0, "", "\Omega_{т}")
    f.add_variable("etaСТ" + str(i), 0.0, "", "\eta_{ст}")
    f.add_variable("psi" + str(i), 0.0, "", "\psi")
    # 1 - K-50-1, 2 - K-50-5, 3 - K-70-17, 4 - K-100-2l
    f.add_variable("тип ступени" + str(i), 0, "", "тип ступени")
    # 1 - phi = const, 2 - phi = decrease, 3 - phi = variable
    f.add_variable("закон phi*" + str(i), 0, "", "закон \phi^{*}")
    # 1 - (Dн=const, Dвт!=const), 2 - (Dн!=const, Dвт=const), 3 - (Dн!=const, Dвт!=const)
    f.add_variable("тип проточной части" + str(i), 0, "", "тип проточной части")
    f.add_variable("Hср_ст*" + str(i), 0.0, "", "H_{ср.ст}^{*}")
    f.add_variable("HрЛА*" + str(i), 0.0, "", "H_{p.ла}^{*}")
    f.add_variable("alpha" + str(i), 0.0, "", "\\alpha")
    f.add_variable("i" + str(i), 0.0, "", "i")
    f.add_variable("i_int" + str(i), 0.0, "", "i_{целое}")
    f.add_variable("etaЛА" + str(i), 0.0, "", "\eta_{ла}")
    f.add_variable("a_help" + str(i), 0.0, "", "a_{help}")

    f.add_variable("l1" + str(i), 0.0, "", "l_{1}")
    f.add_variable("l2" + str(i), 0.0, "", "l_{2}")
    f.add_variable("Dн1" + str(i), 0.0, "", "D_{н1}")
    f.add_variable("Dвт1" + str(i), 0.0, "", "D_{вт1}")
    f.add_variable("Dн2" + str(i), 0.0, "", "D_{н2}")
    f.add_variable("Dвт2" + str(i), 0.0, "", "D_{вт2}")
    f.add_variable("rho1*" + str(i), 0.0, "", "\\rho_{1}^{*}")
    f.add_variable("rho_ЛА*" + str(i), 0.0, "", "\\rho_{ла}^{*}")
    f.add_variable("dr_вт" + str(i), 0.0, "", "\Delta r_{вт}")
    f.add_variable("dr_н" + str(i), 0.0, "", "\Delta r_{н}")
    f.add_variable("rвт2_rel" + str(i), 0.0, "", "\overline{r_{вт2}}")


def print_calc_res(f):
    str_r = ""
    if f.v["тип ступени"] == 1:
        str_r += "|K-50-1  "
    elif f.v["тип ступени"] == 2:
        str_r += "|K-50-5  "
    elif f.v["тип ступени"] == 3:
        str_r += "|K-70-17 "
    elif f.v["тип ступени"] == 4:
        str_r += "|K-100-2l"
    str_r += "|" + str(f.v["тип проточной части"]) + "            "
    str_r += "|" + str(f.v["rвт"])
    str_r += "|" + to_fixed(f.v["Dн1"], 4)
    str_r += "|" + to_fixed(f.v["Dвт1"], 4)
    str_r += "|" + to_fixed(f.v["l1"], 4)
    str_r += "|" + to_fixed(f.v["uн"], 4)
    str_r += "|" + to_fixed(f.v["Dн2"], 4)
    str_r += "|" + to_fixed(f.v["Dвт2"], 4)
    str_r += "|" + to_fixed(f.v["l2"], 4)
    str_r += "|" + to_fixed(f.v["Dвт2"] / f.v["Dн1"], 4)
    if f.v["i_int"] > 9:
        str_r += "|" + to_fixed(f.v["i_int"], 0)
    else:
        str_r += "|" + to_fixed(f.v["i_int"], 0) + " "
    str_r += "|" + to_fixed(f.v["etaЛА"], 4)
    str_r += "|" + to_fixed(f.v["dr_вт"], 4)
    if f.v["dr_н"] < 0:
        str_r += "|" + to_fixed(f.v["dr_н"], 4) + "|"
    else:
        str_r += "|" + to_fixed(f.v["dr_н"], 4) + " |"
    print(str_r)


def print_start_str():
    print("*********************************")
    print("selection of parameters (010):")
    str_r = ""
    str_r += "|тип ст. "
    str_r += "|тип пр. части"
    str_r += "|rвт"
    str_r += "|Dн1   "
    str_r += "|Dвт1  "
    str_r += "|l1    "
    str_r += "|uн1     "
    str_r += "|Dн2   "
    str_r += "|Dвт2  "
    str_r += "|l2    "
    str_r += "|rвт2  "
    str_r += "|i "
    str_r += "|etaЛА*"
    str_r += "|drвт  "
    str_r += "|drн    |"
    print(str_r)


def print_best_param():
    print("Best variant:")


def print_end_str():
    print("*********************************\n")


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def calc_param(f, i_r, delta_r, nv):
    f.v["Dн1" + str(nv)] = f.v["Dн" + str(nv)]
    f.v["Dвт1" + str(nv)] = f.v["rвт" + str(nv)] * f.v["Dн1" + str(nv)]
    f.v["l1" + str(nv)] = (f.v["Dн1" + str(nv)] - f.v["Dвт1" + str(nv)]) / 2.0
    exp_ind = 1.0 - (f.v["k"] - 1.0) / (f.v["k"] * f.v["etaЛА" + str(nv)])
    f.v["rho1*" + str(nv)] = (f.v["p1*"]) / (f.v["R"] * f.v["TВ*"])
    f.v["rho_ЛА*" + str(nv)] = f.v["rho1*" + str(nv)] * pow((f.v["pЛА*"]) / (f.v["p1*"]), exp_ind)
    if f.v["тип проточной части" + str(nv)] == 1:
        if f.v["закон phi*" + str(nv)] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*" + str(nv)] * f.v["phi1" + str(nv)] * f.v["uн" + str(nv)])
            f.v["Dвт2" + str(nv)] = math.sqrt(pow(f.v["Dн1" + str(nv)], 2.0) - h1)
            f.v["Dн2" + str(nv)] = f.v["Dн1" + str(nv)]
            f.v["l2" + str(nv)] = (f.v["Dн2" + str(nv)] - f.v["Dвт2" + str(nv)]) / 2.0
            f.v["dr_вт" + str(nv)] = (f.v["Dвт2" + str(nv)] / f.v["Dн2" + str(nv)]) - f.v["rвт" + str(nv)]
            f.v["dr_н" + str(nv)] = 0
    elif f.v["тип проточной части" + str(nv)] == 2:
        if f.v["закон phi*" + str(nv)] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*" + str(nv)] * f.v["phi1" + str(nv)] * f.v["uн" + str(nv)])
            f.v["Dвт2" + str(nv)] = f.v["Dвт1" + str(nv)]
            f.v["Dн2" + str(nv)] = math.sqrt(pow(f.v["Dвт1" + str(nv)], 2.0) + h1)
            f.v["l2" + str(nv)] = (f.v["Dн2" + str(nv)] - f.v["Dвт2" + str(nv)]) / 2.0
            f.v["dr_н" + str(nv)] = (f.v["Dн2" + str(nv)] - f.v["Dн1" + str(nv)]) / (f.v["Dн1" + str(nv)])
            if i_r == 0:
                f.v["dr_вт" + str(nv)] = 0.0
            else:
                f.v["dr_вт" + str(nv)] = i_r * delta_r
    elif f.v["тип проточной части" + str(nv)] == 3:
        if f.v["закон phi*" + str(nv)] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*" + str(nv)] * f.v["phi1" + str(nv)] * f.v["uн" + str(nv)])
            f.v["Dвт2" + str(nv)] = math.sqrt(pow(f.v["Dн1" + str(nv)], 2.0) - h1)
            f.v["Dвт2" + str(nv)] = math.sqrt(pow(f.v["Dвт1" + str(nv)], 2.0) + h1)
            f.v["l2" + str(nv)] = (f.v["Dн2" + str(nv)] - f.v["Dвт2" + str(nv)]) / 2.0
            f.v["dr_н" + str(nv)] = (f.v["Dн2" + str(nv)] - f.v["Dвт2" + str(nv)]) / (f.v["Dвт2" + str(nv)])
            f.v["dr_вт" + str(nv)] = f.v["Dвт2" + str(nv)] / f.v["Dн2" + str(nv)] - f.v["rвт" + str(nv)]
    f.v["rвт2_rel" + str(nv)] = f.v["Dвт2" + str(nv)] / f.v["Dн1" + str(nv)]


def param_calc(f, is_cycle, nv):
    if is_cycle is False:
        if f.v["тип ступени" + str(nv)] == 4:
            f.v["rвт" + str(nv)] = 0.5
        else:
            f.v["rвт" + str(nv)] = 0.6
    h_var1 = f.v["m"] * f.v["R"] * f.v["TВ*"]
    h_var2 = (1.0 - pow(f.v["rвт" + str(nv)], 2.0)) * f.v["p1*"] * f.v["n"] * f.v["phi1" + str(nv)]
    f.v["Dн" + str(nv)] = 2.9 * pow(h_var1 / h_var2, 1.0 / 3.0)
    f.v["uн" + str(nv)] = f.v["pi"] * f.v["Dн" + str(nv)] * f.v["n"] / 60.0


def param_clarification(f, is_cycle, nv):
    max_delta_phi = 0.001
    n_iter = 0
    max_n_iter = 10
    if f.v["тип ступени" + str(nv)] == 1:
        f_list = gs.st_k_50_1_eta(f.v["uн" + str(nv)])
    elif f.v["тип ступени" + str(nv)] == 2:
        f_list = gs.st_k_50_5_eta(f.v["uн" + str(nv)])
    elif f.v["тип ступени" + str(nv)] == 3:
        f_list = gs.st_k_70_17_eta(f.v["uн" + str(nv)])
    elif f.v["тип ступени" + str(nv)] == 4:
        f_list = gs.st_k_100_2l_eta(f.v["uн" + str(nv)])
    f_point = GraphData.find_max_y_point_in_list(f_list)
    f.v["phi1" + str(nv)] = f_point[0]
    f.v["etaСТ" + str(nv)] = f_point[1]
    phi_rem = f.v["phi1" + str(nv)]
    while True:
        param_calc(f, is_cycle, nv)
        if f.v["тип ступени" + str(nv)] == 1:
            f_list = gs.st_k_50_1_eta(f.v["uн" + str(nv)])
        elif f.v["тип ступени" + str(nv)] == 2:
            f_list = gs.st_k_50_5_eta(f.v["uн" + str(nv)])
        elif f.v["тип ступени" + str(nv)] == 3:
            f_list = gs.st_k_70_17_eta(f.v["uн" + str(nv)])
        elif f.v["тип ступени" + str(nv)] == 4:
            f_list = gs.st_k_100_2l_eta(f.v["uн" + str(nv)])
        f_point = GraphData.find_max_y_point_in_list(f_list)
        f.v["phi1" + str(nv)] = f_point[0]
        f.v["etaСТ" + str(nv)] = f_point[1]
        if abs(phi_rem - f.v["phi1" + str(nv)]) < max_delta_phi:
            break
        phi_rem = f.v["phi1" + str(nv)]
        n_iter += 1
        if n_iter > max_n_iter:
            break
    if f.v["тип ступени" + str(nv)] == 1:
        f.v["psi" + str(nv)] = gs.st_k_50_1_get_psi(f, nv)
    elif f.v["тип ступени" + str(nv)] == 2:
        f.v["psi" + str(nv)] = gs.st_k_50_5_get_psi(f, nv)
    elif f.v["тип ступени" + str(nv)] == 3:
        f.v["psi" + str(nv)] = gs.st_k_70_17_get_psi(f, nv)
    elif f.v["тип ступени" + str(nv)] == 4:
        f.v["psi" + str(nv)] = gs.st_k_100_2l_get_psi(f, nv)


def alpha_list(f):
    f_list = None
    if (f.v["k"] >= 1.35) and (f.v["k"] < 1.53):
        use_graph = GraphData("alpha_14.csv")
        f_list = use_graph.get_data(True, False, False)
    elif f.v["k"] < 1.35:
        use_graph = GraphData("alpha_13.csv")
        f_list = use_graph.get_data(True, False, False)
    elif f.v["k"] > 1.53:
        use_graph = GraphData("alpha_16.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def get_alpha_value(f):
    f_list = alpha_list(f)
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["ПЛА*"])
    return f_point[1]


def calc_part_7(f, nv):
    if f.v["psi_посл" + str(nv)] is not None:
        psi_aver = (f.v["psi" + str(nv)] + f.v["psi_посл" + str(nv)]) / 2.0
    else:
        psi_aver = f.v["psi" + str(nv)]
    if f.v["тип проточной части" + str(nv)] == 1:
        k_psi = 0.98
    else:
        k_psi = 0.97
    f.v["Hср_ст*" + str(nv)] = k_psi * psi_aver * pow(f.v["uн" + str(nv)], 2.0) / 2.0
    f.v["alpha" + str(nv)] = get_alpha_value(f)
    f.v["HрЛА*" + str(nv)] = f.v["alpha" + str(nv)] * f.v["HЛА*"]
    f.v["i" + str(nv)] = f.v["HрЛА*" + str(nv)] / f.v["Hср_ст*" + str(nv)]
    f.v["i_int" + str(nv)] = math.ceil(f.v["i" + str(nv)])


def calc_part_8(f, nv):
    if f.v["eta_посл" + str(nv)] is not None:
        eta_aver = (f.v["etaСТ" + str(nv)] + f.v["eta_посл" + str(nv)]) / 2.0
    else:
        eta_aver = f.v["etaСТ" + str(nv)]
    f.v["a_help" + str(nv)] = (f.v["i" + str(nv)] * eta_aver) / (f.v["i" + str(nv)] - 1.0 + eta_aver)
    h1 = pow(f.v["ПЛА*"], (f.v["k"] - 1.0) / f.v["k"]) - 1.0
    h2 = f.v["a_help" + str(nv)] * (pow(f.v["ПЛА*"], (f.v["k"] - 1.0) / (f.v["a_help" + str(nv)] * f.v["k"])) - 1.0)
    f.v["etaЛА" + str(nv)] = eta_aver * h1 / h2


def iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res, nv):
    h_var1 = f.v["m"] * f.v["R"] * f.v["TВ*"]
    h_var2 = (1.0 - pow(f.v["rвт" + str(nv)], 2.0)) * f.v["p1*"] * f.v["n"] * f.v["phi1" + str(nv)]
    f.v["Dн" + str(nv)] = 2.9 * pow(h_var1 / h_var2, 1.0 / 3.0)
    f.v["uн" + str(nv)] = f.v["pi"] * f.v["Dн"] * f.v["n"] / 60.0
    f.v["тип ступени" + str(nv)] = i_st
    f.v["тип проточной части" + str(nv)] = i_t_st
    if f.v["тип ступени" + str(nv)] == 1:
        f.v["OmegaТ" + str(nv)] = 0.5
    elif f.v["тип ступени" + str(nv)] == 2:
        f.v["OmegaТ" + str(nv)] = 0.5
    elif f.v["тип ступени" + str(nv)] == 3:
        f.v["OmegaТ" + str(nv)] = 0.7
    elif f.v["тип ступени" + str(nv)] == 4:
        f.v["OmegaТ" + str(nv)] = 1.0

    param_clarification(f, True, nv)
    # clc5.param_clarification(f, True)
    f.v["закон phi*" + str(nv)] = 1
    f.v["тип проточной части" + str(nv)] = i_t_st
    if f.v["закон phi*" + str(nv)] == 1:
        f.v["eta_посл" + str(nv)] = f.v["etaСТ" + str(nv)]
        f.v["psi_посл" + str(nv)] = f.v["psi" + str(nv)]

    calc_part_7(f, nv)
    # clc7.run(f, False, False)
    calc_part_8(f, nv)
    # clc8.run(f, False, False)
    calc_param(f, i_r, delta_r, nv)
    if is_print_res is True:
        print_calc_res(f)


def calc_part(f, is_print_res):
    if is_print_res is True:
        print_start_str()
    n_min_st = 100
    best_param = []
    start_phi1 = 0.6
    delta_r = 0.02
    nv = 0
    # if abs(f.v["dr_н"]) > 0.2 or abs(f.v["dr_вт"]) > 0.2:
    if True is True:
        n_iter_r = 12
        for i_r in range(n_iter_r):
            if i_r != 0:
                n_st_perm = 4
            else:
                n_st_perm = 5
            for i_st in range(1, n_st_perm):
                if i_r == 0:
                    for i_t_st in range(1, 3):
                        nv += 1
                        add_variant_variables(f, nv)
                        if i_st == 4:
                            f.v["rвт" + str(nv)] = 0.5 + i_r * delta_r
                        else:
                            f.v["rвт" + str(nv)] = 0.6 + i_r * delta_r
                        f.v["phi1" + str(nv)] = start_phi1
                        iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res, nv)
                        if f.v["i_int" + str(nv)] < n_min_st:
                            n_min_st = f.v["i_int" + str(nv)]
                            best_param = [i_r, i_st, i_t_st]
                else:
                    for i_t_st in range(2, 3):
                        nv += 1
                        add_variant_variables(f, nv)
                        f.v["phi1" + str(nv)] = start_phi1
                        if i_st == 4:
                            f.v["rвт" + str(nv)] = 0.5 + i_r * delta_r
                        else:
                            f.v["rвт" + str(nv)] = 0.6 + i_r * delta_r
                        iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res, nv)
                        if f.v["i_int" + str(nv)] < n_min_st:
                            n_min_st = f.v["i_int" + str(nv)]
                            best_param = [i_r, i_st, i_t_st]
    # best_param = [1, 2, 2]
    f.v["n_variants"] = int(nv)
    '''
    if best_param[1] == 4:
        f.v["rвт"] = 0.5 + best_param[0] * delta_r
    else:
        f.v["rвт"] = 0.6 + best_param[0] * delta_r
    f.v["phi1"] = start_phi1
    if is_print_res is True:
        print_best_param()
    choose_variant = 1
    iter_by_param(f, best_param[0], delta_r, best_param[1], best_param[2], is_print_res, choose_variant)
    if is_print_res is True:
        print_end_str()
    '''


def run(field, is_add_variables, is_print_res):
    if is_add_variables is True:
        add_variables(field)
    calc_part(field, is_print_res)
