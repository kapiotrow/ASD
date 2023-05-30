from typing import List, Any, Tuple
from copy import deepcopy
import numpy as np

class Vertex:
    def __init__(self, key: Any) -> None:
        self.key = key

    def __hash__(self) -> Any:
        return hash(self.key)
    
    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __str__(self) -> str:
        return f'{self.key}'



class MatrixGraph:
    def __init__(self) -> None:
        self.vertex_dict = {}
        self.matrix = []

    def order(self):
        return len(self.vertex_dict)
    
    def isEmpty(self) -> bool:
        return self.order() == 0
    
    def getVertexID(self, vertex: Vertex) -> int:
        return self.vertex_dict[vertex]

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex] = self.order()
        
        for row in self.matrix:
            row.append(0)
        
        if self.order() != 0:
            self.matrix.append([0] * (self.order()))

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: int=1) -> None:
        self.matrix[self.getVertexID(vertex1)][self.getVertexID(vertex2)] = edge
        self.matrix[self.getVertexID(vertex2)][self.getVertexID(vertex1)] = edge

    def deleteVertex(self, vertex: Vertex) -> None:
        id = self.getVertexID(vertex)
        for row in self.matrix:
            row.pop(id)
        self.matrix.pop(id)

        new_dict = {}
        for k, v in self.vertex_dict.items():
            if v == id:
                continue
            if v > id:
                new_dict[k] = v - 1
            else:
                new_dict[k] = v
        self.vertex_dict = new_dict
    
    def deleteEdge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        self.matrix[self.getVertexID(vertex1)][self.getVertexID(vertex2)] = 0
        self.matrix[self.getVertexID(vertex2)][self.getVertexID(vertex1)] = 0

    def neighboursIdx(self, vertex_id: int) -> List[int]:
        n = []
        for i, v in enumerate(self.matrix[vertex_id]):
            if v != 0:
                n.append(i)
        return n
    
    def size(self) -> int:
        edges = 0
        for row in self.matrix:
            edges += sum([i for i in row])
        return edges // 2
    
    def edges(self) -> List[Tuple]:
        e = []
        for d in range(0, len(self.matrix)):
            for r in range(0, len(self.matrix)):
                if self.matrix[d][r] and r > d:
                    vertex1 = [k for k, v in self.vertex_dict.items() if v == r][0]
                    vertex2 = [k for k, v in self.vertex_dict.items() if v== d][0]
                    e.append((vertex2, vertex1))
        print('matrix: ', e)
        return e

def is_iso(M, P, G):
    X = M @ np.transpose(M @ G)
    comparison = X == P
    if comparison.all():
        return True
    else:
        return False

def ullman1(G, P, M=None, current_row=0, used_columns=None, calls=0, iso=0):
    calls += 1
    if M is None:
        M = np.zeros((P.shape[0], G.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == M.shape[0]:
        current_row -= 1
        if is_iso(M, P, G):
            iso += 1
            return calls, iso
        else:
            return calls, iso
    M1 = deepcopy(M)
    for c in range(len(M1[0])):
        if c not in used_columns:
            M1[current_row, :] = 0
            M1[current_row, c] = 1
            used_columns.append(c)
            calls, iso = ullman1(G, P, M1, current_row + 1, used_columns, calls, iso)
            used_columns.remove(c)
    return calls, iso
    
def edges(M, i):
    e = 0
    for j in range(M.shape[0]):
        if M[i][j] == 1:
            e += 1
    return e
    
def find_m0(G, P):
    M = np.zeros((P.shape[0], G.shape[0]))
    for i in range(P.shape[0]):
        for j in range(G.shape[0]):
            if edges(P, i) <= edges(G, j):
                M[i][j] = 1
    return M

def ullman2(G, P, M0, M=None, current_row=0, used_columns=None, calls=0, iso=0):
    calls += 1
    if M is None:
        M = np.zeros((P.shape[0], G.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == M.shape[0]:
        current_row -= 1
        if is_iso(M, P, G):
            iso += 1
            return calls, iso
        else:
            return calls, iso
    
    M1 = deepcopy(M)
    for c in range(len(M1[0])):
        if c not in used_columns and M0[current_row][c] == 1:
            for i in range(len(M1[0])):
                M1[current_row][i] = 0
            M1[current_row][c] = 1
            used_columns.append(c)
            calls, iso = ullman2(G, P, M0, M1, current_row + 1, used_columns, calls, iso)
            used_columns.remove(c)
    return calls, iso


def prune(M, P, G):
    changed = True
    while changed:
        changed = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 0:
                    n = False

                    for k in range(len(P[0])):
                        for l in range(len(G[0])):
                            if M[k, l] == 1:
                                n = True
                                break
                    
                    if not n:
                        M[i, j] = 0
                        changed = True
                        break
    return False


def ullman3(G, P, M0, M=None, current_row=0, used_columns=None, calls=0, iso=0):
    calls += 1
    if M is None:
        M = np.zeros((P.shape[0], G.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == M.shape[0]:
        current_row -= 1
        if is_iso(M, P, G):
            iso += 1
            return calls, iso
        else:
            return calls, iso
    
    M1 = deepcopy(M)
    b = False
    if current_row == M.shape[0] - 1:
       b = prune(M1, P, G)
    
    for c in range(len(M1[0])):
        if b and current_row != 0:
            break
        if c not in used_columns and M0[current_row][c] == 1:
            for i in range(len(M1[0])):
                M1[current_row][i] = 0
            M1[current_row][c] = 1
            used_columns.append(c)
            calls, iso = ullman3(G, P, M0, M1, current_row + 1, used_columns, calls, iso)
            used_columns.remove(c)
    return calls, iso


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    g1 = MatrixGraph()
    g2 = MatrixGraph()

    for elem in graph_G:
        if Vertex(elem[0]) not in g1.vertex_dict.keys():
            g1.insertVertex(Vertex(elem[0]))
        if Vertex(elem[1]) not in g1.vertex_dict.keys():
            g1.insertVertex(Vertex(elem[1]))
        g1.insertEdge(Vertex(elem[0]), Vertex(elem[1]))

    for elem in graph_P:
        if Vertex(elem[0]) not in g2.vertex_dict.keys():
            g2.insertVertex(Vertex(elem[0]))
        if Vertex(elem[1]) not in g2.vertex_dict.keys():
            g2.insertVertex(Vertex(elem[1]))
        g2.insertEdge(Vertex(elem[0]), Vertex(elem[1]))

    G = np.array(g1.matrix)
    P = np.array(g2.matrix)
    calls, iso = ullman1(G, P)
    print(iso, calls)

    M0 = find_m0(G, P)
    calls, iso = ullman2(G, P, M0)
    print(iso, calls)

    calls, iso = ullman3(G, P, M0)
    print(iso, calls)
    
if __name__ == '__main__':
    main()