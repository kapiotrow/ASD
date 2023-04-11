#!/usr/bin/python
# -*- coding: utf-8 -*-

#Skończone

class Matrix:
    def __init__(self, elem, par=0):
        if isinstance(elem, tuple):
            rows, cols = elem
            self.matrix = [[par for i in range(cols)] for j in range(rows)]
        else:
            self.matrix = elem

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j], end=" ")
            print()

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.size()[0] == other.size()[0] and self.size()[1] == other.size()[1]:
            rows, cols = self.size()
            res = [[0 for i in range(cols)] for j in range(rows)]

            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    res[i][j] = self.matrix[i][j] + other[i][j]

            result = Matrix(res)
            return result
        else:
            print("Nie można dodać macierzy")
            return None

    def __mul__(self, other):
        if self.size()[0] == other.size()[1] and self.size()[1] == other.size()[0]:
            rows = self.size()[0]
            cols = other.size()[1]
            res = [[0 for i in range(cols)] for j in range(rows)]

            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(other.size()[0]):
                        res[i][j] += self.matrix[i][k] * other[k][j]
            result = Matrix(res)
            return result
        else:
            print("Nie można pomnożyć macierzy")
            return None


def transpose(matrix):
    rows, cols = matrix.size()
    mat_T = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            mat_T[j][i] = matrix[i][j]
    matrix_T = Matrix(mat_T)
    return matrix_T


if __name__ == "__main__":
    print("Macierz 1")
    matrix1 = Matrix([[1, 0, 2], [-1, 3, 1]])
    matrix1.__str__()

    print("\nMacierz 2")
    matrix2 = Matrix((2, 3), 1)
    matrix2.__str__()

    print("\nMacierz 3")
    matrix3 = Matrix([[3, 1], [2, 1], [1, 0]])
    matrix3.__str__()

    print("\nMacierz - suma 1 i 2")
    matrix4 = matrix1 + matrix2
    matrix4.__str__()

    print("\nMacierz - iloczyn 1 i 3")
    matrix5 = matrix1 * matrix3
    matrix5.__str__()

    print("\nTranspozycja macierzy 1")
    matrix_T = transpose(matrix1)
    matrix_T.__str__()
