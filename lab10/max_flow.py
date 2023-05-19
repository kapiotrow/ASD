from typing import Any, List, Tuple
from copy import deepcopy

class Vertex:
    def __init__(self, key: Any) -> None:
        self.key = key
        self.color = None

    def __hash__(self) -> Any:
        return hash(self.key)
    
    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __str__(self) -> str:
        return f'{self.key}'
    


class Edge:
    def __init__(self, capacity, isresidual) -> None:
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity
        self.isResidual = isresidual

    def __str__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.isResidual}"
    
    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.isResidual}"
    
    def __gt__(self, other):
        return self.capacity > other.capacity
    
    def __le__(self, other):
        return self.capacity < other.capacity
    


class ListGraph:
    def __init__(self) -> None:
        self.vertex_dict = {}
        self.list = []

    def order(self):
        return len(self.vertex_dict)
    
    def isEmpty(self) -> bool:
        return self.order() == 0
    
    def getVertexID(self, vertex: Vertex) -> int:
        return self.vertex_dict[vertex]
    
    def getVertex(self, id) -> int:
        return ([vertex for vertex, val in self.vertex_dict.items() if val == id][0]).key
    
    def getEdge(self, vertex1, vertex2) -> Edge:
        for e in self.list[vertex1]:
            if e[0] == vertex2:
                return e[1]

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex] = self.order()
        
        self.list.append([])

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge) -> None:
        id1 = self.getVertexID(vertex1)
        id2 = self.getVertexID(vertex2)
        self.list[id1].append((id2, edge))

    def deleteVertex(self, vertex: Vertex) -> None:
        id = self.getVertexID(vertex)
        self.list.pop(id)
        for id1, row in enumerate(self.list):
            for id2, j in enumerate(row):
                if j == id and j in row:
                    row.remove(j)
            for id2, j in enumerate(row):
                if j > id and j in row:
                    self.list[id1][id2] -= 1

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
        id1 = self.getVertexID(vertex1)
        id2 = self.getVertexID(vertex2)

        for i in self.list[id1]:
            if i == id2 and i in self.list[id1]:
                self.list[id1].remove(i)
                break

    def neighboursIdx(self, vertex_id: int) -> List[int]:
        return self.list[vertex_id]
    
    def size(self) -> int:
        edges = 0
        for row in self.list:
            edges += len(row)
        return edges // 2
    
    def edges(self) -> List[Tuple]:
        l = self.list.copy()
        e = []
        for i, row in enumerate(l):
            for j in row:
                if i < j:
                    vertex1 = [k.key for k, v in self.vertex_dict.items() if v == i][0]
                    vertex2 = [k.key for k, v in self.vertex_dict.items() if v == j][0]
                    e.append((vertex2, vertex1))
        return e
    
    def BFS(self, begin) -> List:
        visited = []
        parent = [None for v in range(self.order())]
        queue = [begin]

        while queue:
            e = queue.pop(0)
            neighbours = self.neighboursIdx(e)
            for v in neighbours:
                if v[0] not in visited and v[1].residual > 0:
                    queue.append(v[0])
                    visited.append(v[0])
                    parent[v[0]] = e
        return parent
    
    def flow(self, begin, end, parent) -> float:
        current = end
        min_cap = float('inf')
        if parent[current] is None:
            return 0
        while current is not begin:
            e = self.getEdge(parent[current], current)
            if min_cap > e.residual:
                min_cap = e.residual
            current = parent[current]
        return min_cap
    
    def path_augmentation(self, begin, end, parent, min_cap) -> None:
        current = end
        while current is not begin:
            self.getEdge(parent[current], current).flow += min_cap
            self.getEdge(parent[current], current).residual -= min_cap
            self.getEdge(current, parent[current]).residual += min_cap
            current = parent[current]

    def FF(self, begin, end) -> float:
        begin_id = self.getVertexID(begin)
        end_id = self.getVertexID(end)
        sum = 0
        parent = self.BFS(begin_id)
        min_cap = self.flow(begin_id, end_id, parent)
        while min_cap > 0:
            sum += min_cap
            self.path_augmentation(begin_id, end_id, parent, min_cap)
            parent = self.BFS(begin_id)
            min_cap = self.flow(begin_id, end_id, parent)
        return sum

    
def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighboursIdx(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


    
def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), 
              ('d', 'c', 4)]


    for i in range(4):
        gl = ListGraph()
        for elem in eval('graf_' + str(i)):
            if Vertex(elem[0]) not in gl.vertex_dict.keys():
                gl.insertVertex(Vertex(elem[0]))
            if Vertex(elem[1]) not in gl.vertex_dict.keys():
                gl.insertVertex(Vertex(elem[1]))
            gl.insertEdge(Vertex(elem[0]), Vertex(elem[1]), Edge(elem[2], False))
            gl.insertEdge(Vertex(elem[1]), Vertex(elem[0]), Edge(0, True))
        print(f"Max przepływ dla grafu numer {i}:")
        print(gl.FF(Vertex('s'), Vertex('t')))
        printGraph(gl)

if __name__ == '__main__':
    main()