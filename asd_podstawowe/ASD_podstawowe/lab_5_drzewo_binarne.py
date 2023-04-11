class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def children(self):  # sprawdza jakie dzieci ma element
        right = False
        left = False
        if self.right is not None:
            right = True
        if self.left is not None:
            left = True
        return left, right


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        def insert_in(node):
            if node is None:
                return Element(key, value)
            if key > node.key:
                node.right = insert_in(node.right)
                return node
            elif key < node.key:
                node.left = insert_in(node.left)
                return node
            else:
                node.value = value
                return node

        if self.root is None:
            self.root = Element(key, value)
        else:
            node = self.root
            insert_in(node)

    def search_parent(self, key):  # poszukuje danego elementu oraz jego rodzica
        def search_in(node):
            if node is None:
                return node, node, node
            if (node.left is not None) and (key == node.left.key):
                return node, node.left, False
            if (node.right is not None) and (key == node.right.key):
                return node, node.right, True
            if key > node.key:
                result = search_in(node.right)
                return result
            elif key < node.key:
                result = search_in(node.left)
                return result

        if self.root is None:
            return None, None, None  # zdaje sobie sprawe że to jest słabe, ale walcze z tym już naprawde długo...
        if self.root.key == key:
            return self.root, self.root, False
        return search_in(self.root)

    def search(self, key):
        def search_in(node):
            if node is None:
                return node
            if key > node.key:
                result = search_in(node.right)
                return result
            elif key < node.key:
                result = search_in(node.left)
                return result
            else:
                return node

        if self.root is None:
            return None
        node = self.root
        node = search_in(node)
        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):  # , że tak, zdaje sobie sprawępewnie można lepiej, ale działa(o dziwo)
        parent, node, right_child = self.search_parent(key)  # parent-rodzic usuwanego elementu(node),
        # right_child-zmienna boolowska przenosząca informacje czy usuwany element jest prawym czy lewym dzieckiem
        # rodzica
        if node is not None:
            if parent == self.root:
                left, right = node.children()
                if (not left) and (not right):  # usunięcie elementu bez dzieci
                    if right_child:
                        self.root.right = None
                    elif not right_child:
                        self.root.left = None
                elif left and right:  # usunięcie elementu dwojga dzieci
                    child = node.right
                    childs_parent = node
                    is_left = False
                    while child.left:
                        childs_parent = child
                        child = childs_parent.left
                        is_left = True
                    node.value = child.value
                    node.key = child.key
                    if is_left:
                        childs_parent.left = child.right
                    else:
                        childs_parent.right = child.right
                else:  # usunięcie elementu z jednym dzieckiem
                    if left:
                        if right_child:
                            self.root.right = node.left
                        elif not right_child:
                            self.root.left = node.left
                    elif right:
                        if right_child:
                            self.root.right = node.right
                        elif not right_child:
                            self.root.left = node.right
            else:
                left, right = node.children()
                if (not left) and (not right):  # usunięcie elementu bez dzieci
                    if right_child:
                        parent.right = None
                    elif not right_child:
                        parent.left = None
                elif left and right:  # usunięcie elementu dwojga dzieci
                    child = node.right
                    childs_parent = node
                    is_left = False
                    while child.left:
                        childs_parent = child
                        child = childs_parent.left
                        is_left = True
                    node.value = child.value
                    node.key = child.key
                    if is_left:
                        childs_parent.left = child.right
                    else:
                        childs_parent.right = child.right
                else:  # osieracam jedno dziecko :(
                    if left:
                        if right_child:
                            parent.right = node.left
                        elif not right_child:
                            parent.left = node.left
                    elif right:
                        if right_child:
                            parent.right = node.right
                        elif not right_child:
                            parent.left = node.right

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self._print_tree(node.left, lvl + 5)

    def __str__(self):
        def visit(node, lst=None):
            if lst is None:
                lst = []
            if node:
                visit(node.left, lst)
                lst.append(node)
                visit(node.right, lst)
                return lst
        string = "["
        lst = visit(self.root)
        for el in lst:
            string += str(el.key) + ":" + str(el.value) + ", "
        string += "]"
        string = string.replace(", ]", "]")
        return string

    def print(self):
        print(self)

    def height(self):
        def visit(node, counter=0, remember=0):
            if node:
                counter += 1
                if counter > remember:
                    remember = counter
                remember = visit(node.left, counter, remember)
                remember = visit(node.right, counter, remember)
                counter -= 1
            return remember
        return visit(self.root)


tree = Tree()
tree.insert(50, 'A')
tree.insert(15, 'B')
tree.insert(62, 'C')
tree.insert(5, 'D')
tree.insert(20, 'E')
tree.insert(58, 'F')
tree.insert(91, 'G')
tree.insert(3, 'H')
tree.insert(8, 'I')
tree.insert(37, 'J')
tree.insert(60, 'K')
tree.insert(24, 'L')
tree.print_tree()
tree.print()
print(tree.search(24))
tree.insert(20, 'AA')
tree.insert(6, 'M')
tree.delete(62)
tree.insert(59, 'N')
tree.insert(100, 'P')
tree.delete(8)
tree.delete(15)
tree.insert(55, 'R')
tree.delete(50)
tree.delete(5)
tree.delete(24)
print(tree.height())
tree.print()
tree.print_tree()