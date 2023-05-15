from typing import Any, List, Tuple
from copy import deepcopy
import graf_mst

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

    def insertVertex(self, vertex: Vertex) -> None:
        self.vertex_dict[vertex] = self.order()
        
        self.list.append([])

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge=1) -> None:
        id1 = self.getVertexID(vertex1)
        id2 = self.getVertexID(vertex2)
        self.list[id1].append((id2, edge))
        self.list[id1] = sorted(set(self.list[id1]))
        self.list[id2].append((id1, edge))
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
                    vertex1 = [k.key for k, v in self.vertex_dict.items() if v == i][0]
                    vertex2 = [k.key for k, v in self.vertex_dict.items() if v == j][0]
                    e.append((vertex2, vertex1))
        return e
    

class MST:
    def __init__(self, graph: ListGraph) -> None:
        self.graph = deepcopy(graph)
        self.tree = None
        self.size = self.tree.order()
        self.intree = {key:0 for key in self.graph.vertex_dict.keys()}
        self.distance = {key:float('inf') for key in range(self.size)}
        self.parent = {key:-1 for key in range(self.size)}

    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, val):
        self.__tree = ListGraph()
        for vertex in self.graph.vertex_dict.keys():
            self.__tree.insertVertex(vertex)

    def find_MST(self):
        vertex = list(self.graph.vertex_dict.keys())[0]
        weights = []
        while self.intree[vertex] == 0:
            current = vertex
            self.intree[vertex] = 1
            for n in self.graph.list[self.graph.getVertexID(vertex)]:
                if n[1] < self.distance[n[0]]:
                    self.distance[n[0]] = n[1]
                    self.parent[n[0]] = current
            min_cost = float('inf')
            for v in self.graph.vertex_dict.keys():
                if self.intree[v] == 0:
                    if self.distance[self.tree.getVertexID(v)] < min_cost:
                        min_cost = self.distance[self.tree.getVertexID(v)]
                        vertex = v
            weight = 0
            for edge in self.graph.list[self.graph.getVertexID(self.parent[self.graph.getVertexID(vertex)])]:
                if edge[0] == self.graph.getVertexID(vertex):
                    weight = edge[1]
                    weights.append(weight)
                    break
            self.tree.insertEdge(self.parent[self.tree.getVertexID(vertex)], vertex, weight)

        return sum(weights[:-1])
    

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighboursIdx(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def main():
    g = ListGraph()

    for elem in graf_mst.graf:
        v = Vertex(elem[0])
        if v not in g.vertex_dict.keys():
            g.insertVertex(v)
        v = Vertex(elem[1])
        if v not in g.vertex_dict.keys():
            g.insertVertex(v)
        g.insertEdge(Vertex(elem[0]), Vertex(elem[1]), elem[2])

    t = MST(g)
    sum = t.find_MST()
    printGraph(t.tree)


if __name__ == '__main__':
    main()