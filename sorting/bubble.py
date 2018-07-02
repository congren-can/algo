"""
BUBBLE SORT

Best: O(n)
Average: O(n^2)
Worst: O(n^2)

Stable: True

A bubble sort algorithm walks through a collection
and compares two elements at a time.  If the elements
are out of order, it swaps them.  It continues to 
swap out-of-order elements until the entire collection
is sorted.
"""

def bubblesort(arr):
    """
    Implementation of Bubble Sort Algorithm

    1) Go through the entire array and comparing two elements at a time.
    2) Swap the two elements if they are in the wrong order.
    3) After the first path, the last element is in its right place.
    4) Repeat step 1) and 2) until the array is sorted 
    """

    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print("Bubble:\t{}".format(arr))