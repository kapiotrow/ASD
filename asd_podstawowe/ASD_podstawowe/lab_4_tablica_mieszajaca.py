class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def is_key_equal(self, key):
        if key == self.key:
            return True
        else:
            return False


class HashList:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def mix_fun(self, key):
        value = key
        if isinstance(key, str):
            value = 0
            for letter in key:
                value += ord(letter)
        return value % self.size

    def solve_colision_insert(self, index, key):
        for i in range(1, self.size+1):
            new_index = (index + (self.c1 * i) + (self.c2 * i**2)) % self.size
            if (self.tab[new_index] is None) or (self.tab[new_index].key is None) or (self.tab[new_index].is_key_equal(key)):
                return new_index
        return None

    def solve_colision_search(self, index, key):
        for i in range(1, self.size+1):
            new_index = (index + (self.c1 * i) + (self.c2 * i**2)) % self.size
            if self.tab[new_index] is None:
                return None
            elif (self.tab[new_index].key is not None) and (self.tab[new_index].is_key_equal(key)):
                return new_index
        return None

    def search_index(self, key):
        index = self.mix_fun(key)
        element = self.tab[index]
        if element is None:
            return None
        else:
            if (element.key is not None) and (element.is_key_equal(key)):
                return index
            else:
                new_index = self.solve_colision_search(index, key)
                return new_index

    def search(self,key):
        index = self.search_index(key)
        if index is None:
            return index
        else:
            return self.tab[index].data

    def insert(self, key, data):
        index = self.mix_fun(key)
        if (self.tab[index] is None) or (self.tab[index].key is None) or (self.tab[index].is_key_equal(key)):
            self.tab[index] = Element(key, data)
        else:
            new_index = self.solve_colision_insert(index, key)
            if new_index is None:
                raise MemoryError
            else:
                self.tab[new_index] = Element(key, data)

    def remove(self, key):
        index = self.search_index(key)
        if index is not None:
            self.tab[index].key = None

    def __str__(self):
        string = "["
        for i in range(self.size):
            if self.tab[i] is None:
                string += 'None, '
            else:
                string += '{' + str(self.tab[i].key) + ':' + str(self.tab[i].data) + '}' + ', '
        string += ']'
        string = string.replace(", ]", "]")
        return string


def fun_insert(lst, key, data):
    try:
        lst.insert(key, data)
    except MemoryError:
        print("Brak miejsca")


def first_test_function(keys, values, c1, c2):
    my_list = HashList(13, c1, c2)
    for i in range(15):
        fun_insert(my_list, keys[i], values[i])
    print(my_list)
    print(my_list.search(5))
    print(my_list.search(14))
    fun_insert(my_list, 5, 'Z')
    print(my_list.search(5))
    my_list.remove(5)
    print(my_list)
    print(my_list.search(31))
    fun_insert(my_list, "test", "W")
    print(my_list)


def second_test_function(values, c1, c2):
    my_second_list = HashList(13, c1, c2)
    for i in range(13):
        fun_insert(my_second_list, 13 + (13 * i), values[i])
    print(my_second_list)


keys = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
first_test_function(keys, values,1,0)

second_test_function(values,1,0)

second_test_function(values,0,1)
first_test_function(keys,values,0,1)
