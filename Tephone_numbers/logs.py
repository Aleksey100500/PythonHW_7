import datetime as time

def logs_csv(surname, name, tel_number, params):
    time_calc = time.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; \n Time: {}'.format(surname, name, tel_number, params, time_calc))

def logs_json(surname, name, tel_number, params):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.json', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; \n Time: {}'.format(surname, name, tel_number, params, time_calc))

def logs_xml(surname, name, tel_number, params):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.xml', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; \n Time: {}'.format(surname, name, tel_number, params, time_calc))