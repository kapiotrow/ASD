class Element:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return str(self.priority) + ':' + str(self.data)

class Kopiec:
    def __init__(self):
        self.tab = []
        self.size = 0

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
        return self.tab[0].data

    def enqueue(self, data, priority):
        el = Element(data, priority)
        self.tab.append(el)
        self.size += 1
        el_index = self.size - 1
        next_index = self.parent(el_index)
        if next_index is not None:
            while el.priority > self.tab[next_index].priority:
                self.tab[el_index] = self.tab[next_index]
                self.tab[next_index] = el
                el_index = next_index
                next_index = self.parent(next_index)
                if next_index is None:
                    return None

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            self.size -= 1
            return self.tab.pop().data
        else:
            temp = self.peek()
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size-1] = temp
            result = self.tab.pop()
            self.size -= 1
            el = self.tab[0]
            el_index = 0
            next_index = 0
            right = self.right(next_index)
            left = self.left(next_index)
            if left is None:
                return result
            elif right is None:
                next_index = left
            elif self.tab[right].priority > self.tab[left].priority:
                next_index = right
            else:
                next_index = left
            if next_index is not None:
                while el.priority < self.tab[next_index].priority:
                    self.tab[el_index] = self.tab[next_index]
                    self.tab[next_index] = el
                    el_index = next_index
                    right = self.right(next_index)
                    left = self.left(next_index)
                    if left is None:
                        return result
                    elif right is None:
                        next_index = left
                    elif self.tab[right].priority > self.tab[left].priority:
                        next_index = right
                    else:
                        next_index = left
                    if next_index is None:
                        return result
            return result

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


kopiec = Kopiec()
keys = [4, 7, 6, 7, 5, 2, 2, 1]
values = ['A', 'L', 'G', 'O', 'R', 'Y', 'T', 'M']
for i in range(len(keys)):
    kopiec.enqueue(values[i], keys[i])
kopiec.print_tree(0, 0)
kopiec.print_tab()
print(kopiec.dequeue())
print(kopiec.peek())
kopiec.print_tab()
while not kopiec.is_empty():
    print(kopiec.dequeue())
kopiec.print_tree(0, 0)
