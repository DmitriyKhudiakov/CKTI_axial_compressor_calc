def add_variables(f):
    f.add_variable("rhoВ*", 0.0, "", "\\rho_{в}^{*}")
    f.add_variable("c1", 0.0, "", "c_{1}")
    f.add_variable("zetaВ", 0.0, "", "\zeta_{в}")
    f.add_variable("dpВ*", 0.0, "", "\Delta p_{в}^{*}")
    f.add_variable("rhoК*", 0.0, "", "\\rho_{к}^{*}")
    f.add_variable("pК*", 0.0, "", "p_{к}^{*}")
    f.add_variable("TК*", 0.0, "", "T_{к}^{*}")
    f.add_variable("cЛА", 0.0, "", "c_{ла}")
    f.add_variable("zetaК", 0.0, "", "\zeta_{к}")
    f.add_variable("dpК*", 0.0, "", "\Delta p_{к}^{*}")


def print_calc_res(f):
    print("*********************************")
    print("pressure loss in the pipes (002):")
    print("         zetaВ = ", f.v["zetaВ"])
    print("         rhoВ* = ", f.v["rhoВ*"])
    print("         c1 = ", f.v["c1"])
    print("         dpВ* = ", f.v["dpВ*"])
    print("         zetaК = ", f.v["zetaК"])
    print("         pК* = ", f.v["pК*"])
    print("         TК* = ", f.v["TК*"])
    print("         rhoК* = ", f.v["rhoК*"])
    print("         cЛА = ", f.v["cЛА"])
    print("         dpК* = ", f.v["dpК*"])
    print("*********************************\n")


def calc_part(f):
    f.v["zetaВ"] = 0.15
    f.v["rhoВ*"] = f.v["pВ*"] / (f.v["R"] * f.v["TВ*"])
    f.v["c1"] = 105.0
    f.v["dpВ*"] = f.v["zetaВ"] * f.v["rhoВ*"] * pow(f.v["c1"], 2.0) / 2.0
    f.v["zetaК"] = 0.525
    f.v["pК*"] = f.v["pВ*"] * f.v["ПК*"]
    f.v["TК*"] = f.v["TВ*"] * (1.0 + (pow(f.v["ПК*"], (f.v["k"] - 1) / (f.v["k"])) - 1.0) / (f.v["etaК"]))
    f.v["rhoК*"] = f.v["pК*"] / (f.v["R"] * f.v["TК*"])
    f.v["cЛА"] = 105.0
    f.v["dpК*"] = f.v["zetaК"] * f.v["rhoВ*"] * pow(f.v["cЛА"], 2.0) / 2.0


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
