"""
HEAPSORT

Best: O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)

Stable: False

A heap sort is a sorting algorithm that is 
based exclusively upon a binary heap tree.
It involves finding the largest element, and
storing it at the end of an unsorted collection.

A heap is a complete binary tree in which
every level, except possibly the last, is 
completely filled, and all nodes are as far
left as possible.

A max heap is in one in which the value in 
each internal node is greater than or equal
to the values in the children of that node.
"""

def heapsort(arr):
    """
    Implementation of Heap Sort Algorithm

    1) Build a max heap from the input array
    2) Swap the root node with the last element
    3) Recursively repeat step 1) and 2) for the 
        reminder elements in the array since the
        last element is already in place
    
    ::param: arr the input array to be sorted
    """

    # build a max heap
    build_max_heap(arr)
    n = len(arr)

    # continue heap sort until length = 1
    while (n > 1):
        # swap the root (largest) and last element
        arr[0], arr[n-1] = arr[n-1], arr[0]
        # re-heapify with one less element
        _heapify(arr, n-1, 0)
        n -= 1
    
    print("Heap:\t{}".format(arr))

def build_max_heap(arr):
    """
    Construct a max heap from input array arr

    ::param: arr the input array
    """
    n = len(arr)
    for i in range(n-1, -1, -1):
        # loop through the input array and heapify 
        # starting from the last element
        _heapify(arr, n, i)
        #print('\t{0}:\t{1}'.format(i, arr))

def _heapify(arr, n, i):
    """
    Build a max heap from input array starting at index i

    ::param: arr the input array
    ::param: n the size of heap
    ::param: i the index of sub-root element to start
    """

    largest = i
    left = 2*i+1
    right = 2*i+2

    # check if left child exists and is greather than root
    if left < n and arr[largest] < arr[left]:
        largest = left
    
    # check if right child exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest == i:
        # either the subtree is already heapified
        # or the largest(root) is at a leaf node
        return
    
    # swap if largest is not at the root
    arr[i], arr[largest] = arr[largest], arr[i]
    # re-heapify the sub-tree when largest is not the root
    _heapify(arr, n, largest)
    