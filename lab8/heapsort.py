#nie skonczone

from typing import Any, List
import random
import time

class Element():
    def __init__(self, data: Any, priority: int):
        self.data = data
        self.priority = priority

    def __lt__(self, other) -> bool:
        return self.priority < other.priority
    
    def __gt__(self, other) -> bool:
        return self.priority > other.priority
    
    def __str__(self) -> str:
        return f'{self.priority} : {self.data}'
    
    def __repr__(self) -> str:
        return f'{self.priority} : {self.data}'
    

class Heap():
    def __init__(self, array: List=None):
        self.size = len(array)
        if array is None:
            self.array = [0]
        else:
            self.array = array
            for i in range(self.size // 2, -1, -1):
                self.__heapify(self.size, i)

    def right(self, i: int) -> int:
        return 2 * i + 2
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def is_empty(self) -> bool:
        return not bool(self.array)
    
    def peek(self) -> Element:
        """returns element with the highest priority without modifying the array"""
        if self.is_empty():
            return None
        return self.array[0]
    
    def __heapify(self, len: int, start: int) -> None:
        left = self.left(start)
        right = self.right(start)
        largest = start

        if left <= len - 1 and self.array[left] > self.array[largest]:
            largest = left
        if right <= len- 1 and self.array[right] > self.array[largest]:
            largest = right

        if largest != start:
            self.array[start], self.array[largest] = self.array[largest], self.array[start]
            self.__heapify(len, largest)

    def heapsort(self):
        for i in range(self.size - 1, -1, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.__heapify(i, 0)
    
    # def dequeue(self) -> Element:
    #     if self.is_empty():
    #         return None
        
    #     temp = self.queue[0]
    #     self.queue[0] = self.queue[-1]
    #     self.queue = self.queue[:-1]
    #     self.size -= 1

    #     self.__heapify(0)

    #     return temp
    
    # def enqueue(self, element: Element) -> None:
    #     self.queue.append(element)
    #     curr__idx = self.size
    #     self.size += 1

    #     while curr__idx > 0 and self.queue[curr__idx] > self.queue[self.parent(curr__idx)]:
    #         self.queue[curr__idx], self.queue[self.parent(curr__idx)] = self.queue[self.parent(curr__idx)], self.queue[curr__idx]
    #         curr__idx = self.parent(curr__idx)
        
    def print_tab(self) -> None:
        if self.is_empty():
            print('{ }')
            return
        print ('{', end=' ')
        for i in range(self.size - 1):
            print(self.array[i], end=', ')
        if self.array[self.size - 1]:
            print(self.array[self.size - 1], end=' ')
        print( '}')

    def print_tree(self, i: int, lvl: int) -> None:
        if i < self.size:
            self.print_tree(self.right(i), lvl + 1)
            print(2 * lvl * '  ', self.array[i] if self.array[i] else None)
            self.print_tree(self.left(i), lvl + 1)



def selection_sort(array: List) -> None:
    for i in range(len(array)):
        jmin = i
        for j in range(i + 1, len(array)):
            if array[j] < array[jmin]:
                jmin = j
        if jmin != i:
            array[i], array[jmin] = array[jmin], array[i]
    


def main():
    #heapsort-----------------
    l =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab = []
    for i in range(len(l)):
        tab.append(Element(l[i][1], l[i][0]))
    heap = Heap(tab)
    heap.print_tab()
    heap.print_tree(0, 0)
    heap.heapsort()
    heap.print_tab()
    print('Kolejność elementów o tym samy  priorytecie nie jest zachowana - sortowanie nie jest stabilne')

    r = [int(random.random() * 100) for _ in range(10000)]
    t1 = time.perf_counter()
    heap2 = Heap(r)
    heap2.heapsort()
    t2 = time.perf_counter()
    heap_time = t1 - t2
    print("Czas obliczeń:", "{:.7f}".format(heap_time))


    #selection sort-------------
    l =  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab = []
    for i in range(len(l)):
        tab.append(Element(l[i][1], l[i][0]))
    selection_sort(tab)
    print('array after selection sort: ', tab)
    print('Kolejność elementów o tym samym priorytecie jest zachowana - sortowanie jest stabilne')

    r = [int(random.random() * 100) for _ in range(10000)]
    t1 = time.perf_counter()
    selection_sort(r)
    t2 = time.perf_counter()
    selection_time = t1 - t2
    print("Czas obliczeń:", "{:.7f}".format(selection_time))

    print('Heapsort jest szybszy o {:.7f}'.format(heap_time - selection_time))
    

if __name__ == '__main__':
    main()