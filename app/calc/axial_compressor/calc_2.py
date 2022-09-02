from .calc_parts.calc_part_011 import calc_part as cp11
from .calc_parts.calc_part_011 import add_variables as av11
from .calc_parts.calc_part_012 import calc_part as cp12
from .calc_parts.calc_part_012 import add_variables as av12


def set_nv_variables(f, nv):
    f.v["phi1"] = f.v["phi1" + str(nv)]
    f.v["rвт"] = f.v["rвт" + str(nv)]
    f.v["Dн"] = f.v["Dн" + str(nv)]
    f.v["uн"] = f.v["uн" + str(nv)]
    f.v["Dн_посл"] = f.v["Dн_посл" + str(nv)]
    f.v["eta_посл"] = f.v["eta_посл" + str(nv)]
    f.v["psi_посл"] = f.v["psi_посл" + str(nv)]
    f.v["OmegaТ"] = f.v["OmegaТ" + str(nv)]
    f.v["etaСТ"] = f.v["etaСТ" + str(nv)]
    f.v["psi"] = f.v["psi" + str(nv)]
    f.v["тип ступени"] = f.v["тип ступени" + str(nv)]
    f.v["закон phi*"] = f.v["закон phi*" + str(nv)]
    f.v["тип проточной части"] = f.v["тип проточной части" + str(nv)]
    f.v["Hср_ст*"] = f.v["Hср_ст*" + str(nv)]
    f.v["HрЛА*"] = f.v["HрЛА*" + str(nv)]
    f.v["alpha"] = f.v["alpha" + str(nv)]
    f.v["i"] = f.v["i" + str(nv)]
    f.v["i_int"] = f.v["i_int" + str(nv)]
    f.v["etaЛА"] = f.v["etaЛА" + str(nv)]
    f.v["a_help"] = f.v["a_help" + str(nv)]
    f.v["l1"] = f.v["l1" + str(nv)]
    f.v["l2"] = f.v["l2" + str(nv)]
    f.v["Dн1"] = f.v["Dн1" + str(nv)]
    f.v["Dвт1"] = f.v["Dвт1" + str(nv)]
    f.v["Dн2"] = f.v["Dн2" + str(nv)]
    f.v["Dвт2"] = f.v["Dвт2" + str(nv)]
    f.v["rho1*"] = f.v["rho1*" + str(nv)]
    f.v["rho_ЛА*"] = f.v["rho_ЛА*" + str(nv)]
    f.v["dr_вт"] = f.v["dr_вт" + str(nv)]
    f.v["dr_н"] = f.v["dr_н" + str(nv)]
    f.v["rвт2_rel"] = f.v["rвт2_rel" + str(nv)]


def calc(f, is_init_vars, calc_name, nv):
    set_nv_variables(f, nv)
    if is_init_vars is False:
        av11(f)
    cp11(f)
    if is_init_vars is False:
        av12(f)
    cp12(f, False)
    if is_init_vars is False:
        is_init_vars = True
    return is_init_vars
