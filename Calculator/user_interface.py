import model_sum as s
import except_num as ex
import model_sub as smi
import model_mult as mu
import model_pow as po
import model_sqrt as sq
import model_div as d
import compl as com
import logg as lg

def user_enter():
    print('Calculator Wolcomes You!\n\n')
    while True:
        interface_type_number()
        vibor = ex.get_number()
        if vibor == 1:
            interface_rational()
        elif vibor == 2:
            interface_complex()
        else:
            lg.exit_app()
            exit()


def interface_rational():
    interface_operations()
    vibor_1 = int(ex.get_number())
    if vibor_1 == 1:
        a = ex.get_number()
        b = ex.get_number()
        result = s.sum(a, b)
        print(result)
        lg.sum_log(a, b, result)
    elif vibor_1 == 2:
        a = ex.get_number()
        b = ex.get_number()
        result = smi.sub(a, b)
        print(result)
        lg.sub_log(a, b, result)
    elif vibor_1 == 3:
        a = ex.get_number()
        b = ex.get_number()
        result = mu.mult(a, b)
        print(result)
        lg.mult_log(a, b, result)
    elif vibor_1 == 4:
        interface_operations_div()
        vibor_2 = ex.get_number()
        if vibor_2 == 1:
            a = ex.zero_except()
            b = ex.zero_except()
            result = d.div_del(a, b)
            print(result)
            lg.div_log(a, b, result)
        elif vibor_2 == 2:
            a = ex.zero_except()
            b = ex.zero_except()
            result = d.div_ost(a, b)
            print(result)
            lg.div_log_ost(a, b, result)
        elif vibor_2 == 3:
            a = ex.zero_except()
            b = ex.zero_except()
            result = d.div_bez(a, b)
            print(result)
            lg.div_log_bez(a, b, result)
    elif vibor_1 == 5:
        a = ex.get_number()
        b = ex.get_number()
        result = po.pow(a, b)
        print(result)
        lg.pow_log(a, b, result)
    elif vibor_1 == 6:
        a = ex.get_number()
        result = sq.sqrt_math(a)
        print(result)
        lg.sqrt_log(a, result)
    elif vibor_1 == 0:
        user_enter()
    else:
        print('Not bad. Try again.')
        lg.error_enter()
        interface_rational()


def interface_type_number():
    main_menu_list = '1 - rational', '2 - complex'
    print('Working with:')
    for i in main_menu_list:
        print(i)
    print('0 - exit')


def interface_operations():
    print('Operations: ')
    operations_number = range(1, 7)
    operations_menu = 'sum', 'sub', 'mul', 'div', 'pow', 'sqrt'
    for i in operations_number:
        print(f'{i} - {operations_menu[i - 1]}')
    print('0 - previous menu')


def interface_operations_div():
    print('Operations: ')
    operations_div_menu = '1 - "/"', '2 - "%"', '3 - "//"'
    for i in operations_div_menu:
        print(i)

def interface_operations_div_f_com():
    print('Operations: ')
    print('1 - /')

def interface_complex():
    interface_operations()
    vibor_1 = int(ex.get_number())
    if vibor_1 == 1:
        a = com.get_complex_numbers()
        b = com.get_complex_numbers()
        result = s.sum(a, b)
        print(result)
        lg.sum_log(a, b, result)
    elif vibor_1 == 2:
        a = com.get_complex_numbers()
        b = com.get_number()
        result = smi.sub(a, b)
        print(result)
        lg.sub_log(a, b, result)
    elif vibor_1 == 3:
        a = com.get_complex_numbers()
        b = com.get_complex_numbers()
        result = mu.mult(a, b)
        print(result)
        lg.mult_log(a, b, result)
    elif vibor_1 == 4:
        interface_operations_div_f_com()
        vibor_2 = ex.get_number()
        if vibor_2 == 1:
            a = com.get_complex_numbers()
            b = com.get_complex_numbers()
            result = d.div_del(a, b)
            print(result)
            lg.div_log(a, b, result)
            user_enter()
    elif vibor_1 == 5:
        a = com.get_complex_numbers()
        b = com.get_complex_numbers()
        result = po.pow(a, b)
        print(result)
        lg.pow_log(a, b, result)
    elif vibor_1 == 6:
        a = com.get_complex_numbers()
        result = sq.sqrt_cmath(a)
        print(result)
        lg.sqrt_log(a, result)
    elif vibor_1 == 0:
        user_enter()
    else:
        print('Not bad. Try again.')
        lg.error_enter()
        interface_rational()
user_enter()