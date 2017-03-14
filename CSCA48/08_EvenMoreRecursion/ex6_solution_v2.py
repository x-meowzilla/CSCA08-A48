def rsum(L):
    # base case: empty list
    if L == []:
        result = 0
    # recursive case: if the first element is a list
    elif isinstance(L[0], list):
        result = rsum(L[0]) + rsum(L[1:])
    # recursive case: if the first element is a number
    else:
        result = L[0] + rsum(L[1:])
    return result


def rmax(L):
    # base case
    if (L == []):
        result = float("-inf")
    else:
        # deal with the first element
        if (isinstance(L[0], list)):
            first_max = rmax(L[0])
        else:
            first_max = L[0]

        # now deal with the rest of the list
        rest_max = rmax(L[1:])

        if (first_max > rest_max):
            result = first_max
        else:
            result = rest_max
    return result


def second_smallest(L):
    # use a helper function
    (s1, s2) = _get_two_smallest(L)
    return s2


def _get_two_smallest(L):
    # base case
    if (L == []):
        MIN, SMIN = (float("inf"), float("inf"))
    else:
        # deal with the first element first
        if (isinstance(L[0], list)):
            first_min_pair = _get_two_smallest(L[0])
        else:
            first_min_pair = (L[0], float("inf"))

        # now deal with the rest
        rest_min_pair = _get_two_smallest(L[1:])

        # get the two smallest values out of the 4 possible values
        # get the smallest (must be one of the first two elements
        if (first_min_pair[0] < rest_min_pair[0]):
            MIN = first_min_pair[0]
            odd = first_min_pair[1]
            even = rest_min_pair
        else:
            MIN = rest_min_pair[0]
            odd = rest_min_pair[1]
            even = first_min_pair

        # no we've got 3 elements left
        if (odd < even[0]):
            SMIN = odd
        else:
            SMIN = even[0]

    return (MIN, SMIN)


def sum_max_min(L):
    # use a helper function
    (max_val, min_val) = _get_max_and_min(L)
    return max_val + min_val


def _get_max_and_min(L):
    # base case
    if (L == []):
        MAX, MIN = (float("-inf"), float("inf"))
    else:
        # deal with the first element first
        if (isinstance(L[0], int)):
            first_max = first_min = L[0]
        else:
            (first_max, first_min) = _get_max_and_min(L[0])

        # deal with the rest of the list
        (rest_max, rest_min) = _get_max_and_min(L[1:])

        # now we just need to pick the actual max and min
        if (first_max > rest_max):
            MAX = first_max
        else:
            MAX = rest_max

        if (first_min < rest_min):
            MIN = first_min
        else:
            MIN = rest_min

    return (MAX, MIN)


if __name__ == "__main__":
    L = [5, 2, [1, 4, [3], 7], 9, [11, 0]]
    print(second_smallest(L))
    print(sum_max_min(L))
