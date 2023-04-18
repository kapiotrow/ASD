import polska
from typing import Any, List, Tuple

class Vertex:
    def __init__(self, key: Any) -> None:
        self.key = key

    def __hash__(self) -> Any:
        return hash(self.key)
    
    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __str__(self) -> str:
        return f'{self.key}'
    

class Edge:
    def __init__(self, weight=0) -> None:
        self.weight = weight


class MatrixGraph:
    def __init__(self) -> None:
        self.vertex_dict = {}
        self.matrix = [[]]

    def order(self):
        return len(self.vertex_dict)
    
    def isEmpty(self) -> bool:
        return self.order == 0
    
    def getVertexID(self, vertex: Vertex) -> int:
        return self.vertex_dict[vertex]

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex] = self.order()
        
        for row in self.matrix:
            row.append(0)
        
        if self.order != 0:
            self.matrix.append([0] * (self.order + 1))

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge=Edge(1)) -> None:
        self.matrix[self.getVertexID(vertex1)][self.getVertexID(vertex2)] = edge
        self.matrix[self.getVertexID(vertex2)][self.getVertexID(vertex1)] = edge

    def deleteVertex(self, vertex: Vertex) -> None:
        id = self.getVertexID(vertex)
        for row in self.matrix:
            row.pop(vertex)
        self.matrix.pop(vertex)

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
        self.matrix[self.getVertexID(vertex1)][self.getVertexID(vertex2)] = Edge()
        self.matrix[self.getVertexID(vertex2)][self.getVertexID(vertex1)] = Edge()

    def neighboursIdx(self, vertex_id: int) -> List[int]:
        n = []
        for i, v in enumerate(self.matrix[vertex_id]):
            if v != 0:
                n.append(i)
        return n
    
    def size(self) -> int:
        edges = 0
        for row in self.matrix:
            edge += sum(row)
        return edges // 2
    
    def edges(self) -> List[Tuple]:
        