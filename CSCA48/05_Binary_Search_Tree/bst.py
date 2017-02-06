class BSTNode():
    """ A class represent tree node """

    def __init__(self, data, left=None, right=None):
        """ (BSTNode, object, Node, Node) -> NoneType

        Initialize a tree node.
        """
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BSTNode) -> str

        Return a string representation of this node.
        """
        return self.data

    def __str__(self):
        """ (BSTNode) -> str

        Return a string representation of this tree. (Used recursion to print the tree structure)
        """
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BSTNode, str) -> str
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


def bst_search(root, value):
    """ (BSTNode, str) -> bool

    Return True iff the BST rooted at root
    contains a node whose data is value.
    """
    curr = root
    while curr and curr.data != value:
        if value < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    return (curr != None)


def bst_insert(root, value):
    """ (BSTNode, str) -> BSTNode

    Insert a node whose data is value into the BST rooted at root.
    Return the root of the updated BST.
    """
    if (not root):
        root = BSTNode(value)
    else:
        # search for the parent of this new node.
        curr = root
        parent = None
        while (curr and curr.data != value):
            parent = curr
            curr = curr.left if curr.data > value else curr.right

        if (not curr):  # curr is None, meaning no nodes contains same data
            node = BSTNode(value)
            if (parent.data > value):
                parent.left = node
            else:
                parent.right = node

    return root


if __name__ == "__main__":
    bst_root = BSTNode(11,
                       BSTNode(5, None, BSTNode(7, None, None)),
                       BSTNode(16, None, None))
    print(bst_root)
    print(bst_search(bst_root, 7))
    print(bst_search(bst_root, 17))
