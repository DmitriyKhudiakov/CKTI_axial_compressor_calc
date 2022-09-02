import math
from . import graph_save_data as gs


def add_variables(f):
    f.add_variable("l_aver", 0.0, "", "l_{ср}")
    f.add_variable("drн_ср_rel", 0.0, "", "\Delta_{\overline{r_{н.ср}}}")
    f.add_variable("drвт_ср_rel", 0.0, "", "\Delta_{\overline{r_{вт.ср}}}")
    f.add_variable("b_aver", 0.0, "", "b_{ср}")
    f.add_variable("l_aver_rel", 0.0, "", "\overline{l_{ср}}")
    f.add_variable("S1z_aver", 0.0, "", "S_{ср.1z}")
    f.add_variable("S2z_aver", 0.0, "", "S_{ср.2z}")
    f.add_variable("S1z_aver_rel", 0.0, "", "\overline{S_{ср.1z}}")
    f.add_variable("S2z_aver_rel", 0.0, "", "\overline{S_{ср.2z}}")
    f.add_variable("Sr_aver_rel", 0.0, "", "\overline{S_{ср.r}}")
    f.add_variable("k_psi_м", 0.0, "", "k_{\psi м}")
    f.add_variable("k_eta_м", 0.0, "", "k_{\eta м}")
    f.add_variable("k_psi_зl", 0.0, "", "k_{\psi з\overline{l}}")
    f.add_variable("k_eta_зl", 0.0, "", "k_{\eta з\overline{l}}")
    f.add_variable("k_psi_z", 0.0, "", "k_{\psi z}")
    f.add_variable("k_eta_z", 0.0, "", "k_{\eta м}")
    f.add_variable("k_psi_dr", 0.0, "", "k_{\psi \Delta r}")
    f.add_variable("k_eta_dr", 0.0, "", "k_{\eta \Delta r}")
    f.add_variable("k_psi_dr_вт", 1.0, "", "k_{\psi \Delta r_{вт}}")
    f.add_variable("k_eta_dr_вт", 1.0, "", "k_{\eta \Delta r_{вт}}")
    f.add_variable("k_psi_dr_н", 1.0, "", "k_{\psi \Delta r_{н}}")
    f.add_variable("k_eta_dr_н", 1.0, "", "k_{\eta \Delta r_{н}}")
    f.add_variable("k_psi", 0.0, "", "k_{\psi}")
    f.add_variable("k_eta", 0.0, "", "k_{\eta}")


def print_calc_res(f):
    print("*********************************")
    print("calculation of coefficients - k_psi and k_eta (011):")
    print("         l_aver = ", f.v["l_aver"])
    print("         drн_ср_rel = ", f.v["drн_ср_rel"])
    print("         drвт_ср_rel = ", f.v["drвт_ср_rel"])
    print("         b_aver = ", f.v["b_aver"])
    print("         l_aver_rel = ", f.v["l_aver_rel"])
    print("         S1z_aver = ", f.v["S1z_aver"])
    print("         S2z_aver = ", f.v["S2z_aver"])
    print("         S1z_aver_rel = ", f.v["S1z_aver_rel"])
    print("         S2z_aver_rel = ", f.v["S2z_aver_rel"])
    print("         Sr_aver_rel = ", f.v["Sr_aver_rel"])
    print("         k_psi_м = ", f.v["k_psi_м"])
    print("         k_eta_м = ", f.v["k_eta_м"])
    print("         k_psi_зl = ", f.v["k_psi_зl"])
    print("         k_eta_зl = ", f.v["k_eta_зl"])
    print("         k_psi_z = ", f.v["k_psi_z"])
    print("         k_eta_z = ", f.v["k_eta_z"])
    print("         k_psi_dr_вт = ", f.v["k_psi_dr_вт"])
    print("         k_psi_dr_н = ", f.v["k_psi_dr_н"])
    print("         k_eta_dr_вт = ", f.v["k_eta_dr_вт"])
    print("         k_eta_dr_н = ", f.v["k_eta_dr_н"])
    print("         k_psi_dr = ", f.v["k_psi_dr"])
    print("         k_eta_dr = ", f.v["k_eta_dr"])
    print("         k_psi = ", f.v["k_psi"])
    print("         k_eta = ", f.v["k_eta"])
    print("*********************************\n")


def geometric_parameters(f):
    f.v["l_aver"] = (f.v["l1"] + f.v["l2"]) / 2.0
    if f.v["тип проточной части"] == 1:
        f.v["drн_ср_rel"] = f.v["dr_н"]
        f.v["drвт_ср_rel"] = (0.0 + f.v["dr_вт"]) / 2.0
    elif f.v["тип проточной части"] == 2:
        f.v["drн_ср_rel"] = (0.0 + f.v["dr_н"]) / 2.0
        f.v["drвт_ср_rel"] = f.v["dr_вт"]
    if f.v["OmegaТ"] == 0.5:
        f.v["b_aver"] = 0.45 * f.v["l_aver"]
        f.v["l_aver_rel"] = 2.25
    elif f.v["OmegaТ"] == 0.7:
        f.v["b_aver"] = 0.5 * f.v["l_aver"]
        f.v["l_aver_rel"] = 2.0
    elif f.v["OmegaТ"] == 1.0:
        f.v["b_aver"] = 0.6 * f.v["l_aver"]
        f.v["l_aver_rel"] = 1.65
    f.v["S1z_aver"] = 0.5 * f.v["b_aver"]
    f.v["S2z_aver"] = 0.175 * f.v["b_aver"]
    f.v["S1z_aver_rel"] = f.v["S1z_aver"] / f.v["b_aver"]
    f.v["S2z_aver_rel"] = f.v["S2z_aver"] / f.v["b_aver"]
    f.v["Sr_aver_rel"] = 0.0075


def coefficients_func_1(f):
    # k_psi_м, k_eta_м
    if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
        if f.v["тип проточной части"] == 1:
            f.v["k_psi_м"] = 0.97
            f.v["k_eta_м"] = 0.99
        elif f.v["тип проточной части"] == 2:
            f.v["k_psi_м"] = 0.97
            f.v["k_eta_м"] = 0.975
    elif f.v["тип ступени"] == 3:
        if f.v["тип проточной части"] == 1:
            f.v["k_psi_м"] = 0.91
            f.v["k_eta_м"] = 0.975
        elif f.v["тип проточной части"] == 2:
            f.v["k_psi_м"] = 0.95
            f.v["k_eta_м"] = 0.975
    elif f.v["тип ступени"] == 4:
        if f.v["тип проточной части"] == 1:
            f.v["k_psi_м"] = 0.980
            f.v["k_eta_м"] = 0.980
        elif f.v["тип проточной части"] == 2:
            f.v["k_psi_м"] = 0.960
            f.v["k_eta_м"] = 0.970


def coefficients_func_2(f):
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
    h_psi_1 = 1.0 - 0.045 * math.sqrt(f.v["OmegaТ"]) * f.v["Sr_aver_rel"] / f.v["l_aver_rel"]
    h_eta_1 = 1.0 - 0.024 * math.sqrt(f.v["OmegaТ"]) * f.v["Sr_aver_rel"] / (1.0 - f.v["l_aver"] / f.v["Dн1"])
    f.v["k_psi_зl"] = h_psi_1 / h_psi_2
    f.v["k_eta_зl"] = h_eta_1 / h_eta_2


def coefficients_func_3(f):
    # k_psi_z, k_eta_z
    h_psi_2 = 1.0
    h_eta_2 = 1.0
    if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
        h_psi_2 = 0.947
        h_eta_2 = 1.03
    elif f.v["тип ступени"] == 3:
        h_psi_2 = 0.934
        h_eta_2 = 1.04
    elif f.v["тип ступени"] == 4:
        h_psi_2 = 0.934
        h_eta_2 = 1.04
    h_psi_1 = gs.psi_sz_get_psi(f, None)
    h_eta_1 = gs.eta_sz_get_eta(f, None)
    f.v["k_psi_z"] = h_psi_1 / h_psi_2
    f.v["k_eta_z"] = h_eta_1 / h_eta_2


def coefficients_func_4(f):
    # k_psi_dr, k_eta_dr
    if f.v["dr_вт"] == 0.0:
        f.v["k_psi_dr_вт"] = 1.0
        f.v["k_eta_dr_вт"] = 1.0
    else:
        f.v["k_eta_dr_вт"] = gs.rk_eta_plus_get_k(f, None)
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["k_psi_dr_вт"] = gs.k_psi_dr_plus_50_get_k(f, None)
        elif f.v["тип ступени"] == 3:
            f.v["k_psi_dr_вт"] = gs.k_psi_dr_plus_70_get_k(f, None)
        elif f.v["тип ступени"] == 4:
            f.v["k_psi_dr_вт"] = gs.k_psi_dr_plus_100_get_k(f, None)
    if f.v["dr_н"] == 0.0:
        f.v["k_psi_dr_н"] = 1.0
        f.v["k_eta_dr_н"] = 1.0
    else:
        f.v["k_eta_dr_нk_eta_dr_н"] = gs.rk_eta_minus_get_k(f, None)
        if f.v["тип ступени"] == 1 or f.v["тип ступени"] == 2:
            f.v["k_psi_dr_н"] = gs.k_psi_dr_minus_50_get_k(f, None)
        elif f.v["тип ступени"] == 3:
            f.v["k_psi_dr_н"] = gs.k_psi_dr_minus_70_get_k(f, None)
        elif f.v["тип ступени"] == 4:
            f.v["k_psi_dr_н"] = gs.k_psi_dr_minus_100_get_k(f, None)
    f.v["k_psi_dr"] = f.v["k_psi_dr_вт"] * f.v["k_psi_dr_н"]
    f.v["k_eta_dr"] = f.v["k_eta_dr_вт"] * f.v["k_eta_dr_н"]


def coefficients_func_5(f):
    # k_psi, k_eta
    f.v["k_psi"] = f.v["k_psi_м"] * f.v["k_psi_зl"] * f.v["k_psi_z"] * f.v["k_psi_dr"]
    f.v["k_eta"] = f.v["k_eta_м"] * f.v["k_eta_зl"] * f.v["k_eta_z"] * f.v["k_eta_dr"]


def calc_part(f):
    geometric_parameters(f)
    coefficients_func_1(f)
    coefficients_func_2(f)
    coefficients_func_3(f)
    coefficients_func_4(f)
    coefficients_func_5(f)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
