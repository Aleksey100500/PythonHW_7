def get_number():
    number = input('Enter a number: ')
    try:
        number = float(number)
        print('Its OK.')
        return number
    except ValueError:
        print('Its not a number. Try again.')
        return get_number()