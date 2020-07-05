"""Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n²"""
def sum_of_suares(number):
    """Функция считает сумму квадратов элементов ряда 1²+2²+3²+...+n²"""
    summa = 0
    for i in range(1,number+1):
        summa += i**2
    return summa

num = int(input('Введите число:'))
print('Сумма квадратов ряда:', sum_of_suares(num))
