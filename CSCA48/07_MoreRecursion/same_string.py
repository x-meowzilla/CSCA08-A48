def same_string(s1, s2):
    '''(str, str) -> bool
    Return True iff s1 == s2
    REQ: len(s1) == len(s2)
    '''
    # base case: empty strings are equal
    if (s1 == "" and s2 == ""):
        result = True
    # if we found a place where they're different, return False
    elif (s1[0] != s2[0]):
        result = False
    # if the first two letters are the same, look at the rest of the string
    else:
        result = same_string(s1[1:], s2[1:])
    return result


def almost_same_string(s1, s2):
    '''(str, str) -> bool
    Return True iff differ in at most one place
    REQ: len(s1) == len(s2)
    '''
    # base case: empty strings are equal
    if (s1 == "" and s2 == ""):
        result = True
    # if we found a place where they're different, the only way
    # we can return True is if the rest of the string is exactly equal
    elif (s1[0] != s2[0]):
        result = same_string(s1[1:], s2[1:])
    # if the first two letters are the same, then we need to check
    # if the rest of the strings are almost the same
    else:
        result = almost_same_string(s1[1:], s2[1:])
    return result


# ===================================================
# ===================================================


def almost_same_string2(s1, s2):
    '''(str, str) -> bool
    Return True iff differ in at most one place
    REQ: len(s1) == len(s2)
    '''
    return _almost_same_string_helper(s1, s2) <= 1


## solution using a helper function
def _almost_same_string_helper(s1, s2):
    '''(str, str) -> bool
    Return the number of places where s1 and s2 differ
    REQ: len(s1) == len(s2)
    '''
    # base case: empty strings differ in zero places
    if (s1 == "" and s2 == ""):
        result = 0
    # we have at least 1 character
    else:
        # count the number of differences in the first character
        if (s1[0] == s2[0]):
            differences = 0
        else:
            differences = 1
        # add the number of differences in the rest of the string
        differences += _almost_same_string_helper(s1[1:], s2[1:])
        result = differences
    return result


if (__name__ == "__main__"):
    print(same_string("ABCD", "ABCD"))
    print(same_string("ABXD", "ABCD"))
    print(same_string("ABCD", "WXYZ"))
    print(almost_same_string("ABCD", "ABCD"))
    print(almost_same_string("ABXD", "ABCD"))
    print(almost_same_string("ABCD", "WXYZ"))
    print(almost_same_string2("ABCD", "ABCD"))
    print(almost_same_string2("ABXD", "ABCD"))
    print(almost_same_string2("ABCD", "WXYZ"))
