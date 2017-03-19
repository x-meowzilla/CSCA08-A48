Term Test 2 Solution & Marking Scheme - CSCA48 Winter 2017
---------------

####Question 1

+ **a) 8**
    + **Marking:** all or nothing

+ **b) 2^(n-1)**
    + **Justification:** for each insertion except last one, we must insert either the smallest or the largest of the remaining numbers.
    + **Marking:**
        + 2 marks for 2^(n-1)
            + 1 mark if they are off by one (i.e 2^n or 2^(n-1)+1 or 2^(n-1)-1)
        + 2 marks for justification
            + 1 mark if they don't get it, but have some worthwhile ideas (i.e mention something about smallest/largest)
    
+ **c) 6**
    + **Justification:** consider the following heap, where number indicate positions
        ```
                     0
                  /     \
                1         2
              /   \     /   \   
             3     4   5     6
            /
           7
        ```
        + To get desired heap:
            + D must be at index 0
            + on the "vowels" side, E,I,O,U must be at indices 1,3,4,7
                + So E must be at index 1 and U must be at index 4 or 7
                    + if U is at index 4, then I must be at index 3 and O must be at index 7 (1 way)
                    + if U is at index 7 then I,O can be at either of indices 3,4 (2 ways)
            + on the "consonants" side, R,S,T must be at indices 2,5,6
                + So R must be at index 2 and S,T can be at either of indices 5,6 (2 ways)
            + Therefore, the grand total is 3*2=6 ways
    + **Marking:**
        + 2 marks for 6, all or nothing
        + 2 marks for justification
            + 1 mark if they don't get it, but have some worthwhile ideas

---------------

####Question 2
+ **a)**
    ```
    jumble(PINEAPPLE) = PEPPLAINE  <---------------------------------------------
        -> | s = INEAPPLEP                                                      |
           | h = 4                                                              |
           | t = jumble(PPLEP) = PEPPL  <------------------------------------   |   <-- [a]
           v        -> | s = PLEPP                                          |   |
           v           | h = 2                                              |   |
           v           | t = jumble(EPP) = PEP  <------------------------   |   |   <-- [b]
           v           v        -> | s = PPE                            |   |   |
           v           v           | h = 1                              |   |   |
           v           v           | t = jumble(PE) = PE  <----------   |   |   |
           v           v           v        -> | s = EP             |   |   |   |
           v           v           v           | h = 1              |   |   |   |
           v           v           v           | t = jumble(P) = P  |   |   |   |
           v           v           v           | u = jumble(E) = E  |   |   |   |
           v           v           v           | return PE  ---------   |   |   |
           v           v           | u = jumble(P) = P                  |   |   |
           v           v           | return PEP  ------------------------   |   |
           v           | u = jumble(PL) = PL  <----------                   |   |   <-- [b]
           v           v        -> | s = LP             |                   |   |
           v           v           | h = 1              |                   |   |
           v           v           | t = jumble(P) = P  |                   |   |
           v           v           | u = jumble(L) = L  |                   |   |
           v           v           | return PL  ---------                   |   |
           v           | return PEPPL  --------------------------------------   |
           v                                                                    |
           | u = jumble(INEA) = AINE  <----------------------                   |   <-- [a]
           v        -> | s = NEAI                           |                   |
           v           | h = 2                              |                   |
           v           | t = jumble(AI) = AI  <----------   |                   |
           v           v        -> | s = IA             |   |                   |
           v           v           | h = 1              |   |                   |
           v           v           | t = jumble(A) = A  |   |                   |
           v           v           | u = jumble(I) = I  |   |                   |
           v           v           | return AI  ---------   |                   |   <-- [c]
           v           | u = jumble(NE) = NE  <----------   |                   |
           v           v        -> | s = EN             |   |                   |
           v           v           | h = 1              |   |                   |
           v           v           | t = jumble(N) = N  |   |                   |
           v           v           | u = jumble(E) = E  |   |                   |
           v           v           | return NE  ---------   |                   |   <-- [c]
           v           | return AINE  -----------------------                   |
           v                                                                    |
           | return PEPPLAINE  --------------------------------------------------   <-- [d]
    ```
    + **Marking:** all or nothing for each mark as described below
        + 1 mark for jumble(PPLEP) and jumble(INEA) - indicated by [a]
        + 1 mark for jumble(EPP) and jumble(PL) - indicated by [b]
        + 1 mark for return AI and return NE - indicated by [c]
        + 1 mark for return PEPPLAINE - indicated by [d]

+ **b)**
    + AAAA (accept any string of 4 same letters)
    + **Marking:** 2 marks, all or nothing

+ **c)**
    + HALAL (accept any string of form xyzyz)
    + **Marking:** 2 marks, all or nothing

+ **d)**
    + WONTON (accept any string of form uxyvxy)
    + **Marking:** 2 marks, all or nothing
    
---------------

####Question 3
```python
def unright_helper(root, include_root):
    """ (IntBinTreeNode, bool) -> (int, int)
    
    Return a tuple of (sum, num_nodes) where,
        - sum, is the sum of all the numbers in the tree rooted at root
        that are not stored in a node that is a right child (meaning the left child)
        and plus the number stored at the root if the root is included.
        - num_nodes, is the number of nodes in the tree rooted at root 
        that are not right children, plus one if root is included.
    """
    sum = 0
    num_nodes = 0
    if root != None:
        (sum_left, num_nodes_left) = unright_helper(root.left, True)
        (sum_right, num_nodes_right) = unright_helper(root.right, False)
        sum = sum_left + sum_right
        num_nodes = num_nodes_left + num_nodes_right
        
        if include_root:
            sum = sum + root.sum
            num_nodes = num_nodes + 1
            
    return (sum, num_nodes)
    
    
def unright_avg(root):
    """ (IntBinTreeNode) -> float
    
    Return the average of all the numbers in the tree rooted at root 
    that are not stored in a not that is a right child (of another node).
    """
    (sum, num_nodes) = unright_helper(root, True)
    return sum/num_nodes
```
