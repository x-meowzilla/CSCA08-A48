# Document me if you like.

# vowel list
VOWEL = list('AEIOUaeiou')


def vowel_count_v1(s):
    ''' (str) -> int
    Count number of vowel in the string s.
    O(n) time, exponential space.
    '''
    if len(s) == 0:
        res = 0
    elif len(s) == 1:
        res = int(s in VOWEL)
    else:
        res = int(s[0] in VOWEL) + vowel_count_v1(s[1:])
    return res


def vowel_count_v2(s):
    ''' (str) -> int
    Count number of vowel in the string s.
    O(n) time, constant space (better space efficiency).
    '''

    def _helper(s, idx):
        if idx >= len(s):
            res = 0
        else:
            res = int(s[idx] in VOWEL) + _helper(s, idx + 1)
        return res

    return _helper(s, 0)


def has_more_vowel_v1(s):
    ''' (str) -> bool
    Return True if input string has more vowel than consonants.
    O(n) time, exponential space.
    '''

    def _helper(s, v_count, c_count):
        if s == '':
            res = v_count > c_count
        else:
            if s[0] in VOWEL:
                v_count += 1
            else:
                c_count += 1
            res = _helper(s[1:], v_count, c_count)
        return res

    return _helper(s, 0, 0)


def has_more_vowel_v2(s):
    ''' (str) -> bool
    Return True if input string has more vowel than consonants.
    O(n) time, constant space (better space efficiency)
    '''

    def _helper(s, idx, v_count, c_count):
        if idx >= len(s):
            res = v_count > c_count
        else:
            if s[idx] in VOWEL:
                v_count += 1
            else:
                c_count += 1
            res = _helper(s, idx + 1, v_count, c_count)
        return res

    return _helper(s, 0, 0, 0)


if __name__ == '__main__':
    s1 = 'Apple'
    s2 = 'Orange'
    print(vowel_count_v1(s1))
    print(vowel_count_v2(s2))

    print(has_more_vowel_v1(s1))
    print(has_more_vowel_v2(s2))
