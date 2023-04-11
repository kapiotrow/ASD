#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, len=5) -> None:
        self.size = len
        self.num_elem = 0
        self.tab = [None for i in range(len)]
        self.next = None

    def insert(self, elem, index) -> None:
        if index >= self.size:
            raise IndexError('index out of range!')
        self.tab.insert(index, elem)
        self.num_elem += 1
        if self.num_elem > self.size:
            next_node = Node()
            next_node.tab[0] = self.tab[-1]
            self.tab.pop(-1)
            self.nex = next_node
            next_node.num_elem += 1

    def is_empty(self) -> bool:
        return not self.num_elem
    
    def remove(self, elem, index) -> None:
        if self.is_empty:
            raise Exception('the list is empty!')
        if index >= self.size:
            raise IndexError('index out of range!')
        self.tab.pop(index)
        self.num_elem -= 1