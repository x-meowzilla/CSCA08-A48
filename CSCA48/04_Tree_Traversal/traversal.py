from utility import BTNode, Stack, Queue


# Breadth-First Search (BFS)
#   - Level-order traversal
def level_order_traversal(root):
    """ (BTNode) -> list of BTNode

    This is the level-order traversal algorithm. The function returns a list of BTNode.
    For level-order traversal, it is commonly used a Queue to keep track of the level.
    """
    q = Queue()
    output = []

    q.enqueue(root)
    while (not q.is_empty()):
        node = q.dequeue()
        output.append(node)
        if (node.left): q.enqueue(node.left)
        if (node.right): q.enqueue(node.right)

    return output


def mysterious_traversal(root):
    """ (BTNode) -> list of BTNode

    This traversal uses the same algorithm but with a Stack instead of Queue.
    Play with it, find the pattern.
    """
    q = Stack()
    output = []

    q.push(root)
    while (not q.is_empty()):
        node = q.pop()
        output.append(node)
        if (node.left): q.push(node.left)
        if (node.right): q.push(node.right)

    return output


# Depth-First Search (DFS)
#   - Pre-order traversal
#   - In-order traversal
#   - Post-order traversal
# Note: For DFS algorithms, it will be implemented once recursion is taught.
#       Using loops to implement DFS is way too complicated to understand.


if __name__ == "__main__":
    # what does the following tree look like?
    root = BTNode("A",
                  BTNode("B",
                         BTNode("C", None, None),
                         BTNode("D", None, None)),
                  BTNode("E",
                         BTNode("F", None, None),
                         BTNode("G", None, None)))
    print(root)
    print("Level-order Traversal output:", level_order_traversal(root))
    print("Mysterious Traversal output:", mysterious_traversal(root))
