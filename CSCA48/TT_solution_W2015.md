Term Test Solution - Winter 2015
---------------

#### Question 1
```python
def edit_distance(s1, s2):
    ''' (str, str) -> int
    Returns the number of single character changes
    necessary to turn s1 into s2.
    '''
    if len(s1) == 0:
        result = 0
    else:
        cost = 0 
        if s1[0] != s2[0]:
            cost = 1
        result = cost + edit_distance(s1[1:], s2[1:])
    return result
```

```python
def edit_distance_hard(s1, s2):
    ''' (str, str) -> int
    Returns the minimum number of single character
    edits required to turn s1 into s2. Allowable edits
    are insertions, deletions, and substitutions.
    See: Levenshtein distance
    '''
    if len(s1) == 0:
        result = len(s2)
    elif len(s2) == 0:
        result = len(s1)
    else:
        cost = (s1[-1] != s2[-1])
        result = min(edit_distance_hard(s1[:-1], s2) + cost,
                     edit_distance_hard(s1, s2[:-1]) + cost,
                     edit_distance_hard(s1[:-1], s2[:-1]) + cost)
    return result
```

#### Question 2
```python
def all_perms(s):
    ''' (str) -> list of str
    Returns all permutations of the given string
    using two loops.
    '''
    if (len(s) < 2):
        result = [s]
    elif (len(s) == 2):
        result = [s[0] + s[1], s[1] + s[0]]
    else:
        L = []
        for i in range(len(s)):
            for perm in perms(s[:i] + s[i + 1:]):
                L.append(s[i] + perm)
        result = L
    return result
```

```python 
def all_perms_comp(s):
    ''' (str) -> list of str
    Returns all permutations of the given string
    using list comprehensions.
    '''
    if (len(s) < 2):
        result = [s]
    else:
        result = [c + perm
                  for i, c in enumerate(s)
                  for perm in perms_comp(s[:i] + s[i + 1:])]
    return result
```

#### Question 3
```
# part A
STEP 1: [(1, 2), (3, 4), (1, 4), (5, 6), (5, 7), (1, 7)]
STEP 2: [(11, 12), (10, 12), (13, 14), (15, 16), (19, 20), (18, 20), (17, 20), (15, 20), (13, 20), (10, 20)]
```

```python
# part B
from math import *


def f2(a, b, r):
    ''' (int, int, float) -> list of (int, int)
    REQ: 0 < r < 1.
    '''
    if a >= b:
        return []  # return empty list
    c = floor(a + (b - a) * r)
    return [(a, b)] + f2(c + 1, b, r) + f2(a, c, r)
```

#### Question 4
```python
# part A
def listmerge(l1, l2):
    """ (CustomerNode, CustomerNode) -> CustomerNode

    Merge the linked lists headed by l1 and l2 into a single list with
    ticket_num in increasing order.
    Return the head of the merged list

    REQ: Lists headed by l1 and l2 are each sorted by ticket_num, and
    each CustomerNode has unique ticket_num

    """
    # initialize list to return and its last node
    new_list = None
    last = None

    # while both lists not empty
    while l1 != None and l2 != None:
        # test which head of list has smaller ticket_num and
        # append corresponding node to new_list
        if l1.get_ticket_num() < l2.get_ticket_num():
            if new_list == None:
                new_list = l1
            else:
                last.next = l1

            last = l1
            l1 = l1.next

        else:
            if new_list == None:
                new_list = l2
            else:
                last.next = l2

            last = l2
            l2 = l2.next

    # append any remaining nodes to new_list
    if l1 == None:
        if new_list == None:
            new_list = l2
        else:
            last.next = l2

    else:
        if new_list == None:
            new_list = l1
        else:
            last.next = l1

    # return merged list
    return new_list
```