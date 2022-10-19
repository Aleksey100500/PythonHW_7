import logg as lg

def get_number():
    number = input('Enter a number: ')
    try:
        number = float(number)
        print('Its OK.')
        return number
    except ValueError:
        print('Its not a number. Try again.')
        lg.error_enter()
        return get_number()


def zero_except():
    number = input('Enter a number: ')
    number = float(number)    
    if number == 0:
        print('Its a zero. Try again.')
        lg.error_zero()
        return zero_except()
    print('Its OK.')
    return number