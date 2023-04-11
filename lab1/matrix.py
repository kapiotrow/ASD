#!/usr/bin/python
# -*- coding: utf-8 -*-

#skończone

class Matrix:
    def __init__(self, contents, default_elem=0):
        if isinstance(contents, tuple):
            self.matrix = [[default_elem for i in range(contents[1])] for j in range(contents[0])]
        else:
            self.matrix = contents
    
    def __getitem__(self, i):
        return self.matrix[i]
    
    def __setitem__(self, i, val):
        self.matrix[i] = val
    
    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.size() == other.size():
            row, col = self.size()
            result = [[0 for i in range(col)] for j in range(row)]
            for i in range(row):
                for j in range(col):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            
            return Matrix(result)
        else:
            raise Exception("matrices must have equal sizes!")

    def __mul__(self, other):
        row_1, col_1 = self.size()
        row_2, col_2 = other.size()
        if row_1 == col_2 and row_2 == col_1:
            result = [[0 for i in range(col_2)] for j in range(row_1)]

            for i in range(row_1):
                for j in range(col_2):
                    for k in range(row_2):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix(result)
        else:
            raise Exception("wrong matrix sizes!")
        
    def __str__(self) -> None:
        result = ""
        for i in range(self.size()[0]):
            result += "|"
            for j in range(self.size()[1]):
                result += str(self.matrix[i][j])
                if j < self.size()[1]-1:
                    result += " "
            result += "|\n"
        return result

def transpose(matrix: Matrix) -> Matrix:
    result = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(result.size()[0]):
        for j in range(result.size()[1]):
            result[i][j] = matrix[j][i]
    return result


def det2(matrix: Matrix):
    assert matrix.size() == (2, 2)

    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

def swap_rows(matrix: Matrix):
    i = 1
    while i < matrix.size()[0]:
        if matrix[i][0] != 0:
            buf = matrix[0].copy()
            matrix[0] = matrix[i].copy()
            matrix[i] = buf
            return False
    return True


def chio(matrix: Matrix):
    if matrix.size()[0] != matrix.size()[1]:
        raise Exception("matrix must be square!")
    
    n = matrix.size()[0]

    if n == 2:
        return det2(matrix)
    
    new_matrix = Matrix((n-1, n-1))

    sign = 1

    if matrix[0][0] == 0:
        sign = -1
        if swap_rows(matrix):
            return 0
    
    for i in range(n-1):
        for j in range(n-1):
            new_matrix[i][j] = det2(Matrix([[matrix[0][0], matrix[0][j + 1]], [matrix[i + 1][0], matrix[i + 1][j + 1]]]))
    
    return (1 / matrix[0][0] ** (n - 2)) * chio(new_matrix) * sign

def main():
    M = Matrix([[1,0,2],[-1,3,1]])
    N = Matrix((2,3), default_elem=1)
    O = Matrix([[3,1],[2,1],[1,0]])
    P = M + N
    R = M * O
    T = transpose(M)
    print(T)
    print(P)
    print(R)

    M = Matrix(  [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
    
    print(chio(M))

if __name__ == '__main__':
    main()