"""Напишите функцию, которая возводит число в положительную степень с помощью рекурсии. 
В качестве аргументов подаются целые положительные числа n (число) и m (степень)."""

def minus_degree_of_number(n, m):
    if m >= 1:
        result_prev = minus_degree_of_number(n, m-1)
        result = (1/n) * result_prev
    else:
        result = 1
    return(result)


num = int(input('Число: '))
m = int(input('степень: '))
print('Полученное число:', minus_degree_of_number(num, m))
