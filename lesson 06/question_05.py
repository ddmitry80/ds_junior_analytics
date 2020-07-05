def mult2(*args):
    res = 1
    for i in args:
        print(i,type(i))
        res += i
    return res

List = [1, 2, 3, 4, 5, 6, 7]
print(mult2(*List))