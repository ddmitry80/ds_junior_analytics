"""Напишите программу, которая запрашивает у пользователя сторону квадрата и символ, а затем 
рисует этот символ по диагоналям квадрата. Гарантируется, что входное число всегда нечетное."""

#square_width = int(input('Введите сторону квадрата:'))
#symbol = input('Введите ривующий символ:')
square_width = 5
symbol = '#'
for i in range(0,square_width):
    st = ''
    for j in range(0,square_width):
        if (i == j) or (square_width-1-i == j):
            st = st + symbol
        else:
            st = st + ' '
    print(st)

