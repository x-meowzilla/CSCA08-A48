# function to determine whether
# a given string is a palindrome.
def is_palindrome(s):
    ''' (str) -> bool
    Return True iff s is a palindrome.

    >>> is_palindrome("")
    True
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("nick")
    False
    '''
    if len(s) == 0 or len(s) == 1:
        result = True
    elif s[0] == s[-1]:
        result = is_palindrome(s[1:-1])
    else:
        result = False
    return result


# function to determine whether
# a given string is a near palindrome.
# Uses is_palindrome.
def is_near_palindrome1(s):
    ''' (str) -> bool
    Return True iff s is a near palindrome.

    >>> is_near_palindrome1("radar")
    True
    >>> is_near_palindrome1("naval")
    True
    >>> is_near_palindrome1("nick")
    False
    '''
    # if s is empty
    if s == "":
        result = True
    elif s[0] == s[-1]:
        result = is_near_palindrome1(s[1:-1])
    else:
        result = is_palindrome(s[1:-1])
    return result


# ===================================================
# ===================================================


def is_near_palindrome2(s):
    ''' (str) -> bool
    Return True iff s is a near palindrome.

    >>> is_near_palindrome2("radar")
    True
    >>> is_near_palindrome2("naval")
    True
    >>> is_near_palindrome2("nick")
    False
    '''
    return is_palindrome_helper(s, 1)


# Solution using a helper function.
def is_palindrome_helper(s, d):
    ''' (str, int) -> bool
    Return True iff s is within d changes of being a palindrome.
    REQ: d >= 0.

    >>> is_palindrome_helper("radar", 0)
    True
    >>> is_palindrome_helper("naval", 1)
    True
    >>> is_palindrome_helper("palindrome", 4)
    False
    >>> is_palindrome_helper("palindrome", 5)
    True
    '''
    # if s is empty
    if not s:
        result = True
    elif s[0] == s[-1]:
        result = is_palindrome_helper(s[1:-1], d)
    elif d > 0:
        result = is_palindrome_helper(s[1:-1], d - 1)
    else:
        result = False
    return result


# ===================================================
# ===================================================


# Uses python's default argument values to
# add helper without separate function.
def is_near_palindrome3(s, d=1):
    ''' (str, int) -> bool
    Return True iff s is within d changes of being a palindrome.
    REQ: d >= 0.

    >>> is_near_palindrome3("naval", 1)
    True
    >>> is_near_palindrome3("naval")
    True
    >>> is_near_palindrome3("palindrome", 4)
    False
    >>> is_near_palindrome3("palindrome", 5)
    True
    '''
    # if s is empty
    if not s:
        result = True
    elif s[0] == s[-1]:
        result = is_near_palindrome3(s[1:-1], d)
    elif d > 0:
        result = is_near_palindrome3(s[1:-1], d - 1)
    else:
        result = False
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
