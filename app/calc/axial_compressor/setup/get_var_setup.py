

def img_path(f, var_name, i_d):
    return i_d + f.variable_dict[var_name].name_to_image_name() + ".png"


def name(f, var_name):
    return f.variable_dict[var_name].name


def get_var_setup(calc_name, f):
    i_d = "app\\calc\\" + calc_name + "\\source\\display_images\\"
    w_list = [[img_path(f, "m_расход", i_d),
               "[кг/c] lim_1(10.0...500.0)", "",
               "[кг/c] lim_2(10.0...500.0)", "",
               "[-] n_iter(2...100)", "",
               name(f, "m_расход"),
               (10.0, 500.0), (10.0, 500.0), (2.0, 100.0),
               "массовый расход"],
              [img_path(f, "m_ст_двух", i_d),
               "[кг/c] lim_1(2.0...10.0)", "",
               "[кг/c] lim_2(2.0...10.0)", "",
               "[-] n_iter(2...100)", "",
               name(f, "m_ст_двух"),
               (2.0, 10.0), (2.0, 10.0), (2.0, 100.0),
               "степень двухконтурности"]
              ]
    w_list = []
    return w_list
