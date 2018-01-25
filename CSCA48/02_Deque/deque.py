class EmptyQueueError(Exception):
    ''' An error to be raised when dequeued from an empty deque '''
    pass


class Deque():
    '''A double ended queue'''

    def __init__(self):
        ''' (Deque) -> NoneType

        Initialize a Dequeue.
        '''
        # Representation invariant:
        # _container is a list of object.
        # _container[:] are the objects in the deque.
        # len(_container) is the number of items in the deque
        # if _container is not empty, then
        #    - _left and _right are ints, where _left >= 0 and _right < len(_container)
        #    - _container[_left], ..., _container[_right] are the ordered objects in the deque
        # if i >= _left, j <= _right, and i < j, then
        #    _container[i] is to the left of _container[j] in the deque
        #    _container[j] is to the right of _container[i] in the deque
        self._container = []

    def enqueue_left(self, item):
        ''' (Deque, object) -> NoneType

        Add item onto the left side of the deque
        '''
        self._container = [item] + self._container

    def enqueue_right(self, item):
        ''' (Deque, object) -> NoneType

        Add item onto the right side of the deque
        '''
        self._container = self._container + [item]

    def dequeue_left(self):
        ''' (Deque) -> object

        Remove and return the leftmost item in the deque
        '''
        if (self.is_empty()):
            raise EmptyQueueError("Can't dequeue left from an empty queue")
        else:
            item = self._container[0]
            self._container = self._container[1:]
            return item

    def dequeue_right(self):
        ''' (Deque) -> object

        Remove and return the rightmost item in the deque
        '''
        if (self.is_empty()):
            raise EmptyQueueError("Can't dequeue right from an empty queue")
        else:
            item = self._container[-1]
            self._container = self._container[:-1]
            return item

    def is_empty(self):
        ''' (Deque) -> bool

        Return True iff this deque is empty
        '''
        return len(self._container) == 0


if (__name__ == "__main__"):
    dq = Deque()
    dq.enqueue_left('A')
    dq.enqueue_left('B')
    dq.enqueue_left('C')
    dq.enqueue_right('D')
    dq.enqueue_right('E')
    dq.enqueue_right('F')
    dq.enqueue_left('G')
    while (not dq.is_empty()):
        print(dq.dequeue_right())
        print(dq.dequeue_left())
