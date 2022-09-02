def add_variables(f):
    f.add_variable("p1*", 0.0, "", "p_{1}^{*}")
    f.add_variable("pЛА*", 0.0, "", "p_{ла}^{*}")
    f.add_variable("ПЛА*", 0.0, "", "\Pi_{ла}^{*}")
    f.add_variable("HЛА*", 0.0, "", "H_{ла}^{*}")


def print_calc_res(f):
    print("*********************************")
    print("adiabatic head in the blade row (003):")
    print("         p1* = ", f.v["p1*"])
    print("         pЛА* = ", f.v["pЛА*"])
    print("         ПЛА* = ", f.v["ПЛА*"])
    print("         HЛА* = ", f.v["HЛА*"])
    print("*********************************\n")


def calc_part(f):
    f.v["p1*"] = f.v["pВ*"] - f.v["dpВ*"]
    f.v["pЛА*"] = f.v["pК*"] + f.v["dpК*"]
    f.v["ПЛА*"] = f.v["pЛА*"] / f.v["p1*"]
    f.v["HЛА*"] = (f.v["k"] / (f.v["k"] - 1.0)) * f.v["R"] * f.v["TВ*"] * (pow(f.v["ПЛА*"], (f.v["k"] - 1.0) / f.v["k"]) - 1.0)


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
