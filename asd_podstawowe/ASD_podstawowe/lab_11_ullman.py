#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import deepcopy

import numpy as np
#najtrudniejsze ćwiczenie
#później będzie łatwiej ;)

class Vertex:
    def __init__(self, data):
        self.key = data

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


def is_isomorphism(g, p, m):
    x = m @ np.transpose(m @ g)
    comparison = x == p
    if comparison.all():
        return True
    else:
        return False


def ullmann1(g, p, m=None, current_row=0, used_columns=None, recursion=0, isomorphism=0):
    recursion += 1
    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == len(m):
        current_row -= 1
        if is_isomorphism(g,p,m):
            isomorphism += 1
            return isomorphism, recursion
        else:
            return isomorphism, recursion
    m_copy = deepcopy(m)
    for c in range(len(m_copy[0])):
        if c not in used_columns:
            m_copy[current_row, :] = 0
            m_copy[current_row, c] = 1
            used_columns.append(c)
            isomorphism, recursion = ullmann1(g, p, m_copy, current_row + 1, used_columns, recursion, isomorphism)
            used_columns.remove(c)
    return isomorphism, recursion


def count_edges(m, i):
    count = 0
    for j in range(m.shape[0]):
        if m[i][j] == 1:
            count += 1
    return count


def find_m0(g,p):
    m = np.zeros((p.shape[0], g.shape[0]))
    for i in range(p.shape[0]):
        for j in range(g.shape[0]):
            if count_edges(p, i) <= count_edges(g, j):
                m[i][j] = 1
    return m


def ullmann2(g, p, m0, m=None, current_row=0, used_columns=None, recursion=0, isomorphism=0):
    recursion += 1
    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == len(m):
        current_row -= 1
        if is_isomorphism(g,p,m):
            isomorphism += 1
            return isomorphism, recursion
        else:
            return isomorphism, recursion
    m_copy = deepcopy(m)
    for c in range(len(m_copy[0])):
        if c not in used_columns and m0[current_row][c] == 1:
            for i in range(len(m_copy[0])):
                m_copy[current_row][i] = 0
            m_copy[current_row][c] = 1
            used_columns.append(c)
            isomorphism, recursion = ullmann2(g, p, m0, m_copy, current_row + 1, used_columns, recursion, isomorphism)
            used_columns.remove(c)
    return isomorphism, recursion


def prune(g, p, m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i][j] == 1:
                p_n = []
                for ii in range(p.shape[0]):
                    if p[i][ii] == 1:
                        p_n.append(ii)
                g_n = []
                for jj in range(g.shape[0]):
                    if g[j][jj] == 1:
                        g_n.append(jj)
                for x in p_n:
                    help = False
                    for y in g_n:
                        if m[x][y] == 1:
                            help = True
                            break
                    if help:
                        break
                else:
                    m[i][j] = 0
                    return True
    return False


def ullmann3(g, p, m0, m=None, current_row=0, used_columns=None, recursion=0, isomorphism=0):
    recursion += 1
    if m is None:
        m = np.zeros((p.shape[0], g.shape[0]))
    if used_columns is None:
        used_columns = []
    if current_row == len(m):
        current_row -= 1
        if is_isomorphism(g,p,m):
            isomorphism += 1
            return isomorphism, recursion
        else:
            return isomorphism, recursion
    m_copy = deepcopy(m)
    br = False
    if current_row == len(m) - 1:
       br = prune(g, p, m_copy)
    for c in range(len(m_copy[0])):
        if br == True and current_row != 0:
            break
        if c not in used_columns and m0[current_row][c] == 1:
            for i in range(len(m_copy[0])):
                m_copy[current_row][i] = 0
            m_copy[current_row][c] = 1
            used_columns.append(c)
            isomorphism, recursion = ullmann3(g, p, m0, m_copy, current_row + 1, used_columns, recursion, isomorphism)
            used_columns.remove(c)
    return isomorphism, recursion


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


graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
g_graph = GraphMatrix()
for el in graph_G:
    v1 = Vertex(el[0])
    v2 = Vertex(el[1])
    g_graph.insert_edge(v1,v2)
    g_graph.insert_edge(v2,v1)

p_graph = GraphMatrix()
for el in graph_P:
    v1 = Vertex(el[0])
    v2 = Vertex(el[1])
    p_graph.insert_edge(v1,v2)
    p_graph.insert_edge(v2,v1)

g = np.array(g_graph.graph)
p = np.array(p_graph.graph)
ul1 = ullmann1(g,p)
print(ul1)
m0 = find_m0(g, p)
ul2 = ullmann2(g,p, m0)
print(ul2)
ul3 = ullmann3(g,p, m0)
print(ul3)