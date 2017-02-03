class BTNode():
    """ A class represent tree node """

    def __init__(self, data, left=None, right=None):
        """ (BTNode, object, Node, Node) -> NoneType

        Initialize a tree node.
        """
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BTNode) -> str

        Return a string representation of this node.
        """
        return self.data

    def __str__(self):
        """ (BTNode) -> str

        Return a string representation of this tree. (Used recursion to print the tree structure)
        """
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        tree_rep = ""

        if (self.right):
            tree_rep += self.right._str_helper(indentation + "\t") + "\n"
        tree_rep += indentation + str(self.data) + "\n"
        if (self.left):
            tree_rep += self.left._str_helper(indentation + "\t") + "\n"
        return tree_rep


class Stack:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        self._container = []

    def push(self, new_obj):
        self._container.append(new_obj)

    def pop(self):
        return self._container.pop()

    def is_empty(self):
        return self._container == []


class Queue:
    '''A First-in, first-out (FIFO) queue of items'''

    def __init__(self):
        self._container = []

    def enqueue(self, new_obj):
        self._container.append(new_obj)

    def dequeue(self):
        return self._container.pop(0)

    def is_empty(self):
        return self._container == []
