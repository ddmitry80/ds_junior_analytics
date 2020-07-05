max_num = int(input('введите число или 0 чтобы закончить:'))
prev_num = max_num
num2 = max_num
while num2 != 0:
    num2 = int(input('введите число или 0 чтобы закончить:'))
    if num2 > max_num:
        prev_num = max_num
        max_num = num2
    if num2 > prev_num and num2 < max_num:
        prev_num = num2
print('Второе по величине значение:', prev_num)
