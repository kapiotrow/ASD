from typing import Any, List
import random
from copy import deepcopy
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



def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            j = j - 1
        elem = array.pop(i)
        array.insert(j + 1, elem)
    return array


def knuth(array):
    gap = 1
    while gap < len(array) / 3:
        gap = gap * 3 + 1
    return gap


def shell_sort(array):
    h = knuth(array)
    while h > 0:
        for i in range(h, len(array)):
            temp = array[i]
            j = i
            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h

            array[j] = h
        h //= 3


def main():
    r1 = [int(random.random() * 100) for _ in range(10000)]
    r2 = deepcopy(r1)
    r3 = deepcopy(r1)
    r4 = deepcopy(r1)

    t1 = time.perf_counter()
    heap = Heap(r1)
    heap.heapsort()
    t2 = time.perf_counter()
    heap_time = t1 - t2
    print("Czas obliczeń dla heapsort:", "{:.7f}".format(heap_time))


    t1 = time.perf_counter()
    insertion_sort(r2)
    t2 = time.perf_counter()
    insert_time = t1 - t2
    print("Czas obliczeń dla insert sort:", "{:.7f}".format(insert_time))

    t1 = time.perf_counter()
    shell_sort(r3)
    t2 = time.perf_counter()
    shell_time = t1 - t2
    print("Czas obliczeń dla shell sort:", "{:.7f}".format(shell_time))

if __name__ == '__main__':
    main()