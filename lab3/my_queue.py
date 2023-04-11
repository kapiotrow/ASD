#!/usr/bin/python
# -*- coding: utf-8 -*-

#skonczone

def realloc(tab, size):
    old_size = len(tab)
    return [tab[i] if i<old_size else None  for i in range(size)]

class Queue:
    def __init__(self, len=5) -> None:
        self.tab = [None for i in range(len)]
        self.size = len
        self.write = 0
        self.read = 0

    def is_empty(self) -> bool:
        return self.write == self.read
    
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read]
    
    def dequeue(self):
        if self.is_empty():
            return None
        self.read += 1
        if self.read == self.size:
            self.read = 0
        return self.tab[self.read  - 1]
    
    def enqueue(self, elem):
        self.tab[self.write] = elem
        self.write += 1
        if self.write == self.size:
            self.write = 0
        if self.write == self.read:
            self.tab = realloc(self.tab, self.size * 2)
            for i in range(self.write, self.size):
                self.tab[i + self.size] = self.tab[i]
            self.read += self.size
            self.size = self.size * 2

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'
        return f'{self.tab}'
    
    def show_queue(self) -> str:
        s = ''

        current_element = self.read
        while self.tab[current_element] is not None:
            s += f'{str(self.tab[current_element])} '
            if current_element == self.size - 1:
                current_element = 0
            else:
                current_element += 1

        return s

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.dequeue())

    print(q.peek())

    print(q.show_queue())

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)

    print(q)

    while not q.is_empty():
        print(q.dequeue())
    
    print(q)


if __name__ == '__main__':
    main()