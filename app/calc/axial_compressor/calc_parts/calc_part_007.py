import math
from .graph_data import GraphData


def add_variables(f):
    f.add_variable("Hср_ст*", 0.0, "", "H_{ср.ст}^{*}")
    f.add_variable("HрЛА*", 0.0, "", "H_{p.ла}^{*}")
    f.add_variable("alpha", 0.0, "", "\\alpha")
    f.add_variable("i", 0.0, "", "i")
    f.add_variable("i_int", 0.0, "", "i_{целое}")


def add_new_variables(f):
    f.add_variable("Hср_ст*", 0.0, "H_{ср.ст}^{*}")
    f.add_variable("HрЛА*", 0.0, "H_{p.ла}^{*}")
    f.add_variable("alpha", 0.0, "\\alpha")
    f.add_variable("i", 0.0, "i")
    f.add_variable("i_int", 0.0, "i_{целое}")


def print_calc_res(f):
    print("*********************************")
    print("number of compressor stages (007):")
    print("         Hср_ст* = ", f.v["Hср_ст*"])
    print("         alpha = ", f.v["alpha"])
    print("         HрЛА* = ", f.v["HрЛА*"])
    print("         i = ", f.v["i"])
    print("*********************************\n")


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


def calc_part(f):
    if f.v["psi_посл"] is not None:
        psi_aver = (f.v["psi"] + f.v["psi_посл"]) / 2.0
    else:
        psi_aver = f.v["psi"]
    if f.v["тип проточной части"] == 1:
        k_psi = 0.98
    else:
        k_psi = 0.97
    f.v["Hср_ст*"] = k_psi * psi_aver * pow(f.v["uн"], 2.0) / 2.0
    f.v["alpha"] = get_alpha_value(f)
    f.v["HрЛА*"] = f.v["alpha"] * f.v["HЛА*"]
    f.v["i"] = f.v["HрЛА*"] / f.v["Hср_ст*"]
    f.v["i_int"] = math.ceil(f.v["i"])


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
