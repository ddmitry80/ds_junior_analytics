import numpy as np

def my_reshape(A, x_size, y_size):
    if x_size * y_size != A.size:
        return np.array([])
    return A.reshape(x_size, y_size)


A = np.array([[2, 4, 6], 
        [4, 8, 10]])
print(my_reshape(A, 6, 1))

A = np.array([[2, 4, 6], 
        [4, 8, 10]])
print(my_reshape(A, 4, 2))
