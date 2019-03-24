from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix(object):
    def __init__(self, list2_d):
        self.matrix = deepcopy(list2_d)
        self.list2D = list2_d
        self.dim_R = len(self.list2D)
        self.dim_C = len(self.list2D[0])

    def __repr__(self):
        res = ''
        for x in self.list2D:
            s = ''
            for y in x:
                s += str(y) + '\t'
            res += s.strip() + '\n'
        return res.strip()

    def __add__(self, other):
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            result = []
            res = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    my_sum = self.list2D[x][y] + other.list2D[x][y]
                    res.append(my_sum)
                result.append(res)
                res = []
            return Matrix(result)
        else:
            return 'Размерности не совпадают'

    def __sub__(self, other):
        if self.dim_R == other.dim_R and self.dim_C == other.dim_C:
            res = []
            result = []
            for x in range(self.dim_R):
                for y in range(self.dim_C):
                    sub = self.list2D[x][y] - other.list2D[x][y]
                    res.append(sub)
                result.append(res)
                res = []
            return Matrix(result)
        else:
            return 'Размерности не совпадают'

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.list2D]
            return Matrix(result)
        elif self.dim_C != other.dim_R:
            raise MatrixError(self, other)
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            result = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        trans_matrix = list(zip(*self.matrix))
        self.matrix = trans_matrix
        return Matrix(trans_matrix)

    def transposed(self):
        trans_matrix = list(zip(*self.matrix))
        return Matrix(trans_matrix)


exec(stdin.read())
