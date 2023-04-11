#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time


class Element:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __str__(self):
        return str(self.priority) + ':' + str(self.data)

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.priority > other.priority:
            return True
        else:
            return False


class Sorting:
    def __init__(self, tab):
        self.tab = tab
        self.size = len(tab)

    def swap_sort(self):
        for i in range(self.size):
            min = None
            index = 0
            for j in range(i, self.size):
                if min is None or min > self.tab[j]:
                    min = self.tab[j]
                    index = j
            temp = self.tab[i]
            self.tab[i] = min
            self.tab[index] = temp

    def shift_sort(self):
        for i in range(self.size):
            min = None
            index = 0
            for j in range(i, self.size):
                if min is None or min > self.tab[j]:
                    min = self.tab[j]
                    index = j
            self.tab.pop(index)
            self.tab.insert(i, min)

    def print_tab(self):
        if self.size == 0:
            print("{}")
        else:
            print('{', end=' ')
            for i in range(self.size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
            print('}')


test = [Element(5, 'A'), Element(5, 'B'), Element(7, 'C'), Element(2, 'D'), Element(5, 'E'), Element(1, 'F'),
        Element(7, 'G'), Element(5, 'H'), Element(1, 'I'), Element(2, 'J')]

sort = Sorting(test)
sort.swap_sort()
sort.print_tab()
# algorytm niestabilny

test = [Element(5, 'A'), Element(5, 'B'), Element(7, 'C'), Element(2, 'D'), Element(5, 'E'), Element(1, 'F'),
        Element(7, 'G'), Element(5, 'H'), Element(1, 'I'), Element(2, 'J')]

sort = Sorting(test)
sort.shift_sort()
sort.print_tab()
# algorytm stabilny


tested_list = []
for i in range(10000):
    tested_list.append(int(random.random() * 100))
t_start = time.perf_counter()
swap_test = Sorting(tested_list)
swap_test.swap_sort()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


tested_list = []
for i in range(10000):
    tested_list.append(int(random.random() * 100))
t_start = time.perf_counter()
shift_test = Sorting(tested_list)
shift_test.shift_sort()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
# sortowanie z przesunięciem jest nieco wolniejsze od "swap". Sortowanie przez wybieranie jest o wiele (kilka rzędów)
# wolniejsze od sortowania przez kopcowanie
