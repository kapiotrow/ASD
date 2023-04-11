#!/usr/bin/python
# -*- coding: utf-8 -*-

#skończone

from copy import deepcopy

class Element:
    def __init__(self, node, next=None, prev=None) -> None:
        self.data = node
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f'->{self.data[0]} {self.data[1]} {self.data[2]}'
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def destroy(self) -> None:
        curr = self.head
        while curr != None:
            curr.prev = None
            curr = curr.next
        self.head = None

    def is_empty(self) -> bool:
        return self.head == None
    
    def length(self) -> int:
        l = 0
        curr = self.head
        while curr != None:
            l += 1
            curr = curr.next
        return l
    
    def get(self):
        if self.is_empty():
            raise IndexError('the list is empty!')
        return self.head.data

    def add(self, node: Element) -> None:
        node = Element(node, self.head)
        self.head = node

        if self.length() == 1:
            self.tail = node
    
    def append(self, node: Element) -> None:
        node = Element(node, prev=self.tail)

        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove(self) -> None:
        if self.is_empty():
            raise IndexError('the list is empty!')
        self.head = self.head.next

    def remove_end(self) -> None:
        if self.is_empty():
            raise IndexError('the list is empty!')
        if self.length() == 1:
            self.head = None
            return
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

    def __str__(self) -> str:
        curr = self.head
        result = ''
        while curr.next != None:
            result += '->' + str(curr.data) + '\n'
            curr = curr.next
        result += '->' + str(curr.data)
        return result

def main():
    uczelnie = LinkedList()
    list = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]

    uczelnie.add(list[2])
    uczelnie.add(list[1])
    uczelnie.add(list[0])

    uczelnie.append(list[3])
    uczelnie.append(list[4])
    uczelnie.append(list[5])

    print(uczelnie)
    print(uczelnie.length())

    uczelnie.remove()

    print(uczelnie.get())

    uczelnie.remove_end()

    print(uczelnie)

    uczelnie.destroy()

    print(uczelnie.is_empty())

if __name__ == '__main__':
    main()