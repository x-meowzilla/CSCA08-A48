def rsum(L):
    '''(list of int) -> int
    Return the sum of all the element in L.
    >>> rsum([1])
    1
    >>> rsum([1, 2, [4]])
    7
    >>> rsum([1, 2, [4, [5, []]]])
    12
    '''
    # base case
    if L == []:
        result = 0
    # if the first element is a list
    elif isinstance(L[0], list):
        result = rsum(L[0]) + rsum(L[1:])
    else:
        result = L[0] + rsum(L[1:])
    return result


def rmax(L):
    '''(list of int) -> int
    Return the max value in L.
    >>> rmax([1])
    1
    >>> rmax([1, [2], -1, []])
    2
    >>> rmax([1, [1, []]])
    1
    '''
    # base case
    if(L == []):
        result = float("-inf")
    else:
        #deal with the first element
        if(isinstance(L[0], list)):
            first_max = rmax(L[0])
        else:
            first_max = L[0]
        
        #now deal with the rest of the list
        rest_max = rmax(L[1:])
        
        if(first_max > rest_max):
            result = first_max
        else:
            result = rest_max
    return result


def second_smallest(L):
    '''(list of int) -> int
    Return the second smallest value in L. Return the smallest if L has more
    than one smallest element.
    >>> second_smallest([1, 2, 5])
    2
    >>> second_smallest([1, 2, -1])
    1
    >>> second_smallest([1, 1])
    1
    '''
    return _second_smallest_helper(L)[1]


def _second_smallest_helper(L, MIN=float('inf'), SMIN=float('inf'), MAX=float('-inf')):
    '''(list, int, int, int) -> tuple
    Return the tuple including the min, second min and max element in L.
    '''
    # if we come to empty list, we keep what it is
    if L == []:
        result = (MIN, SMIN, MAX)
    else:
        # if we get a list inside, we recurse
        if isinstance(L[0], list):
            # record the recursive result of the first element and compare
            # it with the rest
            MIN, SMIN, MAX = _second_smallest_helper(L[0], MIN, SMIN, MAX)
            # compare
            result = _second_smallest_helper(L[1:], MIN, SMIN, MAX)
        elif isinstance(L[0], int):
            # compare the number
            if L[0] < MIN:
                SMIN = MIN
                MIN = L[0]
            elif L[0] < SMIN:
                SMIN = L[0]
            # check whether it is the max as well
            if L[0] > MAX:
                MAX = L[0]
            # do the recursion
            result = _second_smallest_helper(L[1:], MIN, SMIN, MAX)
    return result


def sum_max_min(L):
    '''(list of int) -> int
    Return the sum of the max and min element in L.
    >>> sum_max_min([1, 2, 5])
    6
    >>> sum_max_min([1, 2, -1])
    1
    >>> sum_max_min([1, 1])
    2
    '''
    result = _second_smallest_helper(L)
    return (result[0] + result[2])
