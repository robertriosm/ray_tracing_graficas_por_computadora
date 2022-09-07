import numpy as np

#from gl import V3


def matrix_by_const(A: list[list[int or float]], a: int or float):
    return [[a*j for j in A[i]] for i in range(len(A))]


def vector_by_const(A: list[int or float] or tuple[int or float], a: float or int):
    return [i*a for i in A]

