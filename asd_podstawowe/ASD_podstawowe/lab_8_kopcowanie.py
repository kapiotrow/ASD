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


class Kopiec:
    def __init__(self, tab=None):
        if tab is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = tab
            self.size = len(tab)
            self.heapify()

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def left(self, index):
        result = 2*index + 1
        if result > self.size - 1:
            return None
        else:
            return result

    def right(self, index):
        result = 2*index + 2
        if result > self.size - 1:
            return None
        else:
            return result

    def parent(self, index):
        result = (index+1)//2 - 1
        if result < 0:
            return None
        else:
            return result

    def peek(self):
        return self.tab[0]

    def enqueue(self, el):
        self.tab.append(el)
        self.size += 1
        el_index = self.size - 1
        next_index = self.parent(el_index)
        if next_index is not None:
            while el > self.tab[next_index]:
                self.tab[el_index] = self.tab[next_index]
                self.tab[next_index] = el
                el_index = next_index
                next_index = self.parent(next_index)
                if next_index is None:
                    return None

    def repear(self, index):
        el = self.tab[index]
        el_index = index
        next_index = index
        right = self.right(next_index)
        left = self.left(next_index)
        if left is None or left > self.size - 1:
            return None
        elif right is None or right > self.size - 1:
            next_index = left
        elif self.tab[right] > self.tab[left]:
            next_index = right
        else:
            next_index = left
        if next_index is not None and next_index < self.size:
            while el < self.tab[next_index]:
                self.tab[el_index] = self.tab[next_index]
                self.tab[next_index] = el
                el_index = next_index
                right = self.right(next_index)
                left = self.left(next_index)
                if left is None or left > self.size - 1:
                    return None
                elif right is None or right > self.size - 1:
                    next_index = left
                elif self.tab[right] > self.tab[left]:
                    next_index = right
                else:
                    next_index = left
        return None

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            self.size -= 1
            return self.tab.pop()
        else:
            temp = self.peek()
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size-1] = temp
            result = self.tab.pop()
            self.size -= 1
            self.repear(0)
            return result

    def heapify(self):
        last = self.parent(self.size - 1)
        for i in range(- last, 1):
            i = i * (-1)
            self.repear(i)

    def sort_tab(self):
        size = self.size
        while self.size > 1:
                temp = self.peek()
                self.tab[0] = self.tab[self.size-1]
                self.tab[self.size - 1] = temp
                self.size -= 1
                self.repear(0)
        self.size = size

    def print_tab(self):
        if self.size == 0:
            print("{}")
        else:
            print('{', end=' ')
            for i in range(self.size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if self.size == 0:
            print("{}")
        elif idx is not None:
            if idx < self.size:
                self.print_tree(self.right(idx), lvl + 1)
                print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
                self.print_tree(self.left(idx), lvl + 1)


test = [Element(5, 'A'), Element(5, 'B'), Element(7, 'C'), Element(2, 'D'), Element(5, 'E'), Element(1, 'F'), Element(7, 'G'), Element(5, 'H'), Element(1, 'I'), Element(2, 'J')]
#wizualizacja nieposortowanej listy
unsorted = Kopiec()
unsorted.tab = test
unsorted.size = 10
unsorted.print_tab()
unsorted.print_tree(0,0)
print('\n')

#właściwe sortowanie
tab_to_sort = Kopiec(test)
tab_to_sort.print_tree(0,0)
tab_to_sort.sort_tab()
tab_to_sort.print_tab()
# algorytm niestabilny

tested_list = []
for i in range(10000):
    tested_list.append(int(random.random() * 100))
t_start = time.perf_counter()
second = Kopiec(tested_list)
second.sort_tab()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
