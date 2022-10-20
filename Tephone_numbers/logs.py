import datetime

def logs_csv(surname, name, tel_number, params):
    time_calc = datetime.datetime.now()
    with open('log_tel.csv', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; Time: {}\n'.format(surname, name, tel_number, params, time_calc))
    work_is_end = 'All in book.'
    return work_is_end

def logs_json(surname, name, tel_number, params):
    time_calc = datetime.datetime.now()
    with open('log_tel.json', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; Time: {}\n'.format(surname, name, tel_number, params, time_calc))
    work_is_end = 'All in book.'
    return work_is_end

def logs_xml(surname, name, tel_number, params):
    time_calc = datetime.datetime.now()
    with open('log_tel.xml', 'a') as log_file:
        log_file.write('{}; {}; {}; {}; Time: {}\n'.format(surname, name, tel_number, params, time_calc))
    work_is_end = 'All in book.'
    return work_is_end