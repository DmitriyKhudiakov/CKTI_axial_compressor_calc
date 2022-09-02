from .graph_data import GraphData
from . import graph_save_data as gs


def add_variables(f):
    f.add_variable("OmegaТ", 0.0, "", "\Omega_{т}")
    f.add_variable("etaСТ", 0.0, "", "\eta_{ст}")
    f.add_variable("psi", 0.0, "", "\psi")
    # 1 - K-50-1, 2 - K-50-5, 3 - K-70-17, 4 - K-100-2l
    f.add_variable("тип ступени", 0, "", "тип ступени")


def print_calc_res(f):
    print("*********************************")
    print("selection of the degree of reaction (005):")
    print("         OmegaТ = ", f.v["OmegaТ"])
    print("         phi1 = ", f.v["phi1"])
    print("         etaСТ = ", f.v["etaСТ"])
    print("         psi = ", f.v["psi"])
    if f.v["тип ступени"] == 1:
        print("         тип ступени = K-50-1")
    elif f.v["тип ступени"] == 2:
        print("         тип ступени = K-50-5")
    elif f.v["тип ступени"] == 3:
        print("         тип ступени = K-70-17")
    elif f.v["тип ступени"] == 4:
        print("         тип ступени = K-100-2l")
    print("*********************************\n")


def vel_210(f):
    eta_max = [gs.st_k_50_1_get_eta(f, None), gs.st_k_50_5_get_eta(f, None), gs.st_k_70_17_get_eta(f, None), gs.st_k_100_2l_get_eta(f, None)]
    n_eta_max = eta_max.index(max(eta_max))
    psi = [gs.st_k_50_1_get_psi(f, None), gs.st_k_50_5_get_psi(f, None), gs.st_k_70_17_get_psi(f, None), gs.st_k_100_2l_get_psi(f, None)]
    f.v["etaСТ"] = eta_max[n_eta_max]
    f.v["psi"] = psi[n_eta_max]
    if n_eta_max == 0:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 1
    elif n_eta_max == 1:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 2
    elif n_eta_max == 2:
        f.v["OmegaТ"] = 0.7
        f.v["тип ступени"] = 3
    elif n_eta_max == 3:
        f.v["OmegaТ"] = 1.0
        f.v["тип ступени"] = 4


def vel_240(f):
    eta_max = [gs.st_k_50_1_get_eta(f, None), gs.st_k_50_5_get_eta(f, None), gs.st_k_70_17_get_eta(f, None)]
    n_eta_max = eta_max.index(max(eta_max))
    psi = [gs.st_k_50_1_get_psi(f, None), gs.st_k_50_5_get_psi(f, None), gs.st_k_70_17_get_psi(f, None)]
    f.v["etaСТ"] = eta_max[n_eta_max]
    f.v["psi"] = psi[n_eta_max]
    if n_eta_max == 0:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 1
    elif n_eta_max == 1:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 2
    elif n_eta_max == 2:
        f.v["OmegaТ"] = 0.7
        f.v["тип ступени"] = 3


def vel_higher(f):
    eta_max = [gs.st_k_50_1_get_eta(f, None), gs.st_k_50_5_get_eta(f, None)]
    n_eta_max = eta_max.index(max(eta_max))
    psi = [gs.st_k_50_1_get_psi(f, None), gs.st_k_50_5_get_psi(f, None)]
    f.v["etaСТ"] = eta_max[n_eta_max]
    f.v["psi"] = psi[n_eta_max]
    if n_eta_max == 0:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 1
    elif n_eta_max == 1:
        f.v["OmegaТ"] = 0.5
        f.v["тип ступени"] = 2


def param_calc(f, is_cycle):
    if is_cycle is False:
        if f.v["тип ступени"] == 4:
            f.v["rвт"] = 0.5
        else:
            f.v["rвт"] = 0.6
    h_var1 = f.v["m"] * f.v["R"] * f.v["TВ*"]
    h_var2 = (1.0 - pow(f.v["rвт"], 2.0)) * f.v["p1*"] * f.v["n"] * f.v["phi1"]
    f.v["Dн"] = 2.9 * pow(h_var1 / h_var2, 1.0 / 3.0)
    f.v["uн"] = f.v["pi"] * f.v["Dн"] * f.v["n"] / 60.0


def param_clarification(f, is_cycle):
    max_delta_phi = 0.001
    n_iter = 0
    max_n_iter = 10
    if f.v["тип ступени"] == 1:
        f_list = gs.st_k_50_1_eta(f.v["uн"])
    elif f.v["тип ступени"] == 2:
        f_list = gs.st_k_50_5_eta(f.v["uн"])
    elif f.v["тип ступени"] == 3:
        f_list = gs.st_k_70_17_eta(f.v["uн"])
    elif f.v["тип ступени"] == 4:
        f_list = gs.st_k_100_2l_eta(f.v["uн"])
    f_point = GraphData.find_max_y_point_in_list(f_list)
    f.v["phi1"] = f_point[0]
    f.v["etaСТ"] = f_point[1]
    phi_rem = f.v["phi1"]
    while True:
        param_calc(f, is_cycle)
        if f.v["тип ступени"] == 1:
            f_list = gs.st_k_50_1_eta(f.v["uн"])
        elif f.v["тип ступени"] == 2:
            f_list = gs.st_k_50_5_eta(f.v["uн"])
        elif f.v["тип ступени"] == 3:
            f_list = gs.st_k_70_17_eta(f.v["uн"])
        elif f.v["тип ступени"] == 4:
            f_list = gs.st_k_100_2l_eta(f.v["uн"])
        f_point = GraphData.find_max_y_point_in_list(f_list)
        f.v["phi1"] = f_point[0]
        f.v["etaСТ"] = f_point[1]
        if abs(phi_rem - f.v["phi1"]) < max_delta_phi:
            break
        phi_rem = f.v["phi1"]
        n_iter += 1
        if n_iter > max_n_iter:
            break
    if f.v["тип ступени"] == 1:
        f.v["psi"] = gs.st_k_50_1_get_psi(f, None)
    elif f.v["тип ступени"] == 2:
        f.v["psi"] = gs.st_k_50_5_get_psi(f, None)
    elif f.v["тип ступени"] == 3:
        f.v["psi"] = gs.st_k_70_17_get_psi(f, None)
    elif f.v["тип ступени"] == 4:
        f.v["psi"] = gs.st_k_100_2l_get_psi(f, None)


def calc_part(f):
    if f.v["uн"] <= 210:
        vel_210(f)
    elif f.v["uн"] <= 240:
        vel_240(f)
    else:
        vel_higher(f)
    param_clarification(f, False)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
