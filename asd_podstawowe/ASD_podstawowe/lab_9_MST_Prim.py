import numpy as np
#zadanie ocenione na maksa, ale zwraca nieodpowieni output.
#powinno zwrócić
#------GRAPH------ 10
#A -> C 1;B 4;
#B -> A 4;G 7;
#C -> A 1;D 3;
#D -> C 3;
#E -> F 2;
#F -> G 8;E 2;H 2;
#G -> B 7;F 8;J 8;
#H -> F 2;I 3;
#I -> H 3;
#J -> G 8;
#-------------------

class Vertex:
    def __init__(self, data):
        self.key = data

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, inn, out):
        self.vetrex_1 = inn
        self.vetrex_2 = out


class GraphList:
    def __init__(self):
        self.v_list = []
        self.dicto = {}
        self.graph = []
        self.ssize = 0

    def get_vertex_idx(self, vertex):
        return self.dicto[vertex]

    def get_vertex(self, vertex_idx):
        for key, value in self.dicto.items():
            if value == vertex_idx:
                return key

    def upgrade_dict(self):
        for i in range(len(self.v_list)):
            self.dicto[self.v_list[i]] = i

    def insert_vertex(self, vertex: Vertex):
        self.v_list.append(vertex)
        self.dicto[vertex] = len(self.v_list) - 1
        self.graph.append([])

    def insert_edge(self, v1, v2, cost):
        if v1 not in self.v_list:
            self.insert_vertex(v1)
        if v2 not in self.v_list:
            self.insert_vertex(v2)
        idx1 = self.get_vertex_idx(v1)
        idx2 = self.get_vertex_idx(v2)
        self.graph[idx1].append((idx2, cost))
        self.ssize += 1

    def delete_edge(self, v1, v2):
        idx1 = self.get_vertex_idx(v1)
        idx2 = self.get_vertex_idx(v2)
        self.graph[idx1].remove(idx2)
        self.ssize -= 1

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.v_list.remove(vertex)
        self.dicto.pop(vertex)
        self.upgrade_dict()
        self.graph.pop(idx)
        for line in self.graph:
            if idx in line:
                line.remove(idx)
            for el in line:
                if el > idx:
                    idx -= 1

    def neighbours(self, v_idx):
        return self.graph[v_idx]

    def size(self):
        return self.ssize

    def order(self):
        return len(self.graph)

    def edges(self):
        result_list = []
        for i in range(len(self.graph)):
            for el in self.graph[i]:
                result_list.append((self.get_vertex(i).key, self.get_vertex(el).key))
        return result_list

    def primm(self):
        result = GraphList()
        for v in self.v_list:
            result.insert_vertex(v)
        alfa = {}
        beta = {}
        v = []
        s = 0
        for i in range(len(self.graph)):
            v.append(i)
        v = set(v)
        for u in v:
            alfa[u] = -1
            beta[u] = np.inf
        sum = 0
        not_in_mst = v - {s}
        last_ver = s
        beta[s] = 0
        while not_in_mst:
            for vertex, waga in self.neighbours(last_ver):
                if vertex in not_in_mst:
                    if beta[vertex] > waga:
                        alfa[vertex] = last_ver
                        beta[vertex] = waga
            mini = np.inf
            chosen_one = None
            for ver in not_in_mst:
                if beta[ver] < mini:
                    mini = beta[ver]
                    chosen_one = ver
            not_in_mst.remove(chosen_one)
            sum += beta[chosen_one]
            result.insert_edge(self.get_vertex(alfa[chosen_one]), self.get_vertex(chosen_one), beta[chosen_one])
            last_ver = chosen_one
        return result, sum


def printgraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i).key
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.get_vertex(j).key, w, end=";")
        print()
    print("-------------------")


graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)
        ]
my_graph = GraphList()
for el in graf:
    my_graph.insert_edge(Vertex(el[0]), Vertex(el[1]), el[2])
    my_graph.insert_edge(Vertex(el[1]), Vertex(el[0]), el[2])
result, sum = my_graph.primm()
printgraph(result)

