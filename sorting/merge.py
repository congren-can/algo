"""
MERGE SORT

Best: O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)

Stable: True

A merge sort algorithm is a divide and conquer algorithm
that splits an unsorted collection into 2 havles; it sorts 
the 2 havles, and then merges them together to form one, 
sorted collection - all of this using recursion.
"""

import math
import numpy

def mergesort(arr):
     print("Merge:\t{}".format(merge_sort(arr)))


def merge_sort(arr):
    """
    Implementation of Merge Sort Algorithm
    """
    n = len(arr)
    if n in {0, 1}:
        # An array of size 0 or 1 is already sorted
        return arr
    
    # Split the unsorted array in the middle
    m = math.floor(n/2)

    # Recursively sort the two sub-arrays
    sorted_arr_1 = merge_sort(arr[0:m])
    sorted_arr_2 = merge_sort(arr[m:n])

    # Merge the two sorted sub-arrays
    return merge(sorted_arr_1, sorted_arr_2)
    

def merge(arr_1, arr_2):
    """
    Merge the two sorted arrays in space
    but compromise on runtime with O(n^2) 

    Basic idea is as follows:
    1) Loop through array 2 in reverse order.
    2) For each element in array 2, find
        the smallest element in the array 1 
        that is greater than the element 
        in array 2.
    3) If such element is found, insert the 
        element in array 2 at that position
        in array 1 where the smallest element 
        is found and shift everything to the
        right by one position. Remove the last
        element in array 1 and insert it back
        into array 2.

    Essentially what this is doing is inserting
    each element in array 2 back into array 1 in 
    the reverse order.

    ::param: arr_1 sorted array 1
    ::param: arr_2 sorted array 2
    """

    # Loop array_2 in reverse order
    for i in range(len(arr_2)-1, -1, -1):
        # Loop array_1 in order
        for j in range(len(arr_1)):
            # Find the smallest element in arr_1
            # that is greater than the element in 
            # arr_2
            if arr_1[j] > arr_2[i]:
                # Remove the last element in arr_1
                # Need to insert this into arr_2 later
                last_arr_1 = arr_1.pop()
                # Remove the element in arr_2
                # and insert it into arr_1 where
                # the smallest element greater 
                # than it is found
                arr_1.insert(j, arr_2.pop(i))
                # Insert what use to be the last
                # element in arr_1 into arr_2
                arr_2.insert(i, last_arr_1)
    
    # merge the two arrays to form the final merged sorted array
    return arr_1 + arr_2