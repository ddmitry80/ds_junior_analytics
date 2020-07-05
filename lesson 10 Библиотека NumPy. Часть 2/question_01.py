import numpy as np

def build_array(size):
    """которая принимает на вход размерность квадратной матрицы (двумерного массива, в котором
    число строк и число столбцов совпадают) и создаёт единичную матрицу E (массив) соответствующей размерности"""
    E = np.zeros((size, size), dtype = int)
    for i in range(0, size):
        E[i, i] = 1
    return E


print(build_array(5))