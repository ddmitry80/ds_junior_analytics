"""Напишите программу, которая на вход получает максимальную ширину ромба и рисует его. 
Гарантируется, что входное число всегда нечетное."""

width_rombus = int(input('Введите максимальную ширину ромба:'))
#width_rombus = 7
for i in range (width_rombus//2,0,-1):
    st = ''
    for j in range(0,width_rombus//2):
        if i-j > 0:
            st = st + ' '
        else:
            st = st + '*'
    st += '*'
    for j in range(width_rombus//2-1,0,-1):
        if i-j > 0:
            st = st + ' '
        else:
            st = st + '*'
    print(st)
st = '*'
st *= width_rombus
print(st)
for i in range (1,width_rombus//2+1):
    st = ''
    for j in range(0,width_rombus//2):
        if i-j > 0:
            st = st + ' '
        else:
            st = st + '*'
    st += '*'
    for j in range(width_rombus//2-1,0,-1):
        if i-j > 0:
            st = st + ' '
        else:
            st = st + '*'
    print(st)