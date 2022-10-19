def get_complex_numbers():
    while True:
        a = input('Enter real part: ')
        if not a.isdigit():
            print('Try again.')
            continue
        a = int(a)
        break
    while True:
        b = input('Enter imaginary number: ')
        if not b.isdigit():
            print('Try again.')
            continue
        b = int(b)
        break
    return complex(a, b)