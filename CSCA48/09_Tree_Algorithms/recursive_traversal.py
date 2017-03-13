class BTNode:
    """ A node in a binary tree. """

    def __init__(self, data, left=None, right=None):
        """ (BTNode, str or int, BTNode, BTNode) -> NoneType

        Initialize a new BTNode with data, left and right children.
        """
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BTNode) -> str

        Return a string representing self.
        """
        return ("BinTreeNode(" + repr(self.data) + ", " +
                repr(self.left) + ", " + repr(self.right) + ")")

    def visit(self):
        """ (BTNode) -> NoneType

        Visit the node self.  In this case we print its data.
        """
        print(str(self.data) + ' ', end='')


def preorder(root):
    """ (BTNode) -> NoneType

    Visit the nodes of the tree rooted at root using pre-order traversal.
    """
    if root:
        root.visit()
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """ (BTNode) -> NoneType

    Visit the nodes of the tree rooted at root using post-order traversal.
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        root.visit()


def inorder(root):
    """ (BTNode) -> NoneType

    Visit the nodes of the tree rooted at root using in-order traversal.
    """
    if root:
        inorder(root.left)
        root.visit()
        inorder(root.right)


if __name__ == "__main__":
    tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                  BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))

    preorder(tree)
    print()
    inorder(tree)
    print()
    postorder(tree)
