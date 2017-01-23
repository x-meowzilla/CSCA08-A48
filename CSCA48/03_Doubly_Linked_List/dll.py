class DLLNode():
    """ A Node in a doubly-linked list """

    def __init__(self, data, prev_link=None, next_link=None):
        ''' (DLLNode, object, DLLNode, DLLNode) -> NoneType
        Create a new DLLNode containing object, with previous node
        prev_link, and next node next_link.
        '''
        # Representation invariant:
        # data is an object
        # prev_link is a DLLNode
        # next_link is a DLLNode
        # data is the item held in this node
        # prev_link is the node immediately before (closer
        # to the head of the list than) this node
        # next_link is the node immediately after (closer
        # to the tail of the list than) this node
        self._data = data
        self._prev_link = prev_link
        self._next_link = next_link

    def __str__(self):
        ''' (DLLNode) -> str
        Return a str representation of this DLLNode.
        '''
        return str(self._data)

    def get_data(self):
        ''' (DLLNode) -> object
        Return the data of this DLL node
        '''
        return self._data

    def get_next(self):
        ''' (DLLNode) -> DLLNode
        Return the next node.
        '''
        return self._next_link

    def get_previous(self):
        ''' (DLLNode) -> DLLNode
        Return the previous node.
        '''
        return self._prev_link

    def set_next(self, node):
        ''' (DLLNode) -> NoneType
        Connect the node node to next link
        '''
        self._next_link = node

    def set_previous(self, node):
        ''' (DLLNode) -> NoneType
        Connect the node node to previous link
        '''
        self._prev_link = node


class DoublyLinkedList():
    """ A doubly linked list """

    def __init__(self):
        '''(DoublyLinkedList) -> NoneType
        Create a new empty DoublyLinkedList
        '''
        # Representation invariant:
        # _head is a DLLNode
        # _tail is a DLLNode
        # if the list is empty:
        #     _head = _tail = None
        # if the list is non-empty:
        #     _head is the first node in the list
        #     _tail is the last node in the list
        #     if nodeA and nodeB are both nodes in this list and nodeA is
        #     before (closer to the head than) nodeB:
        #         nodeA.next_link[.next_link]* = nodeB
        #             ([.next_link]* = 0 or more repetitions of .next_link)
        #         nodeB.prev_link[.prev_link]* = nodeA
        self._head = None
        self._tail = self._head
        self._size = 0

    def __str__(self):
        '''(DoublyLinkedList) -> str
        Return a str representation of the contents of this
        DoublyLinkedList.
        '''
        # store all DLL data
        dll_list = []
        curr_node = self._head
        # append data into the dll list
        while (curr_node):
            dll_list.append(curr_node.get_data())
            curr_node = curr_node.get_next()
        return "Doubly Linked List: " + str(dll_list)

    def get_size(self):
        ''' (DoublyLinkedList) -> int
        Return the size of the doubly linked list
        '''
        return self._size

    def add_head(self, data):
        '''(DoublyLinkedList, object) -> NoneType
        Add data to the head of this DoublyLinkedList.
        '''
        node = DLLNode(data)
        # if empty node list
        if (self._head is None):
            self._head = node
            self._tail = self._head
        # if not empty
        else:
            self._head.set_previous(node)
            node.set_next(self._head)
            self._head = node
        # increase the size by 1
        self._size += 1

    def add_tail(self, data):
        '''(DoublyLinkedList, object) -> NoneType
        Add data to the tail of this DoublyLinkedList.
        '''
        node = DLLNode(data)
        # if empty node list
        if (self._head is None):
            self._head = node
            self._tail = self._head
        # if not empty
        else:
            self._tail.set_next(node)
            node.set_previous(self._tail)
            self._tail = node
        # increase the size by 1
        self._size += 1

    def add_index(self, data, idx):
        '''(DoublyLinkedList, object, int) -> NoneType
        Add data to this DoublyLinkedList at index idx.
        '''
        # if the index is 0, add the node to the head
        if (idx == 0):
            self.add_head(data)
        elif (idx >= self.get_size()):
            self.add_tail(data)
        else:
            node = DLLNode(data)
            curr_node = self._head
            prev_node = curr_node.get_previous()
            # loop thu the nodes to index, after looping thu nodes, prev is the
            # index node, curr is the index+1 node
            for i in range(idx):
                prev_node = curr_node
                curr_node = curr_node.get_next()

            # prev link node
            prev_node.set_next(node)
            node.set_previous(prev_node)

            # node link curr
            node.set_next(curr_node)
            curr_node.set_previous(node)
            self._size += 1

    def remove_head(self):
        '''(DoublyLinkedList) -> object
        Remove and return the first item in this DoublyLinkedList.
        '''
        # mark the head node
        removed_node = self._head
        # check if head node is not None
        if (removed_node):
            # move the head marker to the next node
            self._head = self._head.get_next()
            # double check if current head node is not None,
            # if not None, then break the previous link
            if (self._head):
                self._head.set_previous(None)
            # if None, means this is the last node, also set tail to None
            else:
                self._tail = self._head
            # decrease the DLL size by 1
            self._size -= 1

        return removed_node

    def remove_tail(self):
        '''(DoublyLinkedList) -> object
        Remove and return the last item in this DoublyLinkedList.
        '''
        # mark the tail node
        removed_node = self._tail
        # check if tail node is not None
        if (removed_node):
            # move the tail marker to the previous node
            self._tail = self._tail.get_previous()
            # double check if current tail node is not None
            # if not None, then break the next link
            if (self._tail):
                self._tail.set_next(None)
            # if None, means this is the last node, also set head to None
            else:
                self._head = self._tail
            # decrease the DLL size by 1
            self._size -= 1

        return removed_node

    def remove_index(self, idx):
        '''(DoublyLinkedList, int) -> object
        Remove and return the item at index remove_index in this
        DoublyLinkedList.
        '''
        # if remove index 0, then remove head node
        if (idx == 0):
            removed_node = self.remove_head()
        # if remove index greater than the size of the linked list
        # then raise IndexError
        elif (idx >= self.get_size()):
            raise IndexError("Doubly linked list index out of range.")
        # if remove somewhere else, then
        else:
            curr_node = self._head
            prev_node = curr_node.get_previous()
            removed_node = None
            # loop thu the nodes to the index
            for i in range(idx):
                prev_node = curr_node
                curr_node = curr_node.get_next()

            if (curr_node.get_next() is None):
                self.remove_tail()
            else:
                # mark the node to be removed
                removed_node = curr_node
                curr_node = curr_node.get_next()

                # break the link for prev and curr nodes
                prev_node.set_next(curr_node)
                curr_node.set_previous(prev_node)

                # break the link for removed node
                removed_node.set_next(None)
                removed_node.set_previous(None)

                # decrease the size by 1
                self._size -= 1

        return removed_node


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.add_head(1)
    print("Add head:", dll)
    print("DLL size:", dll.get_size())
    dll.add_head(2)
    print("Add head:", dll)
    print("DLL size:", dll.get_size())
    dll.remove_head()
    print("Remove head:", dll)
    print("DLL size:", dll.get_size())
    dll.remove_head()
    print("Remove head:", dll)
    print("DLL size:", dll.get_size())

    print("====================")

    dll.add_tail(2)
    print("Add tail:", dll)
    print("DLL size:", dll.get_size())
    dll.add_tail(3)
    print("Add tail:", dll)
    print("DLL size:", dll.get_size())
    dll.remove_tail()
    print("Remove tail:", dll)
    print("DLL size:", dll.get_size())
    dll.remove_tail()
    print("Remove tail:", dll)
    print("DLL size:", dll.get_size())

    print("====================")

    dll.add_tail('B')
    dll.add_tail('C')
    dll.add_tail('E')
    dll.add_index('A', 0)
    print("Add index at 0:", dll)
    print("DLL size:", dll.get_size())
    dll.add_index('D', 3)
    print("Add index at 3:", dll)
    print("DLL size:", dll.get_size())
    dll.add_index('F', 5)
    print("Add index at 5:", dll)
    print("DLL size:", dll.get_size())
    dll.add_index('Z', 25)
    print("Add index at 25", dll)
    print("DLL size:", dll.get_size())

    print("====================")

    dll.remove_index(3)  # remove from body
    print("Remove index at 3", dll)
    print("DLL size:", dll.get_size())
    dll.remove_index(0)  # remove head
    print("Remove index at 0", dll)
    print("DLL size:", dll.get_size())
    dll.remove_index(4)  # remove tail
    print("Remove index at 3", dll)
    print("DLL size:", dll.get_size())
    dll.remove_index(25)  # error
    print("Remove index at 25", dll)
    print("DLL size:", dll.get_size())
