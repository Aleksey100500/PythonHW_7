from datetime import datetime


def div_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} / {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def div_log_ost(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} % {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def div_log_bez(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} // {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def mult_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} * {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def sub_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} - {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def sum_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} + {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def pow_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} ** {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def sqrt_log(r1, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} ** 0,5 = {} Time {}\n'.format(r1, result, time_calc))

def error_enter():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} Time {}\n'.format('Error.', time_calc))

def error_zero():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} Time {}\n'.format('Zero Error.', time_calc))

def start_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} Time {}\n'.format('Start work with app', time_calc))

def exit_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} Time {}\n'.format('Exit.', time_calc))