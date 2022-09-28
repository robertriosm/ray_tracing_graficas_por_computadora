
from math import sqrt


def matrix_product(A, B):
    result = [[x * 0 for x in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def identity(num):
    m = []
    for row in range(0, num):
        m.append([])
        for col in range(0, num):
            if (row == col):
                m[row].append(1)
            else:
                m[row].append(0)
    return m


def dot(A: list, B: list):
    return sum([x * y for x,y in zip(A, B)])

def magnitud_vector(vector: list):
    sum = 0
    for comp in vector:
        sum += comp**2
    return sum**0.5

def normalizaVector(vector: list):
    magnitud = magnitud_vector(vector)
    return [a/magnitud for a in vector]


def dot_product(vector_1, vector_2):
    if len(vector_1)!=len(vector_2):
        raise Exception ("No match on vector dimensions")
    total = 0
    for componente_i in range(len(vector_1)):
        total += vector_1[componente_i]*vector_2[componente_i]
    return total


def multiply_vectors(matrix: list, v):
    return [dot(r, v) for r in matrix]


def vectors_product(v1: list, v2: list):
    res = [i for i in v1]
    for i in range(len(v1)):
        res[i] = v1[i] * v2[i]
    return res


def subtract(A: list, B: list):
     size = isinstance(A, list) + 2 * isinstance(B, list)
     if size == 3:
         return [subtract(ra,rb) for ra,rb in zip(A,B)]
     if size == 2:
         return [subtract(A,rb) for rb in B]
     if size == 1: 
         return [subtract(ra,B) for ra in A]
     return A - B


def suma_o_resta_vectores(vector_1: list, vector_2: list, is_resta: bool = False):
    factor = -1 if is_resta else 1
    if not len(vector_2)==len(vector_1):
        print("Dimensiones de vectores no coiniciden")
        return
    vector_res = []
    for i in range(len(vector_1)):
        vector_res.append(vector_1[i]+factor*vector_2[i])
    return vector_res


def add(A, B):
     size = isinstance(A, list) + 2 * isinstance(B, list)
     if size == 3:
         return [add(ra,rb) for ra,rb in zip(A,B)]
     if size == 2:
         return [add(A,rb) for rb in B]
     if size == 1: 
         return [add(ra,B) for ra in A]
     return A + B


def cross_product(A: list, B: list):
    return [A[1] * B[2] - A[2] * B[1],
            A[2] * B[0] - A[0] * B[2],
            A[0] * B[1] - A[1] * B[0]]


def normalize(A: list):
    return sqrt(((A[0] - A[1]) ** 2) + ((A[1] - A[2]) ** 2) + ((A[2] - A[0]) ** 2))


def normalize_vector(A: list):
    return sqrt(sum(i**2 for i in A))


def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def inverse_matrix(A: list):
    tmp = [[] for _ in A]

    for i,j in enumerate(A):
        assert len(j) == len(A)
        tmp[i].extend(j + [0]*i + [1] + [0]*(len(A)-i-1))

    gauss(tmp)

    result = []
    for i in range(len(tmp)):
        result.append(tmp[i][len(tmp[i])//2:])

    return result


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("cant inverse matrix")

        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)

    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)

    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)

    return a

def add_vectors(v1:list, v2:list):
    result= [0,0,0]
    for i in range(len(v1)):
        result[i] = v1[i] + v2[i]
    
def multiply_2_vectors(v1, v2):
    return [v1[i] * v2[i] for i in range(len(v1))]
