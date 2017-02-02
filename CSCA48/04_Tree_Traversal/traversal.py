from utility import BTNode, Stack, Queue


# Breadth-First Search (BFS)
#   - Level-order traversal
def level_order_traversal(root):
    q = Queue()
    output = []

    q.enqueue(root)
    while (not q.is_empty()):
        node = q.dequeue()
        output.append(node)
        if (node.left): q.enqueue(node.left)
        if (node.right): q.enqueue(node.right)

    return output


def level_order_traversal_stack(root):
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
    print("Use Queue as container:", level_order_traversal(root))
    print("Use Stack as container:", level_order_traversal_stack(root))
