#skonczone

from typing import Any

class Node:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.key} : {self.value} "


class BST:
    def __init__(self):
        self.root = None
    
    def search(self, key: int, current: Node = -1) -> Any:
        if current == -1:
            current = self.root

        if current is None:
            return None

        if current.key == key:
            return current.value
        
        if key < current.key:
            return self.search(key, current=current.left)
        
        else: return self.search(key, current=current.right)
    
    def insert(self, node: Node, current=-1) -> None:
        if self.root is None:
            self.root = node
            print(node)
            return
        
        if current == -1:
            current = self.root
        
        if current.key == node.key:
            current.value = node.value
            return
        
        if node.key < current.key:
            if current.left is None:
                current.left = node
                return
            return self.insert(node, current.left)
        
        if node.key > current.key:
            if current.right is None:
                current.right = node
                return
            return self.insert(node, current.right)
        
    def delete(self, key: Any, current: Node = -1) -> None:
        if self.root is None:
            raise Exception('the tree is empty!')
        
        if current == -1:
            current = self.root
        
        if key < current.key:
            current.left = self.delete(key, current.left)
            return current
        
        elif key > current.key:
            current.right = self.delete(key, current.right)
        
        else:
            #case 1: no children
            if current.left is None and current.right is None:
                current = None

            #case 2: only one child
            elif current.left is None:
                current = current.right
            
            elif current.right is None:
                current = current.left
            
            #case 3: two children
            else:
                min_larger = current.right
                while min_larger.left is not None:
                    min_larger = min_larger.left

                temp = min_larger.key

                current.key = min_larger.key
                current.value = min_larger.value

                current.right = self.delete(temp, current.right)

        return current
    
    def height(self, root: int = -1) -> int:
        if root == -1:
            root = self.root
        
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

    def print(self):
        return self.__print(self.root)

    def __print(self, current):
        if current.left:
            self.__print(current.left)
        
        print(f"{current.key} : {current.value}", end=', ')

        if current.right:
            self.__print(current.right)


def main():
    tree = BST()

    for k, v in {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K',
                 24: 'L'}.items():
        tree.insert(Node(k, v))
    
    tree.print_tree()
    tree.print()
    print(tree.search(24))
    tree.insert(Node(20, "AA"))
    tree.insert(Node(6, "M"))
    tree.delete(62)
    tree.insert(Node(59, "N"))
    tree.insert(Node(100, "P"))
    tree.delete(8)
    tree.delete(15)
    tree.insert(Node(55, "R"))
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print()
    print(tree.height())
    print()
    tree.print()
    print()
    tree.print_tree()

if __name__ == '__main__':
    main()