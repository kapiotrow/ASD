import polska


class Vertex:
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.key = data[2]

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, inn, out):
        self.vetrex_1 = inn
        self.vetrex_2 = out


class GraphMatrix:
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

    def insert_vertex(self, vertex: Vertex):
        self.v_list.append(vertex)
        self.dicto[vertex] = len(self.v_list) - 1
        if len(self.graph) == 0:
            self.graph.append([0])
        else:
            for line in self.graph:
                line.append(0)
            self.graph.append([0 for i in range(len(self.graph[0]))])

    def insert_edge(self, v1, v2):
        if v1 not in self.v_list:
            self.insert_vertex(v1)
        if v2 not in self.v_list:
            self.insert_vertex(v2)
        idx1 = self.get_vertex_idx(v1)
        idx2 = self.get_vertex_idx(v2)
        self.graph[idx1][idx2] = 1
        self.ssize += 1

    def delete_edge(self, v1, v2):
        idx1 = self.get_vertex_idx(v1)
        idx2 = self.get_vertex_idx(v2)
        self.graph[idx1][idx2] = 0
        self.ssize -= 1

    def upgrade_dict(self):
        for i in range(len(self.v_list)):
            self.dicto[self.v_list[i]] = i

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.v_list.remove(vertex)
        self.dicto.pop(vertex)
        self.upgrade_dict()
        self.graph.pop(idx)
        for line in self.graph:
            line.pop(idx)

    def neighbours(self, v_idx):
        result_list = []
        for i in range(len(self.graph[v_idx])):
            if self.graph[v_idx][i] == 1:
                result_list.append(i)
        return result_list

    def size(self):
        return self.ssize

    def order(self):
        return len(self.graph)

    def edges(self):
        result_list = []
        for row in range(len(self.graph)):
            for col in range(row):
                if self.graph[row][col] == 1:
                    result_list.append((self.get_vertex(row).key, self.get_vertex(col).key))
        return result_list


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

    def insert_edge(self, v1, v2):
        if v1 not in self.v_list:
            self.insert_vertex(v1)
        if v2 not in self.v_list:
            self.insert_vertex(v2)
        idx1 = self.get_vertex_idx(v1)
        idx2 = self.get_vertex_idx(v2)
        self.graph[idx1].append(idx2)
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


polwoj = GraphList()
for key1, key2 in polska.graf:
    v1 = Vertex(polska.slownik[key1])
    v2 = Vertex(polska.slownik[key2])
    polwoj.insert_edge(v1, v2)
polwoj.delete_edge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
polwoj.delete_edge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
polwoj.delete_vertex(Vertex(polska.slownik['K']))
polska.draw_map(polwoj.edges())

polwoj = GraphList()
for key1, key2 in polska.graf:
    v1 = Vertex(polska.slownik[key1])
    v2 = Vertex(polska.slownik[key2])
    polwoj.insert_edge(v1, v2)
polwoj.delete_edge(Vertex(polska.slownik['W']), Vertex(polska.slownik['E']))
polwoj.delete_edge(Vertex(polska.slownik['E']), Vertex(polska.slownik['W']))
polwoj.delete_vertex(Vertex(polska.slownik['K']))
polska.draw_map(polwoj.edges())