import logg as lg
def get_complex_numbers():
    while True:
        a = input('Enter real part: ')
        if a == 0:
            lg.error_zero()
            print('Its zero try again.')
            get_complex_numbers()
        if not a.isdigit():
            print('Try again.')
            continue
        a = int(a)
        break
    while True:
        b = input('Enter imaginary number: ')
        if b == 0:
            lg.error_zero()
            print('Its zero try again.')
            get_complex_numbers()
        if not b.isdigit():
            print('Try again.')
            continue
        b = int(b)
        break
    return complex(a, b)