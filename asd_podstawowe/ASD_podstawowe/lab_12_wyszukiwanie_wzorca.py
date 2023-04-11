import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()


def naive(s, w):
    i = 0
    m = 0
    compare = 0
    pattern = 0
    p_list = []
    while m + len(w) < len(s) + 1:
        found = True
        i = 0
        while i < len(w):
            compare += 1
            if not s[m + i] == w[i]:
                found = False
                break
            else:
                i += 1
        if found:
            pattern += 1
            p_list.append(m)
        m += 1
    return compare, pattern, p_list


def hash(w, q):
    hw = 0
    d = 256
    for i in range(len(w)):
        hw = (hw * d + ord(w[i])) % q
    return hw


def rabin_karp(s, w):
    d = 256
    q = 101
    h = 1
    n = len(w)
    for i in range(n - 1):
        h = (h * d) % q
    hw = hash(w, q)
    m = 0
    compare = 0
    pattern = 0
    colision = 0
    hs = 0
    while m + n < len(s) + 1:
        compare += 1
        if m == 0:
            hs = hash(s[0: 0 + n], q)
        else:
            hs = (d * (hs - ord(s[m - 1]) * h) + ord(s[m - 1 + n])) % q
        if hs < 0:
            hs += q
        if hs == hw:
            if s[m: m + n] == w:
                pattern += 1
            else:
                colision += 1
        m += 1
    return compare, pattern, colision


def kmp_t(w):
    pos = 1
    cnd = 0
    t = [0 for i in range(len(w))]
    t[0] = -1
    while pos < len(w):
        if w[pos] == w[cnd]:
            t[pos] = t[cnd]
        else:
            t[pos] = cnd
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = t[cnd]
        pos += 1
        cnd += 1
    return t


def kmp(s, w):
    i = 0
    m = 0
    t = kmp_t(w)
    compare = 0
    pattern = 0
    p_list = []
    n = len(w)
    while m < len(s):
        compare += 1
        if w[i] == s[m]:
            m += 1
            i += 1
            if i == n:
                p_list.append(m - i)
                pattern += 1
                i = 0
        else:
            i = t[i]
            if i < 0:
                m += 1
                i += 1
    return compare, pattern, p_list


def make_string(a,b,c=None):
    result = str(a) + "; " + str(b)
    if c:
        result += "; " + str(c)
    return result

#print("Naiwny")
#t_start = time.perf_counter()
c, p, l = naive(S, "time.")
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(make_string(p,c))

#print("Rabin_karp")
#t_start = time.perf_counter()
c, p, colision = rabin_karp(S, "time.")
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(make_string(p,c, colision))

#print("kmp")
#t_start = time.perf_counter()
c, p, li = kmp(S, "time.")
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(make_string(p,c))
