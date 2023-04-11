#nie skonczone

from typing import Any

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
    

class Heap():
    def __init__(self):
        self.queue = []
        self.size = 0

    def right(self, i: int) -> int:
        return 2 * i + 2
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def is_empty(self) -> bool:
        return not bool(self.queue)
    
    def peek(self) -> Element:
        """returns element with the highest priority without modifying the queue"""
        if self.is_empty():
            return None
        return self.queue[0]
    
    def __heapify(self, start: int) -> None:
        left = self.left(start)
        right = self.right(start)
        largest = start

        if left <= self.size - 1 and self.queue[left] > self.queue[largest]:
            largest = left
        if right <= self.size - 1 and self.queue[right] > self.queue[largest]:
            largest = right

        if largest != start:
            self.queue[start], self.queue[largest] = self.queue[largest], self.queue[start]
            self.__heapify(largest)
    
    def dequeue(self) -> Element:
        if self.is_empty():
            return None
        
        temp = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue = self.queue[:-1]
        self.size -= 1

        self.__heapify(0)

        return temp
    
    def enqueue(self, element: Element) -> None:
        self.queue.append(element)
        curr__idx = self.size
        self.size += 1

        while curr__idx > 0 and self.queue[curr__idx] > self.queue[self.parent(curr__idx)]:
            self.queue[curr__idx], self.queue[self.parent(curr__idx)] = self.queue[self.parent(curr__idx)], self.queue[curr__idx]
            curr__idx = self.parent(curr__idx)
        
    def print_tab(self) -> None:
        if self.is_empty():
            print('{ }')
            return
        print ('{', end=' ')
        for i in range(self.size - 1):
            print(self.queue[i], end=', ')
        if self.queue[self.size - 1]:
            print(self.queue[self.size - 1], end=' ')
        print( '}')

    def print_tree(self, i: int, lvl: int) -> None:
        if i < self.size:
            self.print_tree(self.right(i), lvl + 1)
            print(2 * lvl * '  ', self.queue[i] if self.queue[i] else None)
            self.print_tree(self.left(i), lvl + 1)

def main():
    h = Heap()
    l = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    text = 'GRYMOTYLA'
    for i in range(len(l)):
        h.enqueue(Element(text[i], l[i]))
    h.print_tree(0, 0)
    h.print_tab()
    d = h.dequeue()
    print(h.peek())
    h.print_tab()
    print(d)
    while True:
        el = h.dequeue()
        if el is None:
            break
        print(el)
    h.print_tab()

if __name__ == '__main__':
    main()