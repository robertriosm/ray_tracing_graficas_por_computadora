

def matrix_by_const(A: list[list[int or float]], a: int or float):
    return [[a*j for j in A[i]] for i in range(len(A))]


def vector_by_const(A: list[int or float] or tuple[int or float], a: float or int):
    return [i*a for i in A]

def vector_add_const(A: list[int or float] or tuple[int or float], a: float or int):
    return [i+a for i in A]

def add_matrices(A:list, B: list):
    res = [[0*j for j in A[i]] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j] + B[i][j]
    return res

def add_vectors(v1: list, v2: list):
    res = [i*0 for i in range(len(v1))]
    for i in range(len(v1)):
            res[i] = v1[i] + v2[i]
    return res

