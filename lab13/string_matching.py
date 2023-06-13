import numpy as np
import time


def string_compare(P, T, i, j):
    if i == 0: return j
    if j == 0: return i

    changes = string_compare(P, T, i - 1, j - 1) + int(P[i] != T[j])
    inserts = string_compare(P, T, i, j - 1) + 1
    deletes = string_compare(P, T, i - 1, j) + 1

    lowest_cost = min(changes, inserts, deletes)
    return lowest_cost


def string_compare_pd(P, T, i, j):
    D = np.zeros((len(P), len(T)))
    for k in range(len(T)):
        D[0][k] = k
    for k in range(len(P)):
        D[k][0] = k

    parents = np.full((len(P), len(T)), 'X')
    for k in range(1, len(parents[0])):
        parents[0][k] = 'I'
    for k in range(1, len(parents)):
        parents[k][0] = 'D'

    for k in range(1, i + 1):
        for l in range(1, j + 1):
            changes = D[k - 1][l - 1] + int(P[k] != T[l])
            inserts = D[k][l - 1] + 1
            deletes = D[k - 1][l] + 1

            lowest_cost = min(changes, inserts, deletes)

            D[k][l] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[k] == T[l]:
                    parents[k][l] = 'M'
                else: parents[k][l] = 'S'
            elif inserts < changes and inserts < deletes:
                parents[k][l] = 'I'
            else: parents[k][l] = 'D'
    return D[i][j], parents


def path_reconstruction(parents):
    i = len(parents) - 1
    j = len(parents[0]) - 1
    path = []
    curr = parents[i][j]

    while curr != 'X':
        if curr == 'M' or curr == 'S':
            i -= 1
            j -= 1
        elif curr == 'D':
            i -= 1
        else: j -= 1

        path.append(curr)
        curr = parents[i][j]
    path.reverse()
    return ''.join(path)


def string_compare_pd2(P, T, i, j):
    D = np.zeros((len(P), len(T)))
    for k in range(len(P)):
        D[k][0] = k

    parents = np.full((len(P), len(T)), 'X')
    for k in range(1, len(parents)):
        parents[k][0] = 'D'

    for k in range(1, i + 1):
        for l in range(1, j + 1):
            if P[k] != T[l]:
                changes = D[k - 1][l - 1] + 1000
            else: changes = D[k - 1][l - 1]

            inserts = D[k][l - 1] + 1
            deletes = D[k - 1][l] + 1

            lowest_cost = min(changes, inserts, deletes)

            D[k][l] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[k] == T[l]:
                    parents[k][l] = 'M'
                else: parents[k][l] = 'S'
            elif inserts < changes and inserts < deletes:
                parents[k][l] = 'I'
            else: parents[k][l] = 'D'
    m = len(P) - 1
    n = 0
    for k in range(1, len(T)):
        if D[m][k] < D[m][n]:
            n = k
    return n - len(P) + 2


def string_compare_pd3(P, T, i, j):
    D = np.zeros((len(P), len(T)))
    for k in range(len(T)):
        D[0][k] = k
    for k in range(len(P)):
        D[k][0] = k

    parents = np.full((len(P), len(T)), 'X')
    for k in range(1, len(parents[0])):
        parents[0][k] = 'I'
    for k in range(1, len(parents)):
        parents[k][0] = 'D'

    for k in range(1, i + 1):
        for l in range(1, j + 1):
            if P[k] != T[l]:
                changes = D[k - 1][l - 1] + 1000
            else: changes = D[k - 1][l - 1]

            inserts = D[k][l - 1] + 1
            deletes = D[k - 1][l] + 1

            lowest_cost = min(changes, inserts, deletes)

            D[k][l] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[k] == T[l]:
                    parents[k][l] = 'M'
                else: parents[k][l] = 'S'
            elif inserts < changes and inserts < deletes:
                parents[k][l] = 'I'
            else: parents[k][l] = 'D'
    return D[i][j], parents


def longest_shared_sequence(P, T, parents):
    i = len(parents) - 1
    j = len(parents[0]) - 1
    result = []
    curr = parents[i][j]

    while curr != 'X':
        if curr == 'M' or curr == 'S':
            i -= 1
            j -= 1
        elif curr == 'D':
            i -= 1
        else: j -= 1

        if curr == 'M':
            result.append((P[i + 1]))
        curr = parents[i][j]
    result.reverse()
    return ''.join(result)

def main():
    #a -------------------
    P = ' kot'
    T = ' pies'

    # t1 = time.perf_counter()
    # a = string_compare(P, T, 3, 4)
    # t2 = time.perf_counter()
    # print("{:.7f}".format(t1 - t2))

    print(string_compare(P, T, 3, 4))

    #b -------------------
    P = ' biały autobus'
    T = ' czarny autokar'
    # t1 = time.perf_counter()
    # a = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
    # t2 = time.perf_counter()
    # print("{:.7f}".format(t1 - t2))
    cost, parents = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
    print(cost)

    #c -------------------
    P = ' thou shalt not'
    T = ' you should not'
    cost, parents = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
    print(path_reconstruction(parents))

    #d -------------------
    P = ' ban'
    T = ' mokeyssbanana'
    begin_idx = string_compare_pd2(P, T, len(P) - 1, len(T) - 1)
    print(begin_idx)

    #e -------------------
    P = ' democrat'
    T = ' republican'
    cost, parents = string_compare_pd3(P, T, len(P) - 1, len(T) - 1)
    print(longest_shared_sequence(P, T, parents))

    #f ------------------
    T = ' 243517698'
    P = ' ' + ''.join(sorted(T))
    cost, parents = string_compare_pd3(P, T, len(P) - 1, len(T) - 1)
    print(longest_shared_sequence(P, T, parents))

if __name__ == '__main__':
    main()