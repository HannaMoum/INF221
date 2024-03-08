""" Quicksort algorithm based on pseudo-code from "Introduction to algorithms", 4.ed, by Cormen, Leierson, Riverst and Stein.
    (page 183)
"""
def quicksort(A, p, r):
    if p < r:
        # Partition subarray around pivot. Pivot ends up in position A[q]
        q = partition(A, p, r)
        quicksort(A, p, q - 1) # Recursively sort the lower-than-the-pivot side 
        quicksort(A, q + 1, r) # Recursively sort the higher-than-the-pivot side


def partition(A, p, r):
    x = A[r]                        # pivot
    i = p - 1                       # highest index on the low side
    for j in range(p, r):           # process all elements, expect the pivot
        if A[j] <= x:               # move element to the low side if it belongs there, and update the highest index i
            i += 1
            A[i], A[j] = A[j], A[i] 
    A[i + 1], A[r] = A[r], A[i + 1] # move pivot to it's correct position, just to the left of the low side
    return i + 1



if __name__ == "__main__":
    import numpy as np
    array=[2,3,55,6,7,8, 239, 10]
    array = np.arange(998) # i can't run over 999...
    arr_copy = array.copy()  # Make a copy of the array to sort
    quicksort(arr_copy, 0, len(arr_copy) - 1)  # Sort the array
    print(arr_copy)
