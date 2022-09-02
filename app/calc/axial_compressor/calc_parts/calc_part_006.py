def add_variables(f):
    # 1 - phi = const, 2 - phi = decrease, 3 - phi = variable
    f.add_variable("закон phi*", 0, "", "закон \phi^{*}")
    # 1 - (Dн=const, Dвт!=const), 2 - (Dн!=const, Dвт=const), 3 - (Dн!=const, Dвт!=const)
    f.add_variable("тип проточной части", 0, "", "тип проточной части")


def print_calc_res(f):
    print("*********************************")
    print("phi distribution law and type of flow path(006):")
    print("         закон phi* - тип ", f.v["закон phi*"])
    print("         тип проточной части - тип ", f.v["тип проточной части"])
    print("*********************************\n")


def calc_part(f):
    f.v["закон phi*"] = 1
    f.v["тип проточной части"] = 1


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
