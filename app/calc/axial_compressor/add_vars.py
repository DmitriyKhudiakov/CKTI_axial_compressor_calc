

def step_2(f):
    f.add_variable("Rкр", None, "м", "R_{кр}")
    f.add_variable("lambda_R", None, "-", "lambda_{R}")
    f.add_variable("V_C1", None, "-", "V_{C1}")
    f.add_variable("V_A1", None, "-", "V_{A1}")
    f.add_variable("V_B1", None, "-", "V_{B1}")
    f.add_variable("V_D1", None, "-", "V_{D1}")
    f.add_variable("Sм", None, "м^2", "S_{м}")
    f.add_variable("S_11", None, "м^2", "S_{11}")


def add_variables(f):
    f.add_variable("m", None, "кг/c", "\overline{m}")
    f.add_variable("ПК*", None, "-", "\Pi_{к}^{*}")
    f.add_variable("pВ*", None, "Па", "p_{в}^{*}")
    f.add_variable("TВ*", None, "К", "T_{в}^{*}")
    f.add_variable("k", None, "-", "k")
    f.add_variable("R", None, "Дж/(кг*К)", "R")
    f.add_variable("n", None, "об/мин", "n")
    f.add_variable("etaК", None, "-", "\eta_{к}")
    f.add_variable("тип привода", 0, "-", "тип привода")
    f.add_variable("pi", 3.14159265359, "-", "\pi")





