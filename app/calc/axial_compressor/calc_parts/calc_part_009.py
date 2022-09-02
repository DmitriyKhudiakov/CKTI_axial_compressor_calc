import math


def add_variables(f):
    f.add_variable("l1", 0.0, "", "l_{1}")
    f.add_variable("l2", 0.0, "", "l_{2}")
    f.add_variable("Dн1", 0.0, "", "D_{н1}")
    f.add_variable("Dвт1", 0.0, "", "D_{вт1}")
    f.add_variable("Dн2", 0.0, "", "D_{н2}")
    f.add_variable("Dвт2", 0.0, "", "D_{вт2}")
    f.add_variable("rho1*", 0.0, "", "\\rho_{1}^{*}")
    f.add_variable("rho_ЛА*", 0.0, "", "\\rho_{ла}^{*}")
    f.add_variable("dr_вт", 0.0, "", "\Delta r_{вт}")
    f.add_variable("dr_н", 0.0, "", "\Delta r_{н}")


def print_calc_res(f):
    print("*********************************")
    print("length of blades (009):")
    print("         Dн1 = ", f.v["Dн1"])
    print("         Dвт1 = ", f.v["Dвт1"])
    print("         l1 = ", f.v["l1"])
    print("         rho1* = ", f.v["rho1*"])
    print("         rho_ЛА = ", f.v["rho_ЛА*"])
    print("         Dвт2 = ", f.v["Dвт2"])
    print("         Dн2 = ", f.v["Dн2"])
    print("         l2 = ", f.v["l2"])
    print("         dr_н = ", f.v["dr_н"])
    print("         dr_вт = ", f.v["dr_вт"])
    print("*********************************\n")


def calc_part(f):
    f.v["Dн1"] = f.v["Dн"]
    f.v["Dвт1"] = f.v["rвт"] * f.v["Dн1"]
    f.v["l1"] = (f.v["Dн1"] - f.v["Dвт1"]) / 2.0
    exp_ind = 1.0 - (f.v["k"] - 1.0) / (f.v["k"] * f.v["etaЛА"])
    f.v["rho1*"] = (f.v["p1*"]) / (f.v["R"] * f.v["TВ*"])
    f.v["rho_ЛА*"] = f.v["rho1*"] * pow((f.v["pЛА*"]) / (f.v["p1*"]), exp_ind)
    if f.v["тип проточной части"] == 1:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dн1"], 2.0) - h1)
            f.v["Dн2"] = f.v["Dн1"]
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_вт"] = f.v["Dвт2"] / f.v["Dн2"] - f.v["rвт"]
            f.v["dr_н"] = 0.0
    elif f.v["тип проточной части"] == 2:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = f.v["Dвт1"]
            f.v["Dн2"] = math.sqrt(pow(f.v["Dвт1"], 2.0) + h1)
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_н"] = (f.v["Dн2"] - f.v["Dвт2"]) / (f.v["Dвт2"])
            f.v["dr_вт"] = 0.0
    elif f.v["тип проточной части"] == 3:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dн1"], 2.0) - h1)
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dвт1"], 2.0) + h1)
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_н"] = (f.v["Dн2"] - f.v["Dвт2"]) / (f.v["Dвт2"])
            f.v["dr_вт"] = f.v["Dвт2"] / f.v["Dн2"] - f.v["rвт"]


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
