from typing import Any

class Node:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

    def __str__(self):
        return f"{self.key} : {self.value} "
    

    
class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return (self.get_height(root.left) - self.get_height(root.right))
    
    def rotate_left(self, root):
        right = root.right
        left = right.left
        right.left = root
        root.right = left
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        right.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return right
    
    def rotate_right(self, root):
        left = root.left
        right = left.right
        right.right = root
        root.left = right
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        left.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return left
    
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

    def insert(self, node: Node, current=-1):
        if self.root is None:
            self.root = node
            return

        if current == -1:
            current = self.root
        
        if current is None:
            return node

        elif node.key < current.key:
            current.left = self.insert(node, current.left)

        elif node.key > current.key:
            current.right = self.insert(node, current.right)
        
        elif node.key == current.key:
            current.value = node.value

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

        #balancing         
        bf = self.get_balance(current)
        print(bf)
        if bf > 1:
            print('>1')
            if node.key < current.left.key:
                print('r')
                return self.rotate_right(current)
            else:
                current.left = self.rotate_left(current.left)
                print('lr')
                return self.rotate_right(current)               
        
        if bf < -1: 
            print('< -1')
            if node.key > current.right.key:
                print('l')
                return self.rotate_left(current)
            else:
                current.right = self.rotate_right(current.right)
                print('rl')
                return self.rotate_left(current)
        
        return
        
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

        if current is None:
            return current  

        current.height = 1 + max(self.get_height(current.right), self.get_height(current.right))

        bf = self.get_balance(current)

        if bf > 1:
            if self.get_balance(current.left) >= 0:
                return self.rotate_right(current)
            else:
                current.left = self.rotate_left(current.left)
                return self.rotate_right(current)
        if bf < -1:
            if self.get_balance(current.right) <= 0:
                return self.rotate_left(current)
            else:
                current.right = self.rotate_right(current.right)
                return self.rotate_left(current)

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
    tree = AVL()

    for k, v in {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 
                 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}.items():
        tree.insert(Node(k, v))
        print(k, v)
    
    tree.print_tree()
    tree.print()
    print()
    print(tree.search(10))
    tree.delete(50)
    tree.delete(52)
    tree.delete(11)
    tree.delete(57)
    tree.delete(1)
    tree.delete(12)
    tree.insert(Node(3, "AA"))
    tree.insert(Node(4, "BB"))
    tree.delete(7)
    tree.delete(8)
    tree.print()
    print()
    tree.print_tree()

if __name__ == '__main__':
    main()