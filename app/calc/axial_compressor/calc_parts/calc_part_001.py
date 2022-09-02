def add_variables(f):
    f.add_variable("m", 65, "")
    f.add_variable("ПК*", 3.4, "")
    f.add_variable("pВ*", 98100, "")
    f.add_variable("TВ*", 280, "")
    f.add_variable("k", 1.4, "")
    f.add_variable("R", 287.1, "")
    f.add_variable("n", 3000, "")
    f.add_variable("тип привода", 0, "")
    f.add_variable("etaК", 0.9, "")
    f.add_variable("pi", 3.14159265359, "")
    '''
    f.add_variable("m", 62, "")
    f.add_variable("ПК*", 3.7, "")
    f.add_variable("pВ*", 98100, "")
    f.add_variable("TВ*", 293, "")
    f.add_variable("k", 1.4, "")
    f.add_variable("R", 287.1, "")
    f.add_variable("n", 3000, "")
    # тип привода 0 - электрический
    f.add_variable("тип привода", 0, "")
    f.add_variable("etaК", 0.86, "")
    f.add_variable("pi", 3.14159265359, "")
    '''
    '''
    f.add_variable("m", 75, "")
    f.add_variable("ПК*", 3.45, "")
    f.add_variable("pВ*", 98100, "")
    f.add_variable("TВ*", 293, "")
    f.add_variable("k", 1.4, "")
    f.add_variable("R", 287.1, "")
    f.add_variable("n", 3000, "")
    # тип привода 0 - электрический
    f.add_variable("тип привода", 0, "")
    f.add_variable("etaК", 0.86, "")
    f.add_variable("pi", 3.14159265359, "")
    '''


def print_calc_res(f):
    print("*********************************")
    print("initial data (001):")
    print("         m = ", f.v["m"])
    print("         ПК* = ", f.v["ПК*"])
    print("         pВ* = ", f.v["pВ*"])
    print("         TВ* = ", f.v["TВ*"])
    print("         k = ", f.v["k"])
    print("         R = ", f.v["R"])
    print("         n = ", f.v["n"])
    print("         etaК = ", f.v["etaК"])
    print("*********************************\n")


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    if is_print_res:
        print_calc_res(field)
