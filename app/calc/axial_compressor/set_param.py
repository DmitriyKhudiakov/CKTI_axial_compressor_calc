

def is_float(str_read):
    try:
        float(str_read)
        return True
    except ValueError:
        return False


def set_vars(f, setup_list, enter_list):
    is_ok = True
    ret_list = []
    for s_l, e_l in zip(setup_list, enter_list):
        str_read = e_l
        is_right = is_float(str_read)
        if is_right is True:
            val = float(str_read)
            if (val >= s_l[4]) and (val <= s_l[5]):
                f.v[s_l[3]] = val
                ret_list.append("ok")
            else:
                is_ok = False
                ret_list.append("Ошибка: значение не попадает в допустимый диапазон")
        else:
            is_ok = False
            ret_list.append("Ошибка: Неверный формат ввода")
    return ret_list, is_ok


def set_var_vars(f, setup_list, enter_list):
    is_ok = True
    ret_list = []
    for s_l, e_l in zip(setup_list, enter_list):
        curr_ret_list = []
        for i in range(3):
            str_read = e_l[i]
            is_right = is_float(str_read)
            if is_right is True:
                val = float(str_read)
                if (val >= s_l[8+i][0]) and (val <= s_l[8+i][1]):
                    f.v[s_l[7]] = val
                    curr_ret_list.append("ok")
                else:
                    is_ok = False
                    curr_ret_list.append("Ошибка: значение не попадает в допустимый диапазон")
            else:
                is_ok = False
                curr_ret_list.append("Ошибка: Неверный формат ввода")
        ret_list.append(curr_ret_list)
    return ret_list, is_ok
