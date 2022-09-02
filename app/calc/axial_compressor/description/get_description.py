import os
import glob
import pathlib


def param_img(s_val, calc_name):
    str_replace = "<img src=\"app/calc/" + calc_name + "/source/description_images/" + s_val + ".png\">"
    return str_replace


def param_img_create(s_val, calc_name):
    s_val = s_val.strip()
    s_val = s_val.split(";")
    path = "app\\calc\\" + calc_name + "\\source\\description_images\\" + s_val[1].strip()
    is_exist = False
    if len(glob.glob(path + ".png")) > 0:
        is_exist = True
    if is_exist is False:
        import app.calc.scripts.formula as formula
        formula.create_formula(formula=s_val[0], font_size=14, path=path)
    s_val_str = s_val[1].strip()
    return param_img(s_val_str.strip(), calc_name)


def sub(data, calc_name):
    while True:
        f_start = data.find("[[")
        f_end = data.find("]]")+2
        if (f_start != -1) and (f_end != -1):
            s_tag = data[f_start+2:f_end-2]
            param = s_tag[:s_tag.find("=")].strip()
            s_val = s_tag[s_tag.find("=")+1:]
            if param == "img":
                data = data.replace(data[f_start:f_end], param_img(s_val, calc_name))
            elif param == "img_create":
                data = data.replace(data[f_start:f_end], param_img_create(s_val, calc_name))
        else:
            break
    return data


def get_description(calc_name):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(str(pathlib.Path().absolute()) + "\\app\\calc\\axial_compressor\\description\\source\\description.html",
              encoding="utf-8") as file:
        data = file.read().replace('\n', '')
    data = sub(data, calc_name)
    return data
