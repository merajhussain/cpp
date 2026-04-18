
from my_queue import my_queue
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
        print(root.data, end="->")
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


    def is_bst_tree_helper(self,root):
        if  root is None:
            return True
        if root.left:
            if root.left.data > root.data:
                return False
        if root.right:
            if root.right.data < root.data:
                return False
        return self.is_bst_tree_helper(root.left) and self.is_bst_tree_helper(root.right)

    def is_bst_tree(self):
        if self.root is None:
            return True
        return self.is_bst_tree_helper(self.root)

    def search(self,data):
        return self.search_key(data,self.root)

    def to_string(self,order=IN_ORDER):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.print_tree(order)
        return buffer.getvalue().strip()

    def dfs(self):
        if self.root is None:
            return

        queue = my_queue()
        current = self.root
        queue.enqueue(current)

        s=""
        while not queue.is_empty():
            level_size = queue.size()

            for _ in range(level_size):
                item = queue.dequeue()
                s += str(item.data)

                if item.left is not None:
                    queue.enqueue(item.left)
                if item.right is not None:
                    queue.enqueue(item.right)

            s += "|"
        return s

    def __tree_height(self,root=None):
        if root is None:
            return -1
        lh= self.__tree_height(root.left)
        rh= self.__tree_height(root.right)
        return max(lh,rh)+1


    def height(self):
        return self.__tree_height(self.root)

    def size(self):
        if self.root is None:
            return 0
        queue = my_queue()
        current = self.root
        queue.enqueue(current)
        count =0
        while not queue.is_empty():
            item = queue.dequeue()
            count += 1
            if item.left is not None:
                queue.enqueue(item.left)
            if item.right is not None:
                queue.enqueue(item.right)
        return count

    def get_min_node(self,node):
        assert node is not None
        prev = None
        while node.left is not None:
            prev = node
            node = node.left

        return node,prev

    def delete_node(self,val):
        if self.root is None:
            return
        curr = self.root
        prev = None
        while curr:
            if curr.data == val:
                if curr.left is None and curr.right is None: #no children
                    if curr == prev.left:
                        prev.left = None
                    elif curr == prev.right:
                        prev.right = None
                elif curr.left is not None and curr.right is not None: #two children
                    smallest,parent_Smallest_Node = self.get_min_node(curr)
                    curr.data = smallest.data
                    parent_Smallest_Node.left = None

                else: #one child
                    if curr == prev.right:
                        if curr.right:
                            prev.right = curr.right
                        else:
                            prev.right = curr.left
                    elif curr == prev.left:
                        if curr.left:
                            prev.left = curr.left
                        else:
                            prev.left = curr.right
                return
            elif val < curr.data:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

