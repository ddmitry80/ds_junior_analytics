# Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.

def is_simple_number(number):
    """ Возвращает True если number простое """
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


# print(is_simple_number(2))
num = int(input('Введите число:'))
if not is_simple_number(num):
    print('Данное число составное')
else:
    print('Данное число простое')