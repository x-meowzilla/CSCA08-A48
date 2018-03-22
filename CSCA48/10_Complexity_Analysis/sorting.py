#global list
l = [9,2,3,5,4,1,8,7,0,6]
#l = [0,1,2,3,4,5,6,7,8,9]
#==============================================================================
#==============================================================================


def bubble_sort(l):
    ''' (list of sortable objects) -> list

    Returns a copy of the list sorted in ascending order by using bubble sort.

    '''
    l_copy = l[:]
    #take the length of the list that needed to be sorted
    for sort_length in range(len(l_copy)-1,0,-1):
        #loop thu every element and compare the value of next element
        for i in range(sort_length):
            if l_copy[i] > l_copy[i+1]:
                temp = l_copy[i]
                l_copy[i] = l_copy[i+1]
                l_copy[i+1] = temp
    return l_copy

print("Bubble Sort")
print(bubble_sort(l))
print()

#==============================================================================
#==============================================================================


def selection_sort(l):
    ''' (list of sortable objects) -> list

    Returns a copy of the list sorted in ascending order by using selection
    sort.

    '''
    l_copy = l[:]
    #take the length of the list that needed to be sorted
    for sort_length in range(len(l_copy)-1,0,-1):
        max_index = 0
        for i in range(sort_length):
            if l_copy[max_index] < l_copy[i+1]:
                max_index = i+1

        #switching numbers
        temp = l_copy[sort_length]
        l_copy[sort_length] = l_copy[max_index]
        l_copy[max_index] = temp
    return l_copy 

print("Selection Sort")
print(selection_sort(l))
print()

#==============================================================================
#==============================================================================


def merge_sort(l):
    ''' (list of sortable objects) -> list

    Returns a copy of the list sorted in ascending order, with original list
    be left unchanged.

    '''
    l_copy = l[:]
    #base case: 0 or 1 item in the list
    if (len(l) <= 1):
        return l
    else:
        #recursive steps
        sort1 = merge_sort(l_copy[:len(l)//2])
        sort2 = merge_sort(l_copy[len(l)//2:])
        return merge_sort_helper(sort1, sort2)


def merge_sort_helper(l1, l2):
    ''' (list, list) -> list

    A helper function of my_sort, return a copy of sorted list

    '''
    sort_result = []
    #if both lists are not empty, compare index 0 value, append smaller one 
    #to result list, and pop out the smaller one from the list
    while (l1 != [] and l2 != []):
        if (l1[0] < l2[0]):
            sort_result.append(l1[0])
            l1.pop(0)
        else:
            sort_result.append(l2[0])
            l2.pop(0)

    #if any of the list is empty, append the other list to the result list
    if (l1 == []):
        sort_result += l2
    else:
        sort_result += l1

    return sort_result

print("Merge Sort")
print(merge_sort(l))
print()

#==============================================================================
#==============================================================================

def quick_sort(L):
     '''(list) -> list
     Return a copy of L sorted using
     quicksort.
     '''
     if len(L) < 2:
          return L
     pivot = L[0]
     L1 = []
     L2 = [pivot]
     L3 = []
     for item in L[1:]:
          if item < pivot:
               L1.append(item)
          elif item == pivot:
               L2.append(item)
          else:
               L3.append(item)

     return quick_sort(L1) + L2 + quick_sort(L3)


def heap_sort(L):
     '''(list) -> list
     Return a copy of L sorted using heap sort. Note: insert
     a copy of L into the heap so that L is left unchanged.
     '''
     my_heap = Heap(L[:])
     S = []
     while not my_heap.is_empty():
          S.append(my_heap.extract_min())

     return S


def insertion_sort (input_L):
     '''(list) -> list
     Sort L in place using insertion sort. Return L sorted.
     '''
     i = 1
     L = input_L[:]
     while (i < len(L)):
          t = L[i]
          j = i
          while (j > 0 and L[j-1] > t):
               L[j] = L[j-1]
               j = j-1
          L[j] = t
          i = i+1
          
     return L
