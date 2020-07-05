# Напишите программу, которая на вход получает целое число больше 2 и выводит по нему его наименьший натуральный
# делитель, отличный от 1.

def find_smallest_natural_divisor(number):
    """ Возвращает наименьший натуральный делитель """
    for i in range(2, number + 1):
        if number % i == 0:
            return i


# print(find_smallest_natural_divisor(9))
num = int(input('Введите число:'))
print('Наименьший натуральный делитель числа', num, '-', find_smallest_natural_divisor(num))
