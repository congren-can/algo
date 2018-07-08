#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sort

BubbleSort - https://medium.com/basecs/bubbling-up-with-bubble-sorts-3df5ac88e592
MergeSort - https://medium.com/basecs/making-sense-of-merge-sort-part-1-49649a143478
HeapSort - https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82
QuickSort Part I - https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313
QuickSort Part II - https://medium.com/basecs/pivoting-to-understand-quicksort-part-2-30161aefe1d3



A sorting algorithm is said to be stable 
if two objects with equal keys appear in 
the same order in sorted output as they 
appear in the input unsorted array.
"""

import numpy as np

from bubble import bubblesort
from merge import mergesort
from heap import heapsort
from quick import quicksort

array = np.random.randint(100, size=15).tolist()
print('Input:\t{}\n'.format(array))

bubblesort(array[:])
heapsort(array[:])
mergesort(array[:])

#quicksort(cp.copy(array))
#quicksort([9,5,2,6,1,11,3])
#quicksort([3,1,2])