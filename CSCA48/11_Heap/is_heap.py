def is_heap(L, size):
    ''' (list, int) -> bool

    Return True if the list satisfies heap property

    '''
    if (len(L) != size):
        return False

    i_last = len(L)-1
    i_last_parent = (i_last-1)//2

    #min heap
    if L[i_last] > L[i_last_parent]:
        print("Is min heap: ")
        return min_heap(L)
    #max heap
    elif L[i_last] < L[i_last_parent]:
        print("Is max heap: ")
        return max_heap(L)
    #neither
    else:
        return False


def min_heap(L):
    '''(list) -> bool

    Return True if the list satisfies min heap property

    '''
    if (len(L) <= 1):
        return True
    else:
        i_last = len(L)-1
        i_last_parent = (i_last-1)//2
        #children are always greater than parents
        if L[i_last] > L[i_last_parent]:
            return min_heap(L[:i_last])
    return False


def max_heap(L):
    '''(list) -> bool

    Return True if the list satisfies max heap property

    '''
    if (len(L) <= 1):
        return True
    else:
        i_last = len(L)-1
        i_last_parent = (i_last-1)//2
        #children are always less than parents
        if L[i_last] < L[i_last_parent]:
            return max_heap(L[:i_last])
    return False

#L = [6, 5, 4, 3, 2, 1, 0]
#L = [0, 1, 2, 3, 4, 5, 6]
L = [2, 5, 8, 3, 4, 9]
print(is_heap(L, len(L)))
