"""Будем считать, что кубик может иметь неограниченное количество граней (натуральное число). 
Напишите программу, которая запрашивает, сколько граней имеется у двух разных кубиков. 
Затем выводит все возможные комбинации результатов бросков двух таких кубиков."""

cube1_faces = int(input('Введите число граней первого кубика: '))
cube2_faces = int(input('Введите число граней второго кубика: '))
#cube1_faces = 2
#cube2_faces = 3

combinations = 0
for i in range(0, cube1_faces):
    for j in range(0, cube2_faces):
        combinations += 1
        print('Грань первого кубика -', i+1, ', грань второго кубика -', j+1)

print('Всего', combinations, 'комбинаций бросков для двух кубиков с', cube1_faces,'и' , cube2_faces, 'гранями')