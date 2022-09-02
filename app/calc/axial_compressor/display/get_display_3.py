# -*- coding: utf-8 -*-
import os
import glob
import pathlib


def param_img(s_val, calc_name, is_save):
    if is_save is True:
        str_replace = "<img src=\"source/display_images/" + s_val + ".png\">"
    else:
        str_replace = "<img src=\"app/calc/" + str(calc_name) + "/source/display_images/" + s_val + ".png\">"
    return str_replace


def param_img_create(s_val, calc_name, is_save):
    s_val = s_val.strip()
    s_val = s_val.split(";")
    path = "app\\calc\\" + calc_name + "\\source\\display_images\\" + s_val[1].strip()
    is_exist = False
    if len(glob.glob(path + ".png")) > 0:
        is_exist = True
    if is_exist is False:
        import app.calc.scripts.formula as formula
        formula.create_formula(formula=s_val[0], font_size=s_val[2], path=path)
    s_val_str = s_val[1].strip()
    return param_img(s_val_str.strip(), calc_name, is_save)


def param_var(s_val, f):
    if str(round(f.v[str(s_val)], 3)) != "0.000":
        str_replace = str(round(f.v[str(s_val)], 3))
    else:
        str_replace = str(round(f.v[str(s_val)], 6))
    return str_replace


def param_var_image(s_val, f, calc_name, is_save):
    image_name = f.variable_dict[str(s_val)].image_name
    path = "app\\calc\\" + calc_name + "\\source\\display_images\\" + image_name
    is_exist = False
    if len(glob.glob(path + ".png")) > 0:
        is_exist = True
    if is_exist is False:
        import app.calc.scripts.formula as formula
        formula.create_formula(formula=str(f.tex_name[str(s_val)]), font_size=14, path=path)
    # s_val_str = str(f.id_num[str(s_val)])
    s_val_str = image_name
    return param_img(s_val_str.strip(), calc_name, is_save)


def param_type_st(f):
    if f.v["тип ступени"] == 1:
        str_replace = "K-50-1"
    elif f.v["тип ступени"] == 2:
        str_replace = "K-50-5"
    elif f.v["тип ступени"] == 3:
        str_replace = "K-70-17"
    elif f.v["тип ступени"] == 4:
        str_replace = "K-100-2l"
    else:
        str_replace = ""
    return str_replace


def param_law_flow_path(f):
    if f.v["закон phi*"] == 1:
        str_replace = "const"
    elif f.v["закон phi*"] == 2:
        str_replace = "decrease"
    elif f.v["закон phi*"] == 3:
        str_replace = "variable"
    else:
        str_replace = ""
    return str_replace


def param_type_flow_path(f):
    if f.v["тип проточной части"] == 1:
        str_replace = "(Dн=const, Dвт!=const)"
    elif f.v["тип проточной части"] == 2:
        str_replace = "(Dн!=const, Dвт=const)"
    elif f.v["тип проточной части"] == 3:
        str_replace = "(Dн!=const, Dвт!=const)"
    else:
        str_replace = ""
    return str_replace


def add_str_table_var(f, str_name, nv):
    return "<th>" + str(round(f.v[str_name + str(nv)], 4)) + "</th>"


def param_table_geom_1(f):
    str_replace = ""
    for i in range(1, f.v["i_int"] + 1):
        str_replace += "<tr>"
        str_replace += "<th><p1>" + str(i) + "</p1></th>"
        str_replace += add_str_table_var(f, "r_вт_rel", i)
        str_replace += add_str_table_var(f, "rн_rel", i)
        str_replace += add_str_table_var(f, "rср_rel", i)
        str_replace += "<th>" + str(round(f.v["b_k"], 4)) + "</th>"
        str_replace += add_str_table_var(f, "az1вт", i)
        str_replace += add_str_table_var(f, "az1н", i)
        str_replace += add_str_table_var(f, "az1ср", i)
        str_replace += add_str_table_var(f, "az2вт", i)
        str_replace += add_str_table_var(f, "az2н", i)
        str_replace += add_str_table_var(f, "az2ср", i)
        str_replace += add_str_table_var(f, "az3вт", i)
        str_replace += add_str_table_var(f, "az3н", i)
        str_replace += add_str_table_var(f, "az3ср", i)
        str_replace += add_str_table_var(f, "az4вт", i)
        str_replace += add_str_table_var(f, "az4н", i)
        str_replace += add_str_table_var(f, "az4ср", i)
        str_replace += add_str_table_var(f, "bz1вт", i)
        str_replace += add_str_table_var(f, "bz1н", i)
        str_replace += add_str_table_var(f, "bz1ср", i)
        str_replace += add_str_table_var(f, "bz2вт", i)
        str_replace += add_str_table_var(f, "bz2н", i)
        str_replace += add_str_table_var(f, "bz2ср", i)
        str_replace += add_str_table_var(f, "bz3вт", i)
        str_replace += add_str_table_var(f, "bz3н", i)
        str_replace += add_str_table_var(f, "bz3ср", i)
        str_replace += add_str_table_var(f, "bz4вт", i)
        str_replace += add_str_table_var(f, "bz4н", i)
        str_replace += add_str_table_var(f, "bz4ср", i)
        str_replace += "</tr>"
    return str_replace


def param_table_geom_2(f):
    str_replace = ""
    for i in range(1, f.v["i_int"] + 1):
        str_replace += "<tr>"
        str_replace += "<th><p1>" + str(i) + "</p1></th>"
        str_replace += add_str_table_var(f, "Sr1", i)
        str_replace += add_str_table_var(f, "Sr2", i)
        str_replace += add_str_table_var(f, "Sr3", i)
        str_replace += add_str_table_var(f, "Sr4", i)
        str_replace += add_str_table_var(f, "Sz1", i)
        str_replace += add_str_table_var(f, "Sz2", i)
        str_replace += add_str_table_var(f, "Sz3", i)
        str_replace += add_str_table_var(f, "Sz4", i)
        str_replace += "</tr>"
    return str_replace


def param_table_coeff(f):
    str_replace = ""
    for i in range(1, f.v["i_int"] + 1):
        str_replace += "<tr>"
        str_replace += "<th><p1>" + str(i) + "</p1></th>"
        str_replace += add_str_table_var(f, "D_р", i)
        str_replace += add_str_table_var(f, "b", i)
        str_replace += add_str_table_var(f, "bD_р", i)
        str_replace += add_str_table_var(f, "l_", i)
        str_replace += add_str_table_var(f, "l_rel", i)
        str_replace += add_str_table_var(f, "Sr", i)
        str_replace += add_str_table_var(f, "Sr_rel", i)
        str_replace += add_str_table_var(f, "k_psi_зl", i)
        str_replace += add_str_table_var(f, "k_eta_зl", i)
        str_replace += add_str_table_var(f, "k_psi_z", i)
        str_replace += add_str_table_var(f, "k_eta_z", i)
        str_replace += add_str_table_var(f, "k_psi_м", i)
        str_replace += add_str_table_var(f, "k_eta_м", i)
        str_replace += add_str_table_var(f, "D_н", i)
        str_replace += add_str_table_var(f, "drн_rel", i)
        str_replace += add_str_table_var(f, "D_вт", i)
        str_replace += add_str_table_var(f, "drвт_rel", i)
        str_replace += add_str_table_var(f, "k_eta_dr_вт", i)
        str_replace += add_str_table_var(f, "k_eta_dr_н", i)
        str_replace += add_str_table_var(f, "k_eta_dr", i)
        str_replace += add_str_table_var(f, "k_eta", i)
        str_replace += add_str_table_var(f, "k_psi", i)
        str_replace += "</tr>"
    return str_replace


def param_table_second_st(f):
    str_replace = ""
    for i in range(1, f.v["i_int"] + 1):
        str_replace += "<tr>"
        str_replace += "<th><p1>" + str(i) + "</p1></th>"
        str_replace += add_str_table_var(f, "p*", i)
        str_replace += add_str_table_var(f, "T*", i)
        str_replace += add_str_table_var(f, "rho*", i)
        str_replace += add_str_table_var(f, "F_", i)
        str_replace += add_str_table_var(f, "cz*", i)
        str_replace += add_str_table_var(f, "phi*", i)
        str_replace += add_str_table_var(f, "uр'", i)
        str_replace += add_str_table_var(f, "psi", i)
        str_replace += add_str_table_var(f, "eta", i)
        str_replace += add_str_table_var(f, "k_psi_dr_вт", i)
        str_replace += add_str_table_var(f, "k_psi_dr_н", i)
        str_replace += add_str_table_var(f, "k_psi_dr", i)
        str_replace += add_str_table_var(f, "k_psi'", i)
        str_replace += add_str_table_var(f, "k_psi", i)
        str_replace += add_str_table_var(f, "k_eta", i)
        str_replace += add_str_table_var(f, "psi_р", i)
        str_replace += add_str_table_var(f, "eta_р", i)
        str_replace += add_str_table_var(f, "H*", i)
        str_replace += add_str_table_var(f, "dTад*", i)
        str_replace += add_str_table_var(f, "dT*", i)
        str_replace += add_str_table_var(f, "П*", i)
        str_replace += add_str_table_var(f, "p_з*", i)
        str_replace += add_str_table_var(f, "T_з*", i)
        str_replace += "</tr>"
    return str_replace


def sub(data, calc_name, f, is_save):
    while True:
        f_start = data.find("{{")
        f_end = data.find("}}")+2
        if (f_start != -1) and (f_end != -1):
            s_tag = data[f_start+2:f_end-2]
            param = s_tag[:s_tag.find("=")].strip()
            s_val = s_tag[s_tag.find("=")+1:].strip()
            if param == "var":
                data = data.replace(data[f_start:f_end], param_var(s_val, f))
        else:
            break
    while True:
        f_start = data.find("[[")
        f_end = data.find("]]")+2
        if (f_start != -1) and (f_end != -1):
            s_tag = data[f_start+2:f_end-2]
            param = s_tag[:s_tag.find("=")].strip()
            s_val = s_tag[s_tag.find("=")+1:].strip()
            if param == "var":
                data = data.replace(data[f_start:f_end], param_var(s_val, f))
            elif param == "img_create":
                data = data.replace(data[f_start:f_end], param_img_create(s_val, calc_name, is_save))
            elif param == "img":
                data = data.replace(data[f_start:f_end], param_img(s_val, calc_name, is_save))
            elif param == "var_image":
                data = data.replace(data[f_start:f_end], param_var_image(s_val, f, calc_name, is_save))
            elif param == "type_st":
                data = data.replace(data[f_start:f_end], param_type_st(f))
            elif param == "law_flow_path":
                data = data.replace(data[f_start:f_end], param_law_flow_path(f))
            elif param == "type_flow_path":
                data = data.replace(data[f_start:f_end], param_type_flow_path(f))
            elif param == "table_geom_1":
                data = data.replace(data[f_start:f_end], param_table_geom_1(f))
            elif param == "table_geom_2":
                data = data.replace(data[f_start:f_end], param_table_geom_2(f))
            elif param == "table_coeff":
                data = data.replace(data[f_start:f_end], param_table_coeff(f))
            elif param == "table_second_st":
                data = data.replace(data[f_start:f_end], param_table_second_st(f))
        else:
            break
    return data


def get_display(calc_name, f, display_file_name):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\display\\source\\" + display_file_name, encoding="utf-8") as file:
        data = file.read().replace('\n', '')
    data = sub(data, calc_name, f, False)
    return data


def get_data(calc_name, f, display_file_name, is_empty):
    if is_empty is True:
        return ""
    else:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\display\\source\\" + display_file_name, encoding="utf-8") as file:
            data = file.read().replace('\n', '')
        return sub(data, calc_name, f, True)