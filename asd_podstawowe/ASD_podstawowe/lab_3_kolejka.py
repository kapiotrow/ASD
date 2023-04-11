def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]


class Queue:
    def __init__(self, size = 5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.front = 0
        self.back = 0

    def is_empty(self):
        if self.front == self.back:
            return True
        else:
            return False

    def peek(self):
        result = self.tab[self.front]
        return result

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            result = self.peek()
            self.front += 1
            if self.front == self.size:
                self.front = 0
            return result

    def enqueue(self, data):
        self.tab[self.back] = data
        self.back += 1
        if self.back == self.size:
            self.back = 0
        if self.back == self.front:
            self.tab = realloc(self.tab, self.size * 2)
            old_size = self.size
            self.size = self.size * 2
            last_one = self.size
            for i in range(self.front, old_size):
                i = old_size - i
                self.tab[last_one - 1] = self.tab[i]
                last_one -= 1
            self.front = last_one

    def __str__(self):
        string = "["
        if self.front < self.back:
            for i in range(self.front, self.back):
                if self.tab[i] is not None:
                    string += str(self.tab[i]) + " "
        elif self.front > self.back:
            for i in range(self.front, self.size):
                if self.tab[i] is not None:
                    string += str(self.tab[i]) + " "
            for i in range(self.back):
                if self.tab[i] is not None:
                    string += str(self.tab[i]) + " "
        return string + "]"

    def tab_to_str(self):
        string = "["
        for i in range(self.size):
            string += str(self.tab[i]) + " "
        return string + "]"


test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.enqueue(4)
print(str(test.dequeue()))
print(str(test.peek()))
print(test)
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
test.enqueue(8)
print(test.tab_to_str())
while not test.is_empty():
    print(str(test.dequeue()))
print(test)
