def binary_search(L, s):
    '''(list of number, number) -> bool
    Return True iff s is an element of L
    REQ: L must be a sorted list
    '''
    pass
    # BASE CASE:

    # RECURSIVE DECOMP: Pick the middle element, if we found
    # what we're looking for, great. If not, then we've at
    # least cut the list in half


def binary_search2(L, s):
    '''(list of number, number) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be a sorted list
    '''
    # BASE CASE: If L is empty, return -1
    if (L == []):
        result = -1
    else:
        # GENERAL CASE
        # get the middle value of L, if it's larger than s, then s must be in
        # the first half of the list, so call binary_search on the first half,
        # otherwise, call it on the second half of L, if it's equal to s, then
        # we've found s and we can stop
        pass


def binary_search3(L, s):
    '''(list of number, number) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be a sorted list
    '''
    return binary_search3_helper(L, s, 0, len(L) - 1)


def binary_search3_helper(L, s, start, end):
    # base case: we're only looking at a single element of the list
    # if that element is the one we're looking for return its index
    # otherwise return -1
    if (-1):
        pass
    # recursive decomposition:
    else:
        pass
        # 3 cases
        # the middle element is greater than the value for which we're
        # searching, so look to the left

        # the middle element is smaller than the value for which were
        # searching, so look to the right

        # the element in the middle is the one we're looking for;


def binary_search4(L, item):
    '''(list of number, number) -> int
    Return the index of s in the list L, or -1 if s is not in L.
    This function uses loop only.
    REQ: L must be a sorted list
    '''
    pass


if (__name__ == "__main__"):
    L = [1, 2, 4, 6, 8, 10, 12, 13, 15, 17, 19, 20, 25]
    print(binary_search(L, 3))
    print(binary_search(L, 15))

    print(binary_search2(L, 3))
    print(binary_search2(L, 15))

    print(binary_search3(L, 3))
    print(binary_search3(L, 15))

    print(binary_search4(L, 3))
    print(binary_search4(L, 15))
