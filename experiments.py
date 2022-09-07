import numpy as np

mat = np.array([2,2,2])

ye = mat * -1

mat1 = [[2,2,2], [2,2,2], [2,2,2]]

def const_x_matrix(A: list, a: int or float):
    res = []
    for i in A:
        for j in A:
            
    res = [0*i for i in A]
    for i in res:
        for j in i:
            j = j*a
    return res

ye2 = mat1 * -1

print(ye2)

print(const_x_matrix(mat1, -1))