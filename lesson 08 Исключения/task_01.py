class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

def string_validation(line):
    name, email, age = line.split(' ')
    if name == None or email == None or age == None:
        raise ValueError("Строка не делится на имя, почту, возраст")
    if name.isalpha() == False:
        raise NotNameError('Имя содержит неразрешенные символы')
    if email.find('@') == -1 or email.find('.') == -1:
        raise NotEmailError('Email неверен')
    if age.isdigit():
        if  10 > int(age) or int(age) > 99:
            raise ValueError('Возраст не подходит')
    else:
        raise ValueError('Возраст не число')
    return True
    

with open('registrations.txt', 'r', encoding="utf-8") as ff:
    f_good = open('registrations_good.log','w', 1)
    f_bad = open('registrations_bad.log', 'w', 1)
    for i, line in enumerate(ff):
        line = line[:-1]
        try:
            if string_validation(line):
                f_good.write(line)
                f_good.write('\n')
        except (ValueError, NotEmailError, NotNameError) as err:
            f_bad.write(f'В строке {i} с содержимым "{line[:-1]}" ошибка "{err}"\n')
            print(f'В строке {i} с содержимым "{line[:-1]}" ошибка "{err}"')
f_good.close()
f_bad.close()