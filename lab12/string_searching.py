import time


with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()


def naive(S, W):
    m = 0 #index of S
    i = 0 #index of W
    comparison = 0
    found_pattern_idx = []

    while m + len(W) <= len(S):
        comparison += 1
        if S[i:m + len(W)] == W:
            found_pattern_idx.append(m)
        m += 1
        i += 1
    return comparison, found_pattern_idx


def hash(word):
    d = 256
    q = 101
    N = len(word)
    hw = 0

    for i in range(N):
        hw = (hw * d + ord(word[i])) % q
    return hw


def rabin_karp(S, W):
    M = len(S)
    N = len(W)
    hw = hash(W)
    comparisons = 0
    collisions = 0
    found_pattern_idx = []
    d = 256
    q = 101
    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    m = 0
    hs = hash(S[m:m + N])
    while m < M - N + 1:
        comparisons += 1
        if hs == hw:
            if S[m:m + N] == W:
                found_pattern_idx.append(m)
            else:
                collisions += 1
        if m + N < M:
            hs = (d * (hs - ord(S[m]) * h) + ord(S[m + N])) % q
        m += 1
    return comparisons, found_pattern_idx, collisions


def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for i in range(len(W) + 1)]
    T[0] = -1

    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd

    return T


def kmp(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    P = []
    np = 0
    comparisons = 0

    while m < len(S):
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - i)
                np += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return comparisons, P, T


def main():
    W = 'time.'

    t_start = time.perf_counter()
    comps, idx = naive(S, W)
    t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('{}; {}'.format(len(idx), comps))

    t_start = time.perf_counter()
    comps, idx, cols = rabin_karp(S, W)
    t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('{}; {}; {}'.format(len(idx), comps, cols))

    t_start = time.perf_counter()
    comps, P, T = kmp(S, W)
    t_stop = time.perf_counter()
    #print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('{}; {}; {}'.format(len(P), comps, T))



if __name__ == '__main__':
      main()