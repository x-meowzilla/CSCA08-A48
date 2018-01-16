class InvalidSizeError(Exception): pass


class InvalidOperationError(Exception): pass


class Vector():

    def __init__(self, size):
        ''' (Vector, obj) -> NoneType
        Creates a geometric vector of the given size,
        raise InvalidSizeError if the size is 0 or negative number
        '''
        if size <= 0:
            raise InvalidSizeError('Size cannot be zero or negative.')
        self._vector = [0] * size

    def __str__(self):
        ''' (Vector) -> str
        Returns a string representing the vector
        '''
        return str(tuple(self._vector))  # nothing fancy, just a tuple representation
        # res = ''
        # for coordinate in self._vector:
        #     res += str(coordinate) + ', '
        # return '{' + res.strip(', ') + '}'

    def get_size(self):
        ''' (Vector) -> int
        Returns the number of items in the vector (i.e. length)
        '''
        return len(self._vector)

    def get_element(self, i):
        ''' (Vector, int) -> obj
        Returns the object that is found at the given index
        '''
        if i >= len(self._vector):
            raise InvalidOperationError('Cannot get element from this index. Vector index out of range.')
        return self._vector[i]

    def set_element(self, i, value):
        ''' (Vector, int, obj) -> NoneType
        Set the given index to the given value
        '''
        if i >= len(self._vector):
            raise InvalidOperationError('Cannot set element to this index. Vector index out of range.')
        self._vector[i] = value

    def equals(self, vector):
        '''(Vector, Vector) -> bool
        Returns true if two vectors have the same coordinates
        '''
        return self._vector == vector._vector

    def add(self, other):
        ''' (Vector, Vector) -> Vector
        Returns the sum of two vectors
        '''
        if self.get_size() != other.get_size():
            raise InvalidOperationError('Cannot add two vectors with different sizes.')

        # create a result vector and sum up the element.
        result = Vector(self.get_size())
        for i in range(self.get_size()):
            # be extra careful here, since 2 different data types may resulting in crashes
            result.set_element(i, self.get_element(i) + other.get_element(i))

        return result


if __name__ == '__main__':
    v1 = Vector(5)
    v2 = Vector(5)

    print(v1)
    print(v2)

    v3 = v1.add(v2)
    print(v3)
