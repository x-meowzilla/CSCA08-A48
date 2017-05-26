CSCAO8 Fall 2016 - Term Test 2 Solution
----------

Q1
----------
``` 
STEP 1: 2
STEP 2: [1, 99, 3] [1, 99, 3]
STEP 3: [1, 99, 3] [1, 2, 3]
STEP 4: [[1, 2, 3], 88] [[1, 2, 3], [4, 99, 6]]
STEP 5: 3 [1, 99, 3]
STEP 6: 100 99
STEP 7: 2 0 1 [1, 99, 3]
```
* 1 mark each for line 1-4;
* 2 marks each for line 5-7.
* **ALL or NOTHING**

----------


Q2
----------
```python
def get_domain(input_email):
    """
    No external documentation required.
    """
    # setting up condition variables
    found_at = False
    found_second_at = False
    found_period = False
    
    # loop through the input string, the loop stop if first '@' present or index
    # is greater than the length of the input string
    index = 0
    while(index < len(input_email) and not (found_at)):
        # check if the char at index 'index' is '@'
        if (input_email[index] == '@'):
            # set found_at to True and store the index to variable at_index
            found_at = True
            at_index = index
        # increase the index counter by 1
        index += 1
    
    # loop through the rest of the string, the loop stop if second '@' present
    # or index is greater than the length of the input string
    while(index < len(input_email) and not (found_second_at)):
        # case 1: check if the char at index 'index' is '@'
        if (input_email[index] == '@'):
            # set found_second_at to True to terminate the loop
            found_second_at = True
        # case 2: check if the char at index 'index' is '.'
        elif (input_email[index] == '.'):
            # set found_period to True and store the index to variable period_index
            found_period = True
            period_index = index
        # increase the index counter by 1
        index += 1
        
    # second at present or period not present in the string, invalid result
    if (found_second_at or not(found_period)):
        result = "INVALID"
    # otherwise, slice the input string to find the domain
    else:
        result = input_email[at_index+1:period_index]
        
    # return the domail as result
    return result
```
* **Internal commenting: /8**
    * 0 = no comments
    * 1 = a few scattered comments
    * 2 = regular, but mostly unhelpful comments
    * 4 = comments just describe what the code does
    * 5 = comments somewhat helpful
    * 6 = some minor elements not fully explained
    * 7 = one or two bad comments, or sections not fully explained
    * 8 = comments fully explain the code

* **Code /12**
    * 0 = no attempt made
    * 2 = some attempt made
    * 4 = shows a basic understanding of python
    * 6 = basic structure right
    * 8 = several mistakes or inefficient solution (e.g., putting one loop inside the other)
    * 10 = minor mistakes or **nested while loop structure (it must be working)**
    * 12 = code fully reconstructedcorrect

----------


Q3
----------
```python
def domain_mapper(file_list):
    """ (list of str) -> dict of {str: list of str}
    Given a list of file names, the function read each file in the file list and
    search domains in each file. Then generates a dictionary of domain-list of 
    file name pair that maps each domain founed in the file to a list of file 
    names in which it occurs.
    
    REQ: strings must represent valid files!
    """
    # create a dictionary to store each mapping
    result = {}
    # loop through each file in the file list
    for fname in file_list:
        # open the file for reading
        fhandle = open(fname, 'r')
        
        # read each line in the file
        for line in fhandle:
            # split the line into a list of string
            line_list = line.split()
            
            # loop through each string in the line_list
            for word in line_list:
                # call get_domain() function to find if word contains domain
                domain = get_domain(word)
                
                # if the domain is valid, then perfom mapping operation
                if (domain != "INVALID"):
                    # check if the key domain is in the dictionary
                    if (domain in result):
                        # append the file name to value list
                        result[domain].append(fname)
                    # otherwise create a new key-value pair to store domain and file list
                    else:
                        result[domain] = [fname]
                    
        # close the file
        fhandle.close()
        
    return result
```
* **Docstring /6**
    * +1 for good type contract **(must be (list of str) -> dict of {str: list of str})**
    * +1 for description
    * +1 for fully describing everything
    * +1 for REQs (strings must represent valid files or files must exist and readable!)
    * +2 for formatting everything correctly

* **Internal Commenting: /5**
    * 0 = no comments
    * 1= some comments, but not more helpful than reading the code
    * 3 = comments present and sensible
    * 4 = some minor elements not fully explained
    * 5 = comments fully explain the code

* **Code /9**
    * +1 for good function name
    * +1 for looping through the list of files
    * +1 for opening file
    * +1 for closing file (in appropriate place)
    * +1 for reading text from file
    * +1 for splitting text to process each word
    * +1 for checking if valid domain
    * +1 for adding to dict (seen before)
    * +1 for adding to dict (new domain)