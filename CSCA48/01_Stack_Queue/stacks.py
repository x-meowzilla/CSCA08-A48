class EmptyStackException(Exception):
    pass


class StackA:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        ''' (Stack) -> NoneType
        Create a new, empty stack.
        '''
        self._container = []

    def push(self, new_obj):
        ''' (Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._container.append(new_obj)

    def pop(self):
        ''' (Stack) -> object
        Remove and return the top item in this stack.
        '''
        if self._container != []:
            return self._container.pop()
        else:
            raise EmptyStackException

    def is_empty(self):
        ''' (Stack) -> bool
        Return True iff this stack is empty
        '''
        return self._container == []
        # return len(self._container) == 0


class StackB:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        ''' (Stack) -> NoneType
        Create a new, empty Stack.
        '''
        self._container = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        # Store the item to the beginning of the list
        # *****(this is a bad idea, but we're doing it anyway)*****
        self._container.insert(0, new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        if self._container != []:
            return self._container.pop(0)
        else:
            raise EmptyStackException

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty.'''
        return self._container == []


class StackC:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # we're going to store the stack as a dictionary {k:v}
        # where k = height on stack, v = value
        self._container = {}
        self._height = 0

    def push(self, new_obj):
        ''' (Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._container[self._height] = new_obj
        self._height += 1

    def pop(self):
        ''' (Stack) -> object
        Remove and return the top item in this stack.
        '''
        # to pop, we don't actually need to remove the items from
        # the dictionary, as any further push will simply over-write
        # the next key, and we're using height to check for emptiness
        if self._height == 0:
            raise EmptyStackException
        else:
            self._height -= 1
            return self._container[self._height]

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        # if we used return self.contents == {} it would fail,
        # because of the way we implemented pop
        return self._height == 0


if __name__ == "__main__":
    stkA = StackA()
    stkA.pop()
