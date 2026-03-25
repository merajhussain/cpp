from tree_node import TreeNode
import io
from contextlib import redirect_stdout

IN_ORDER = 1
PRE_ORDER = 2
POST_ORDER = 3


class binary_search_tree:
    def __init__(self):
        self.root= None

    def __insert_node(self, data, current):
        if current is None:
            return TreeNode(data)

        if data < current.data:
            current.left = self.__insert_node(data, current.left)
        else:
            current.right = self.__insert_node(data, current.right)

        return current

    def insert_node(self, data):
        self.root = self.__insert_node(data, self.root)

    def in_order(self,root=None):
        if root is None:
            return

        self.in_order(root.left)
        print(root.data,end="")
        if root.right:
            print("->", end="")
        self.in_order(root.right)

    def preorder(self,root=None):
        if root is None:
            return

        print(root.data, end="")
        if root.left or root.right:
            print("->", end="")
        self.preorder(root.left)
        self.preorder(root.right)


    def postorder(self,root=None):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        if root.left or root.right:
            print("->", end="")
        print(root.data, end="")

    def print_tree(self,order=IN_ORDER):
        if order == IN_ORDER:
            self.in_order(self.root)
        if order == PRE_ORDER:
            self.preorder(self.root)
        if order == POST_ORDER:
            self.postorder(self.root)

    def search_key(self,data,current=None):
        if current is None:
            return False
        if current.data == data:
            return True
        if current.data > data:
            return self.search_key(data,current.left)
        else:
            return self.search_key(data,current.right)



    def search(self,data):
        return self.search_key(data,self.root)

    def to_string(self,order=IN_ORDER):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.print_tree(order)
        return buffer.getvalue().strip()
