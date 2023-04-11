from random import random
from typing import Any, List

#skonczone

class Element:
    def __init__(self, key: int, value: Any, maxlevel: int, levels: int = 0):
        self.key = key
        self.value = value
        self.maxlevel = maxlevel
        self.levels = levels
        self.next = [None for i in range(self.levels)]

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, levels: int):
        if levels == 0:
            p = 0.5
            lvl = 1
            while random() < p and lvl < self.maxlevel:
                lvl += 1
            self.__levels = lvl
        else:
            self.__levels = levels

    def __str__(self):
        return f'{self.key} : {self.value}'


class SkipList:
    def __init__(self, maxheight: int):
        self.maxheight = maxheight
        self.head = Element("HEAD", "HEAD", maxheight, maxheight)

    def update_list(self, key):
        update = [None for i in range(self.maxheight)]
        current = self.head

        for i in range(self.maxheight - 1, -1, -1):
            while current.next[i] and current.next[i].key < key:
                 current = current.next[i]
            update[i] = current
        
        return update

    def search(self, key: int, update: List = None):
        if update is None:
            update = self.update_list(key)
        
        current = update[0].next[0]
        if current is None or current.key != key:  # if element not found
            return None

        return f'{current}'

    def insert(self, elem: Element):
        if self.search(elem.key) is not None:
            self.remove(elem.key)
        
        update = self.update_list(elem.key)
        current = update[0].next[0]

        if current is None or current.key != elem.key:
            n = elem
            for i in range(n.levels):
                update[i].next[i] = n

    def remove(self, key: int):
        update = self.update_list(key)
        current = update[0].next[0]

        if current is not None and current.key == key:
            for i in range(self.maxheight):
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]

    def __str__(self):
        s = 'Head '
        current = self.head.next[0]
        s += str(current)
        s += ', '
        while current:
            if current.next[0] is None:
                break
            s += str(current.next[0])
            s += ', '
            current = current.next[0]

        return f'{s[:-2]}'

    def displayList_(self):
        head = self.head
        for lvl in range(self.maxheight - 1, -1, -1):
            print('Level {}: '.format(lvl), end=' ')
            node = head.next[lvl]
            while(node != None):
                print(node.key, end=' ')
                node = node.next[lvl]
            print('')


if __name__ == '__main__':
    HEIGHT = 6
    skip_list = SkipList(HEIGHT)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for num, letter in enumerate(l, start=1):
        skip_list.insert(Element(num, letter, HEIGHT))
    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(Element(2, 'Z', HEIGHT))
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.displayList_()
    skip_list.insert(Element(6, 'W', HEIGHT))
    skip_list.displayList_()