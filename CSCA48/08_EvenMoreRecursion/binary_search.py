def binary_search(L, s):
    '''(list) -> bool
    Return True iff s is an element of L
    REQ: L must be a sorted list
    '''
    # BASE CASE: If L is empty, it's not in the list
    if (len(L) == 0):
        result = False
    # RECURSIVE DECOMP: Pick the middle element, if we found
    # what we're looking for, great. If not, then we've at
    # least cut the list in half
    else:
        # get the middle element of the list
        mid_index = len(L) // 2
        mid_element = L[mid_index]

        # if we didn't find it, then see whether we need to continue searching
        # in the left side of the list, or the right
        if (mid_element < s):
            result = binary_search(L[mid_index + 1:], s)
        elif (mid_element > s):
            result = binary_search(L[: mid_index], s)
        else:
            result = True

    return result


def binary_search2(L, s):
    '''(list of float) -> int
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
        mid_index = len(L) // 2
        mid = L[mid_index]
        if (mid > s):
            # if s is in L, it must be in the first half of the list
            # so just perform a binary search on the first half of the list
            # and return that search's result
            result = binary_search2(L[:mid_index], s)
        elif (mid < s):
            # if s is in L, it must be in the latter half of the list
            # so perform a binary search on the latter half of the list,
            # however, this time, if we do get a result, we have to return
            # its offset from our current midpoint
            result = binary_search2(L[mid_index + 1:], s)
            # if we didn't find it, just pass on the -1, but if we did
            # we have to add the index in the right list to the index of
            # our middle element to get its index in our list
            if (result != -1):
                result = result + mid_index + 1
        else:
            result = mid_index

    return result


def binary_search3(L, s):
    '''(list of float) -> int
    Return the index of s in the list L, or -1 if s is not in L
    REQ: L must be a sorted list
    '''
    return binary_search3_helper(L, s, 0, len(L) - 1)


def binary_search3_helper(L, s, start, end):
    # base case: we're only looking at a single element of the list
    # if that element is the one we're looking for return its index
    # otherwise return -1
    if (start == end):
        if (s == L[start]):
            result = start
        else:
            result = -1
    # recursive decomposition:
    else:
        mid = start + (end - start) // 2
        mid_val = L[mid]
        # 3 cases
        # the middle element is greater than the value for which we're
        # searching, so look to the left
        if (mid_val > s):
            result = binary_search3_helper(L, s, start, mid)
        # the middle element is smaller than the value for which were
        # searching, so look to the right
        elif (mid_val < s):
            result = binary_search3_helper(L, s, mid + 1, end)
        # the element in the middle is the one we're looking for;
        else:
            result = mid

    return result


def binary_search4(L, item):
    '''(list of number, number) -> int
    Return the index of s in the list L, or -1 if s is not in L.
    This function uses loop only.
    REQ: L must be a sorted list
    '''
    first = 0
    last = len(L) - 1
    found = False
    found_index = -1

    while first <= last and not found:
        midpoint = (first + last) // 2
        if L[midpoint] < item:
            first = midpoint + 1
        elif L[midpoint] > item:
            last = midpoint - 1
        else:
            found = True
            found_index = midpoint

    return found_index


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
