class EmptyQueueException(Exception):
    pass


class QueueA:
    '''A First-in, first-out (FIFO) queue of items'''

    def __init__(self):
        ''' (Queue) -> NoneType
        Create a new, empty queue.
        '''
        self._container = []

    def enqueue(self, new_obj):
        ''' (Queue, object) -> NoneType
        Place new_obj on top of this queue.
        '''
        self._container.append(new_obj)
        # self._container.insert(0, new_obj)

    def dequeue(self):
        ''' (Queue) -> object
        Remove and return the top item in this queue.
        '''
        if self._container != []:
            return self._container.pop(0)
            # return self._container.pop()
        else:
            raise EmptyQueueException

    def is_empty(self):
        ''' (Queue) -> bool
        Return True iff this queue is empty
        '''
        return self._container == []
        # return len(self._container) == 0


class QueueB:
    '''A First-in, first-out (FIFO) queue of items'''

    def __init__(self):
        '''(Queue) -> NoneType
        Create a new, empty queue.
        '''
        # we're going to store the queue as a dictionary {k:v}
        # where k = height on Queue, v = value
        self._container = {}
        self._height = 0

    def enqueue(self, new_obj):
        ''' (Queue, object) -> NoneType
        Place new_obj on top of this Queue.
        '''
        self._container[self._height] = new_obj
        self._height += 1

    def dequeue(self):
        ''' (Queue) -> object
        Remove and return the top item in this Queue.
        '''
        # to pop, we don't actually need to remove the items from
        # the dictionary, as any further push will simply over-write
        # the next key, and we're using height to check for emptiness
        if self._height == 0:
            raise EmptyQueueException
        else:
            self._height -= 1
            return self._container[self._height]

    def is_empty(self):
        '''(Queue) -> bool
        Return True iff this Queue is empty
        '''
        # if we used return self.contents == {} it would fail,
        # because of the way we implemented pop
        return self._height == 0


if __name__ == "__main__":
    q = QueueA()
    q.dequeue()
