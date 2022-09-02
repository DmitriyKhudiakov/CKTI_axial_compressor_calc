

def img_path(f, var_name, i_d):
    return i_d + f.variable_dict[var_name].name_to_image_name() + ".png"


def name(f, var_name):
    return f.variable_dict[var_name].name


def get_setup(calc_name, f):
    i_d = "app\\calc\\" + calc_name + "\\source\\display_images\\"
    w_list = [[img_path(f, "m", i_d), "[кг/с] lim(30...150.0)", "", name(f, "m"), 30.0, 150.0],
              [img_path(f, "ПК*", i_d), "[-] lim(1.5...7.0)", "", name(f, "ПК*"), 1.5, 7.0],
              [img_path(f, "pВ*", i_d), "[Па] lim(95000.0...200000.0)", "", name(f, "pВ*"), 95000.0, 200000.0],
              [img_path(f, "TВ*", i_d), "[К] lim(250.0...350.0)", "", name(f, "TВ*"), 250.0, 350.0],
              [img_path(f, "k", i_d), "[-] lim(1.1...2.5)", "", name(f, "k"), 1.1, 2.5],
              [img_path(f, "R", i_d), "[Дж/(кг*К)] lim(50...500)", "", name(f, "R"), 50.0, 500.0],
              [img_path(f, "n", i_d), "[об/мин] lim(1000.0...10000.0)", "", name(f, "n"), 1000.0, 10000.0],
              [img_path(f, "etaК", i_d), "[м/с] lim(0.87...0.91)", "", name(f, "etaК"), 0.87, 0.91]]
    return w_list
