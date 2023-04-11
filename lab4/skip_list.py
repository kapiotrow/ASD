from random import random

class Element:
    def __init__(self, key, val, maxlevel, levels=0):
        self.next = [None for i in range(levels)]
        self.lvls = levels
        self.key = key
        self.val = val
        self.maxlvl = maxlevel

    def levels(self):
        return self.lvls
    
    def levels(self, levels):
        if levels == 0:
            p = 0.5
            lvl = 1
            while random() < p and lvl < self.maxlvl:
                lvl += 1
            self.lvls = lvl
        else:
            self.lvls = levels
    
    def __str__(self):
        return f'{self.key} : {self.val}'
    
class SkipList:
    def __init__(self, maxh):
        self.maxh = maxh
        self.head = Element("Head", "Head", maxh, maxh)

    def update_list(self, key):
        update = [None for i in range(len(self.head.next))]
        current = self.head

        for i in range(len(self.head.next) - 1, -1, -1):
            while current.next[i] and current.next[i].key < key:
                 current = current.next[i]
            update[i] = current
        
        return update
    
    def search(self, key, update=None):
        if update is None:
            update = self.update_list(key)
        if len(update) > 0:
            current = update[0].next[0]
            if current is not None and current.key == key:
                return current
        return None
    
    def remove(self, key):
        update = self.update_list(key)
        current = self.search(key, update)
        if current is not None:
            for i in range(len(current.next), -1, -1):
                update[i].next[i] = current.next[i]
                if self.head is None:
                    self.maxh -= 1

    def insert(self, elem): 
        while len(self.head.next) < len(elem.next):
            self.head.next.append(None)
        update = self.update_list(elem.key)
        if self.search(elem.key, update) is None:
            for i in range(len(elem.next)):
                elem.next[i] = update[i].next[i]
                elem.val = update[i].val
                update[i].next[i] = elem

    def __str__(self) -> str:
        s = 'HEAD '
        current = self.head.next[0]
        s = s + str(current) + ', '
        while current:
            if current.next[0] is None:
                break
            s = s + str(current.next[0]) + ', '
            current = current.next[0]
        return f'{s[:-2]}'
    
    def display_list(self):
        current = self.head.next[0]
        keys = []
        while current:
            keys.append(current.key)
            current = current.next[0]

        for lvl in range(self.maxh - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            current = self.head.next[lvl]
            i = 0
            while current:
                while current.key > keys[i]:
                    print("  ", end=" ")
                    i += 1
                i += 1
                print("{:2d}".format(current.key), end=" ")
                current = current.next[lvl]
            print("")

def main():
    HEIGHT = 6
    skip_list = SkipList(HEIGHT)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1, 16):
        skip_list.insert(Element(i, letters[i - 1], HEIGHT))
    skip_list.display_list()
    print(skip_list.search(2))
    skip_list.insert(Element(2, "Z", HEIGHT))
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.display_list()
    skip_list.insert(Element(6, "W", HEIGHT))
    skip_list.display_list()

if __name__ == '__main__':
    main()