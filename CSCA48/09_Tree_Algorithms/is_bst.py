class BSTNode:
    """ A node in a binary tree. """

    def __init__(self, data, left=None, right=None):
        """ (BSTNode, str, BSTNode, BSTNode) -> NoneType

        Initialize a new BSTNode with data, left and right children.
        """
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BSTNode) -> str

        Return a string representing self.
        """
        return ("BinTreeNode(" + repr(self.data) + ", " +
                repr(self.left) + ", " + repr(self.right) + ")")


def is_BST(root):
    '''(BSTNode) -> bool

    Return True iff the tree is a BST.
    '''
    # base case 0: the root is a leaf
    if not root.left and not root.right:
        is_bst = True
    else:
        # recursive case: right root is None, check left root
        if not root.right:
            left_tree = is_BST(root.left)
            right_tree = True
        # recursive case: left root is None, check right root
        elif not root.left:
            left_tree = True
            right_tree = is_BST(root.right)
        # recursive case: both left and right trees have leaves, check both
        else:
            # check binary search tree property
            if (root.left.data < root.data and root.right.data > root.data):
                left_tree = is_BST(root.left)
                right_tree = is_BST(root.right)
            else:
                left_tree = right_tree = False
        is_bst = left_tree and right_tree

    return is_bst


if __name__ == "__main__":
    root = BSTNode(7,
                   BSTNode(4,
                           BSTNode(1,
                                   BSTNode(0, None, None),
                                   None),
                           BSTNode(5, None, None)),
                   BSTNode(9,
                           BSTNode(8, None, None),
                           BSTNode(10, None,
                                   BSTNode(12, None, None))))
    print(is_BST(root))
