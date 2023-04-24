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
        self.matrix = []

    def order(self):
        return len(self.vertex_dict)
    
    def isEmpty(self) -> bool:
        return self.order() == 0
    
    def getVertexID(self, vertex: Vertex) -> int:
        return self.vertex_dict[vertex.key]

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex.key] = self.order()
        
        for row in self.matrix:
            row.append(Edge())
        
        if self.order() != 0:
            self.matrix.append([Edge()] * (self.order()))

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge=Edge(1)) -> None:
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
            edges += sum([i.weight for i in row])
        return edges // 2
    
    def edges(self) -> List[Tuple]:
        e = []
        for d in range(0, len(self.matrix)):
            for r in range(0, len(self.matrix)):
                if self.matrix[d][r].weight and r > d:
                    vertex1 = [k for k, v in self.vertex_dict.items() if v == r][0]
                    vertex2 = [k for k, v in self.vertex_dict.items() if v== d][0]
                    e.append((vertex2, vertex1))
        print('matrix: ', e)
        return e
    


class ListGraph:
    def __init__(self) -> None:
        self.vertex_dict = {}
        self.list = []

    def order(self):
        return len(self.vertex_dict)
    
    def isEmpty(self) -> bool:
        return self.order() == 0
    
    def getVertexID(self, vertex: Vertex) -> int:
        return self.vertex_dict[vertex.key]

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex.key] = self.order()
        
        self.list.append([])

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        id1 = self.getVertexID(vertex1)
        id2 = self.getVertexID(vertex2)
        self.list[id1].append(id2)
        self.list[id1] = sorted(set(self.list[id1]))
        self.list[id2].append(id1)
        self.list[id2] = sorted(set(self.list[id2]))

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
        
        for i in self.list[id2]:
            if i == id1 and i in self.list[id2]:
                self.list[id2].remove(i)

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
                    vertex1 = [k for k, v in self.vertex_dict.items() if v == i][0]
                    vertex2 = [k for k, v in self.vertex_dict.items() if v == j][0]
                    e.append((vertex2, vertex1))
        return e


def main():
    print(polska.slownik)
    adjacency_list = ListGraph()
    adjacency_matrix = MatrixGraph()

    for key in polska.slownik:
        adjacency_list.insertVertex(Vertex(key))
        adjacency_matrix.insertVertex(Vertex(key))

    for (vertex1, vertex2) in polska.graf:
        adjacency_list.insertEdge(Vertex(vertex1), Vertex(vertex2))
        adjacency_matrix.insertEdge(Vertex(vertex1), Vertex(vertex2))

    adjacency_list.deleteVertex(Vertex('K'))
    adjacency_matrix.deleteVertex(Vertex('K'))

    adjacency_list.deleteEdge(Vertex('W'), Vertex('E'))
    adjacency_matrix.deleteEdge(Vertex('W'), Vertex('E'))

    #polska.draw_map(adjacency_list.edges())
    polska.draw_map(adjacency_matrix.edges())

if __name__ == '__main__':
    main()       