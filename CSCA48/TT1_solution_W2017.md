Term Test 1 Solution & Marking Scheme - Winter 2017
---------------

####Question 1

**a) The shortest sequence that reads GRAPE and prints PAGER is**

    IN,IN,IN,PR,EX,EX,PR,EX

+ This is the only correct answer.
+ Give 2 marks if correct, 0 if incorrect.

**b) Here's why it's impossible to read PEACH and print CHEAP.**

    To print C first, PEA must be inserted into the steue, which makes it impossible to extract E before A or P.

+ The only way to be brief is to argue that printing C first necessitates putting PEA in the steue.
+ Give 1 mark for good argument, 1 mark for being brief and clear.

**c) It's possible to read CRABAPPLE and print APPLECARB. Here's how.**

    IN,IN,IN,EX,IN,IN,PR,PR,PR,PR,EX,EX,EX,EX

+ The IN,EX pair may be replaced by PR if we replace a later PR by an IN,EX pair. So there are 5 shortest sequences. We extract one letter immediately after inserting it so that the subsequent EX,EX,EX,EX sequence will extract what's left in the steue (CRBA) in order CARB.
+ Give 1 mark for saying it's possible,
+ Give 3 marks for the short sequence (all or nothing).

---------------

####Question 2

```python
    def __init__(self: 'Queue') -> None:
        self._contents = Steue()

    def enqueue(self: 'Queue', item: 'object') -> None:
        self._contents.insert(item)

    def dequeue(self: 'Queue') -> object:
        # Extract and re-insert an item, which behave like
        # a pop and a push on a stack, and make
        # the subsequent extract behave like a dequeue.
        temp = self._contents.extract()
        self._contents.insert(temp)
        return self._contents.extract()

    def isempty(self: 'Queue') -> bool:
        return self._contents.isempty()
```

+ Give 1 mark for \_\_init\_\_
+ Give 1 mark for enqueue
+ Give 1 mark for isempty
+ Give 7 marks for dequeue
    + 4 marks for code
        + 2 marks for extract/insert pair (all or nothing)
        + 1 mark for subsequent extract
        + 1 mark for return
        + Order of lines is important.
            + It has to be extract, insert, extract. Extract, extract, insert won't work (if only one element left).
    + 3 marks for comments
        + 1 mark for just saying what code does without explaining why
        + give full marks even if explanation is a bit vague

---------------

####Question 3

**a) Linked list is unchanged**
```
 myhead ---+                                        |     +--- mydata  
           |                                        |     |  
           v                                        |     v
        +-------+   +-------+   +-------+           |   +---+
        | 2 | *-|-->| 3 | *-|-->| 4 | *-|--> None   |   | 3 |
        +-------+   +-------+   +-------+           |   +---+
```

**b) Nodes are reordered with 5 moving to between 3 and 2**
```
 myhead ---+                                                                |     +--- mydata  
           |                                                                |     |  
           v                                                                |     v
        +-------+   +-------+   +-------+   +-------+   +-------+           |   +---+
        | 6 | *-|-->| 4 | *-|-->| 3 | *-|-->| 5 | *-|-->| 2 | *-|--> None   |   | 5 |
        +-------+   +-------+   +-------+   +-------+   +-------+           |   +---+
```

+ Give 2 marks for linked list (all or nothing)
+ Give 1 mark for mydata

**c) Here is the docstring**
```python
    def demote2(head):
        """ (LLNode) -> object
 
        Move the second node in the linked list with first node head
        to the second last position in the list.
        Return the data in the moved node.
        REQ: The linked list with first node head has at least 3 nodes.
        """
```

+ Give 1 mark for type contract
+ Give 2 marks for describing how the second node is moved
+ Give 2 marks for REQ (1 mark if they say at least 1, 2, or 4 nodes).
+ Ignore whether they give examples or not.

---------------

####Question 4
```python
    def sorted_kroy_list_insert(head, newnum):
        """ (KroyNode, int) -> KroyNode
 
        Move the second node in the linked list with first node head to the second last position in the list.
        Return the data in the moved node.
        REQ: The linked list with first node head has at least 3 nodes.
        """
        newnode = KroyNode(newnum)
        if head == None:
            # restore stolen code here
            head = newnode                      # ----

        elif newnum < head.number:
            # restore stolen code here
            newnode.next1 = head                # ----
            newnode.next2 = head.next1          # ----
            head = newnode                      # ----

        else:
            prev = head
            curr = head.next1
            while curr != None and curr.number <= newnum:
                prev = curr
                curr = curr.next1
            # restore stolen code here
            prev.next1 = newnode                # ----

            if curr != None:
                # restore stolen code here
                prev.next2 = curr               # ----
                newnode.next1 = curr            # ----
                newnode.next2 = curr.next1      # ----

        return head
```

+ Give 1 mark for each line (there are 8 of them)
    + Put another way, 1 mark for each pointer set correctly.
    + Deduct 1 mark for each incorrectly set pointer.
+ They only supposed to add assignment statements.
    + For each of the 4 pieces of "stolen code", give zero if they have statements that are not assignments (e.g., if statements).
