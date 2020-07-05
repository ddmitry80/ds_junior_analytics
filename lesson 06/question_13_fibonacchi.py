"""Напишите функцию, которая находит число Фиббоначи по его номеру. В качестве аргумента 
подается целое положительное число n (число)."""

def fibonacci(n):
    num0 = 0
    num1 = 1
    num2 = 1
    if n == 1:
        return(0)
    if n == 2:
        return(1)
    for _ in range(3,n):
        num0, num1, num2 = num1, num2, num1 + num2
    return(num2)


num = int(input('Укажите номер нужного числа Фибоначчи: '))
print('Нужное Вам число:', fibonacci(num))