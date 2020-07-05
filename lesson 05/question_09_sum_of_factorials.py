"""Напишите программу, которая на вход получает число n и считает по нему сумму 1!+2!+3!+...+n!"""
def sum_of_factorials(number):
    """Функция считает сумму факториалов элементов ряда 1!+2!+3!+...+n!"""
    summa = 0
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
        summa += factorial
    return summa

num = int(input('Введите число:'))
print('Сумма факториалов ряда:', sum_of_factorials(num))
