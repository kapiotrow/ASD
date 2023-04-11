from typing import TypeVar

REMOVED = TypeVar("REMOVED")

class Element:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return f"{self.key} : {self.val}"


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
    
    def hash(self, key) -> int:
        if isinstance(key, str):
            key = sum([ord(c) for c in key])
        return key % len(self.tab)
    
    def search(self, key):
        i = self.hash(key)
        if self.tab[i] is None:
            return None
        if isinstance(self.tab[i], Element) and self.tab[i].key == key:
            return self.tab[i].val
        for j in range(1, len(self.tab)):
            new_i = (i + self.c1 * j + self.c2 * i ** 2) % len(self.tab)
            if self.tab[new_i] is not None and  self.tab[new_i] is not REMOVED and self.tab[new_i].key == key:
                return self.tab[new_i].val
        return None
    
    def resolve_conflict(self, elem):
        i = self.hash(elem.key)
        for j in range(1, len(self.tab)):
            new_i = (i + self.c1 * j + self.c2 * i ** 2) % len(self.tab)
            if isinstance(self.tab[new_i], Element) and self.tab[new_i].key == elem.key:
                self.tab[new_i] = elem
                return
            if self.tab[new_i] is None or self.tab[new_i] is REMOVED:
                self.tab[new_i] = elem
                return
        raise Exception("the list if full!")
    
    def insert(self, elem):
        i = self.hash(elem.key)
        if self.tab[i] is None or self.tab[i] is REMOVED:
            self.tab[i] = elem
            return
        if isinstance(self.tab[i], Element) and self.tab[i].key == elem.key:
            self.tab[i] = elem
            return
        self.resolve_conflict(elem)

    def remove(self, key):
        i = self.hash(key)
        if self.tab[i] is None:
            return None
        if isinstance(self.tab[i], Element) and self.tab[i].key == key:
            self.tab[i] = REMOVED
            return
        for j in range(1, len(self.tab)):
            new_i = (i + self.c1 * j + self.c2 * i ** 2) % len(self.tab)
            if isinstance(self.tab[new_i], Element) and self.tab[new_i].key == key:
                self.tab[new_i] = REMOVED
                return
        raise Exception("element not in the list!")
    
    def __str__(self) -> str:
        result = '{'
        for elem in self.tab:
            result += str(elem)
            result += ', '
        result += '}'
        return result
    
def test1():
    t = HashTable(13)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for num, letter in enumerate(l, start=1):
        try:
            if num == 6:
                t.insert(Element(18, letter))
                continue
            if num == 7:
                t.insert(Element(31, letter))
                continue
            t.insert(Element(num, letter))
        except Exception:
            print('the list is full!!')

    print(t)
    print(t.search(5))
    print(t.search(14))
    t.insert(Element(5, 'Z'))
    print(t.search(5))
    t.remove(5)
    print(t)
    print(t.search(31))

def test2():
    t = HashTable(13)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for num, letter in enumerate(l, start=1):
        try:
            t.insert(Element(num * 13, letter))
        except Exception:
            print('the list is full!!')

    print(t)

def test3():
    t = HashTable(13, c1=0, c2=1)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for num, letter in enumerate(l, start=1):
        try:
            t.insert(Element(num * 13, letter))
        except Exception:
            print('the list is full!!')

    print(t)

def test4():
    t = HashTable(13, c1=0, c2=1)
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for num, letter in enumerate(l, start=1):
        try:
            if num == 6:
                t.insert(Element(18, letter))
                continue
            if num == 7:
                t.insert(Element(31, letter))
                continue
            t.insert(Element(num, letter))
        except Exception:
            print('the list is full!!')

    print(t)
    print(t.search(5))
    print(t.search(14))
    t.insert(Element(5, 'Z'))
    print(t.search(5))
    t.remove(5)
    print(t)
    print(t.search(31))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()