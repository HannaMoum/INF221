"""
Python program for implementation of MergeSort

Merges two subarrays of A[].
First subarray is A[p...q]
Second subarray is A[q+1...r]

Inspired by code contributed by Mohit Kumra, at https://www.geeksforgeeks.org/python-program-for-merge-sort/

"""

def merge(A, p, q, r):
    # Calculate the sizes of the left and right halves
    n1 = q - p + 1
    n2 = r - q

    # Create temporary arrays `L` and `R` to hold the left and right halves
    L = [0] * n1
    R = [0] * n2

    # Copy the elements of the left half into L
    for i in range(n1):
        L[i] = A[p + i]

    # Copy the elements of the right half into R
    for j in range(n2):
        R[j] = A[q + j + 1]

    # Merge the sorted L and R arrays back into A
    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements from `L` into `A`
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements from `R` into `A`
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergeSort(A, p, r):
    if p < r:
        q = p + (r - p) // 2

        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


if __name__ == "__main__":
    # Test the array
    def printArray(A, n):
        for i in range(n):
            print(A[i], end=" ")
        print()

    arr = [12, 11, 13, 5, 6, 7]
    import numpy as np
    arr = np.arange(8000)
    n = len(arr)

    # print("Original array is:", end="\n")
    # printArray(arr, n)

    mergeSort(arr, 0, n-1)
    print(arr)
    # print("Sorted array is:", end="\n")
    # printArray(arr, n)