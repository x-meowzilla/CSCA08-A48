# Learning objective: understanding abstract class & method
# Created by Eric Wang (University of Toronto Scarborough)


from abc import ABC, abstractmethod


class InvalidSizeError(Exception): pass


class InvalidOperationError(Exception): pass


class Vector(ABC):

    def __init__(self, size, value):
        ''' (Vector, int, obj) -> NoneType
        The constructor/initializer of an abstract vector object.

        Note: abstract class cannot be initialized/created if any @abstractmethod is not implemented in the subclass.
        Raise: InvalidSizeError if the size is 0 or negative number
        '''
        if not isinstance(size, int) and size <= 0:
            raise InvalidSizeError('Size can only be non-negative numbers.')
        self._vector = [value] * size

    def __str__(self):
        ''' (Vector) -> str
        Returns a string representing the vector
        '''
        return str(tuple(self._vector))

    @abstractmethod
    def equals(self, other):
        pass

    @abstractmethod
    def add(self, other):
        pass

    def get_size(self):
        ''' (Vector) -> int
        Returns the number of items in the vector (i.e. length)
        '''
        return len(self._vector)

    def get_vector(self):
        ''' (Vector) -> Vector
        Return the content of this vector
        '''
        return self._vector

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


class IntVector(Vector):

    def __init__(self, size):
        ''' (IntVector, int) -> NoneType
        The constructor/initializer of an IntVector object.

        Note: @abstractmethod from parent class must be implemented before initialize IntVector.
        '''
        super().__init__(size, 0)

    def equals(self, other):
        '''(IntVector, IntVector) -> bool
        Returns true if two vectors have the same coordinates
        '''
        return self.get_vector() == other.get_vector()

    def add(self, other):
        ''' (IntVector, IntVector) -> Vector
        Returns the sum of two vectors
        '''
        # check conditions:
        # 1. must be IntVector
        if not isinstance(other, IntVector):
            raise InvalidOperationError('Cannot add two vectors with different types.')
        # 2. must be same size
        elif self.get_size() != other.get_size():
            raise InvalidOperationError('Cannot add two vectors with different sizes.')

        # create a result vector and sum up the element.
        result = IntVector(self.get_size())
        for i in range(self.get_size()):
            # be extra careful here, since 2 different data types may resulting in crashes
            result.set_element(i, self.get_element(i) + other.get_element(i))

        return result

    # override method
    def set_element(self, i, value):
        ''' (IntVector, int, obj) -> NoneType
        Override the existing method. Set the given index to the given value
        '''
        if not isinstance(value, int):
            raise InvalidOperationError('Cannot set to non-integer value.')
        super().set_element(i, value)


class StrVector(Vector):

    def __init__(self, size):
        ''' (StrVector, int) -> NoneType
        The constructor/initializer of an StrVector object.

        Note: @abstractmethod from parent class must be implemented before initialize StrVector.
        '''
        super().__init__(size, '')

    def equals(self, other):
        '''(StrVector, StrVector) -> bool
        Returns true if two vectors have the same coordinates
        '''
        return self._vector == other._vector

    def add(self, other):
        ''' (IntVector, IntVector) -> Vector
        Returns the sum of two vectors
        '''
        # check conditions:
        # 1. must be IntVector
        if not isinstance(other, StrVector):
            raise InvalidOperationError('Cannot add two vectors with different types.')
        # 2. must be same size
        elif self.get_size() != other.get_size():
            raise InvalidOperationError('Cannot add two vectors with different sizes.')

        # create a result vector and sum up the element.
        result = StrVector(self.get_size())
        for i in range(self.get_size()):
            # be extra careful here, since 2 different data types may resulting in crashes
            result.set_element(i, self.get_element(i) + other.get_element(i))

        return result

    # override method
    def set_element(self, i, value):
        ''' (IntVector, int, obj) -> NoneType
        Override the existing method. Set the given index to the given value
        '''
        if not isinstance(value, str):
            raise InvalidOperationError('Cannot set to non-str value.')
        super().set_element(i, value)


if __name__ == '__main__':
    int_v1 = IntVector(5)
    int_v2 = IntVector(5)
    int_v3 = IntVector(3)
    int_v1.set_element(1, 5)
    int_v2.set_element(2, 5)
    int_v3.set_element(0, 5)
    print(int_v1)
    print(int_v2)
    print(int_v3)
    int_res = int_v1.add(int_v2)
    print(int_res)
    print(int_v1.equals(int_v2))

    print('=============')

    str_v1 = StrVector(5)
    str_v2 = StrVector(5)
    str_v3 = StrVector(3)
    str_v1.set_element(1, 'Hello')
    str_v2.set_element(1, 'World')
    str_v3.set_element(0, 'Bye')
    print(str_v1)
    print(str_v2)
    print(str_v3)
    str_res = str_v1.add(str_v2)
    print(str_res)
    print(str_v1.equals(str_v2))

    print('=============')

    # # invalid operations
    # res1 = int_v1.add(int_v3)  # invalid operation due to different size
    # res2 = int_v1.add(str_v1)  # invalid operation due to different type
    # int_v3.set_element(1, 'Good') # invalid operation
    # str_v3.set_element(1, 999)  # invalid operation

    # int_v3.set_element(1, True)  # something looks interesting here!
    # print(int_v3)
