class HeapEmptyError(Exception):
    '''To be thrown when attempting to extract from an empty heap'''


class Heap(object):
    '''A max-heap implementation'''

    def __init__(self, insert_list=[]):
        '''(Heap [,list]) -> NoneType
        Create a new Heap containing the elements in insert_list
        '''
        # REPRESENTATION INVARIANT
        # _heap is a list of all elements in this heap
        # if the heap is empty, _heap == []
        # otherwise
        # if i is an index in _heap
            # if j = (i * 2) + 1 is an index in _heap
                # _heap[j] <= heap[i]
            # if j = (i * 2) + 2 is an index in _heap
                # _heap[j] <= heap[i]
        self._heap = []
        for element in insert_list:
            self.insert(element)

    def is_empty(self):
        '''(Heap) -> bool
        Return True iff there are no nodes in this Heap
        '''
        return self._heap == []

    def insert(self, insert_value):
        '''(Heap, object) -> NoneType
        Insert insert_value into the heap
        '''
        self._heap.append(insert_value)
        self._bubble_up()

    def _bubble_up(self):
        '''(Heap) -> NoneType
        Re-arrange the values in the heap to maintain the heap property after
        a new element has been inserted into the heap
        '''
        # the index of the child node, initialized to the new node that was
        # added (the last node in the list)
        c_index = len(self._heap) - 1
        #  the parent index, will always be (child -1)/2 (rounded down)
        p_index = (c_index - 1) // 2

        # Keep looping as long as we're still violating the heap condition
        # i.e., the child is > the parent
        while(c_index > 0 and self._heap[c_index] > self._heap[p_index]):
            # swap the parent and child
            self._swap(c_index, p_index)
            # move up one level
            c_index = p_index
            p_index = (p_index - 1) // 2

    def _swap(self, i, j):
        '''(Heap, int, int) -> NoneType
        Swap the values at index i and j
        '''
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def __str__(self):
        '''(Heap) -> str
        Return a string representation of this Heap
        '''
        return str(self._heap) + "\n" + self._str_helper(0, "")

    def remove_max(self):
        '''(Heap) -> object
        Remove and return the largest element in the heap
        RAISES: HeapEmptyError if heap is empty
        '''
        if(len(self._heap) == 0):
            raise HeapEmptyError("Attempt to remove from empty heap")
        else:
            # save the top element
            ret = self._heap[0]
            # remove the last element from the heap, and
            # replace the head's value with it
            last = self._heap.pop()
            # as long as we've got at least 1 element left in the heap,
            # we need to re-establish the heap propery
            if(len(self._heap) > 0):
                self._heap[0] = last
                self._bubble_down()
            return ret

    def _bubble_down(self):
        '''(Heap) -> NoneType
        Re-arrange the values in the heap to maintain the heap property after
        the top element of the heap has been removed
        '''
        # parent index (starting with top node of heap = 0th item in list
        p_index = 0
        # get the index of the two children
        lt_index = (p_index * 2) + 1
        rt_index = (p_index * 2) + 2
        # keep looping while we violate the heap property
        while(self._violates(p_index)):
            # one of our children violates the heap property
            # if we only have a left child, it must be that one
            if(rt_index >= len(self._heap)):
                self._swap(p_index, lt_index)
                p_index = lt_index

            # if we have two children, we need to swap with the larger child
            elif(self._heap[lt_index] > self._heap[rt_index]):
                self._swap(p_index, lt_index)
                p_index = lt_index
            else:
                self._swap(p_index, rt_index)
                p_index = rt_index
            # find the new children for the next loop
            lt_index = (p_index * 2) + 1
            rt_index = (p_index * 2) + 2

    def _violates(self, index):
        '''(Heap, int) -> bool
        Return True iff the node at index and one of its children violate the
        heap property
        '''
        lt_index = (index * 2) + 1
        rt_index = (index * 2) + 2
        # if we have no children, we're fine
        if(lt_index >= len(self._heap)):
            result = False
        # if we have one child, return True iff it violates
        elif(rt_index >= len(self._heap)):
            result = self._heap[lt_index] > self._heap[index]
        # if we have two children, return True if either child violates
        else:
            result = (self._heap[lt_index] > self._heap[index] or
                    self._heap[rt_index] > self._heap[index])
        return result
