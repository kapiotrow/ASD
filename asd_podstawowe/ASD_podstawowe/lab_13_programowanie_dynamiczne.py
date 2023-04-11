#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import numpy as np


def string_compare_rekur(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare_rekur(P, T, i - 1, j - 1) + (P[i] != T[j])
    wstawien = string_compare_rekur(P, T, i, j - 1) + 1
    usuniec = string_compare_rekur(P, T, i - 1, j) + 1
    najnizszy_koszt = min(zamian, wstawien, usuniec)
    return najnizszy_koszt


def find_path(parent):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    temp = parent[i][j]
    while temp != 'X':
        result += temp
        if temp == 'D':
            i -= 1
        elif temp == 'I':
            j -= 1
        else:
            i -= 1
            j -= 1
        temp = parent[i][j]
    return result[::-1]


def string_compare_pd(P, T, i, j):
    p_size = len(P)
    t_size = len(T)
    D = [[0 for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        D[i][0] = i
    for j in range(t_size):
        D[0][j] = j
    parent = [['X' for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        parent[i][0] = 'D'
    for j in range(t_size):
        parent[0][j] = 'I'

    for i in range(1, p_size):
        for j in range(1, t_size):
            z = D[i - 1][j - 1] + (P[i] != T[j])
            w = D[i][j - 1] + 1
            u = D[i - 1][j] + 1
            temp = [z, w, u]
            mini = min(temp)
            D[i][j] = mini
            idx = temp.index(mini)
            type = ''
            if idx == 0:
                if T[j] == P[i]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parent[i][j] = type
    parent[0][0] = 'X'
    path = find_path(parent)
    return D[p_size - 1][t_size - 1], path


def string_compare_pd_2(P, T, i, j):
    p_size = len(P)
    t_size = len(T)
    D = [[0 for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        D[i][0] = i
    parent = [['X' for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        parent[i][0] = 'D'
    for j in range(t_size):
        parent[0][j] = 'I'

    for i in range(1, p_size):
        for j in range(1, t_size):
            z = D[i - 1][j - 1] + (P[i] != T[j])
            w = D[i][j - 1] + 1
            u = D[i - 1][j] + 1
            temp = [z, w, u]
            mini = min(temp)
            D[i][j] = mini
            idx = temp.index(mini)
            type = ''
            if idx == 0:
                if T[j] == P[i]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parent[i][j] = type
    parent[0][0] = 'X'
    end = D[-1].index(min(D[-1]))
    start = end - p_size + 2
    return start, end


def find_sekwens(parent, p):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    temp = parent[i][j]
    while temp != 'X':
        if temp == 'D':
            i -= 1
        elif temp == 'I':
            j -= 1
        elif temp == 'M':
            result += p[i]
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
        temp = parent[i][j]
    return result[::-1]


def string_compare_pd_3(P, T, i, j):
    p_size = len(P)
    t_size = len(T)
    D = [[0 for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        D[i][0] = i
    for j in range(t_size):
        D[0][j] = j
    parent = [['X' for j in range(t_size)] for i in range(p_size)]
    for i in range(p_size):
        parent[i][0] = 'D'
    for j in range(t_size):
        parent[0][j] = 'I'

    for i in range(1, p_size):
        for j in range(1, t_size):
            x = 0
            if T[j] != P[i]:
                x = np.inf
            z = D[i - 1][j - 1] + x
            w = D[i][j - 1] + 1
            u = D[i - 1][j] + 1
            temp = [z, w, u]
            mini = min(temp)
            D[i][j] = mini
            idx = temp.index(mini)
            type = ''
            if idx == 0:
                if T[j] == P[i]:
                    type = 'M'
                else:
                    type = 'S'
            elif idx == 1:
                type = 'I'
            else:
                type = 'D'

            parent[i][j] = type
    parent[0][0] = 'X'
    sekwens = find_sekwens(parent, P)
    return sekwens


def sort_t(t):
    p = ' '
    temp = t
    temp = temp.replace(' ', '')
    t_list = []
    for el in temp:
        t_list.append(int(el))
    t_list.sort()
    for el in t_list:
        p += str(el)
    return p
P = ' kot'
T = ' pies'
result = string_compare_rekur(P, T, len(P) - 1, len(T) - 1)
print(result)

P = ' biały autobus'
T = ' czarny autokar'
result, path = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
print(result)


P = ' thou shalt not'
T = ' you should not'
result, path = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
print(path)


P = ' ban'
T = ' mokeyssbanana'
start, end = string_compare_pd_2(P, T, len(P) - 1, len(T) - 1)
print(start)


P = ' democrat'
T = ' republican'
sekwens = string_compare_pd_3(P, T, len(P) - 1, len(T) - 1)
print(sekwens)


T = ' 243517698'
P = sort_t(T)
sekwens = string_compare_pd_3(P, T, len(P) - 1, len(T) - 1)
print(sekwens)