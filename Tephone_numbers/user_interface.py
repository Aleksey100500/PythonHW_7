import logs as write_its
import sys

def user_interfase_tel():
    surname = user_surnames()
    name = user_names()
    tel = user_telephone()
    dis = user_description()
    number = chose_your_type_file()
    if number == 0:
        sys.exit('End.')
    elif number == 1:
        write_its.logs_csv(surname, name, tel, dis)
    elif number == 2:
        write_its.logs_json(surname, name, tel, dis)
    micro_lib = {
        '1': f"{write_its.logs_csv(surname, name, tel, dis)}",
        '2': f"{write_its.logs_json(surname, name, tel, dis)}",
        '3': f"{write_its.logs_xml(surname, name, tel, dis)}"
    }
    micro_lib.get[number]

    
    
    
def user_surnames():
    surname = (input('Enter a surname: ')).lower()
    return surname.title()

def user_names():
    name = (input('Enter a name: ')).lower()
    return name.title()

def user_telephone():
    tel_number = (
        input('Enter a telephon number (+/code_operator/tel_number): '))
    return tel_number

def user_description():
    us_des = (input('Enter any descriptions: '))
    return us_des

def chose_your_type_file():
    number = int(input('How safe your file in format(CSV - 1, JSON - 2, XML - 3, exit - 0): '))
    return number

user_interfase_tel()