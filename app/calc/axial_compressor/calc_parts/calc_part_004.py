def add_variables(f):
    f.add_variable("phi1", 0.0, "", "\\varphi_{1}")
    f.add_variable("rвт", 0.0, "", "r_{вт}")
    f.add_variable("Dн", 0.0, "", "D_{н}")
    f.add_variable("uн", 0.0, "", "u_{н}")
    # for next parts
    f.add_variable("Dн_посл", None, "", "D_{н.посл}")
    f.add_variable("eta_посл", None, "", "\eta_{посл}")
    f.add_variable("psi_посл", None, "", "\psi_{посл}")


def print_calc_res(f):
    print("*********************************")
    print("outer diameter and peripheral speed (004):")
    print("         phi1 = ", f.v["phi1"])
    print("         rвт = ", f.v["rвт"])
    print("         Dн = ", f.v["Dн"])
    print("         uн = ", f.v["uн"])
    print("*********************************\n")


def calc_part(f):
    f.v["phi1"] = 0.47
    f.v["rвт"] = 0.6
    h_var1 = f.v["m"] * f.v["R"] * f.v["TВ*"]
    h_var2 = (1.0 - pow(f.v["rвт"], 2.0)) * f.v["p1*"] * f.v["n"] * f.v["phi1"]
    f.v["Dн"] = 2.9 * pow(h_var1 / h_var2, 1.0 / 3.0)
    f.v["uн"] = f.v["pi"] * f.v["Dн"] * f.v["n"] / 60.0


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
