"""Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую на 5 минут больше, 
чем предыдущую. Напишите программу, которая запрашивает сколько стен было в квартире под поклейку, а также 
время работы с первой стеной. Программа должна выводить, сколько часов рабочие потратили на поклейку 
обоев во всей квартире. Ответом должно быть целое число. """

first_wall_time = int(input('За сколько минут поклеили первую стену: '))
wall_number = int(input('Сколько стен в квартире: '))
#first_wall_time = 20
#wall_number = 10
time_minutes = 0

for i in range(0,wall_number): # считаем потраченное время в минутах
    time_minutes += first_wall_time + i*5

# переводим в часы
hours = time_minutes // 60
if time_minutes % 60 != 0:
    hours += 1

print('На работу потрачено', hours, 'часов')
