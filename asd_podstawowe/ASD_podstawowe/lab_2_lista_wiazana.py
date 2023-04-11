

class Element:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class BondList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        next_element = Element(data, self.head)
        self.head = next_element

    def remove(self):
        removing_element = self.head
        self.head = removing_element.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def lenght(self):
        coutrer = 0
        pointer = self.head
        while pointer is not None:
            pointer = pointer.next
            coutrer += 1
        return coutrer

    def get(self):
        return self.head.data

    def __str__(self):
        string = "["
        element = self.head
        for i in range(self.lenght()):
            string += str(element.data)
            element = element.next
            if element is not None:
                string += ", "
        string += "]"
        return string

    def add_to_end(self, data):
        added_element = Element(data)
        if self.is_empty():
            self.head = added_element
        else:
            pointer = self.head
            last = self.head
            while pointer is not None:
                last = pointer
                pointer = pointer.next
            last.next = added_element

    def remove_from_end(self):
        if not self.is_empty():
            pointer = self.head
            last = self.head
            while pointer.next is not None:
                last = pointer
                pointer = pointer.next
            last.next = None

    def take(self, n):
        lenght = self.lenght()
        if n > lenght:
            n = lenght

        new = BondList()
        element = self.head
        for i in range(n):
            new.add_to_end(element.data)
            element = element.next
        return new

    def drop(self, n):
        lenght = self.lenght()
        new = BondList()
        if n > lenght:
            return new
        element = self.head
        for i in range(n):
            element = element.next
        for j in range(lenght - n):
            new.add_to_end(element.data)
            element = element.next
        return new


if __name__ == '__main__':
    my_list = BondList()
    my_list.add(('PG', 'Gdańsk', 1945))
    my_list.add(('UP', 'Poznań', 1919))
    my_list.add(('UW', 'Warszawa', 1915))
    my_list.add(('PW', 'Warszawa', 1915))
    my_list.add(('UJ', 'Kraków', 1364))
    my_list.add(('AGH', 'Kraków', 1919))
    print(my_list)
    print(my_list.is_empty())
    print(my_list.lenght())
    print(my_list.get())

    my_list.remove()
    print(my_list)
    my_list.remove_from_end()
    print("Usunięcie elementu z konca:")
    print(my_list)
    my_list.add_to_end(('PG', 'Gdańsk', 1945))
    print("Dodanie elementu do konca:")
    print(my_list)
    my_list.add(('AGH', 'Kraków', 1919))

    taken_list = my_list.take(4)
    print("Test take()")
    print(taken_list)

    dropped_list = my_list.drop(3)
    print("Test drop()")
    print(dropped_list)
    my_list.destroy()