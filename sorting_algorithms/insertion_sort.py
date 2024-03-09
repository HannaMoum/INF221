""" The insertion sort algorithm based on the pseudocode from "Introduction to algorithms", 4.ed, by Cormen, Leierson, Riverst and Stein.
    (page 19)
"""
def insertionSort(A):
    # Loop over the array from the second element
    for i in range(1, len(A)): 
        key = A[i]
        # Inserting A[i] into the sorted part of the array, i.e. A[0:i-1]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

if __name__ == "__main__":
    # Test the insertion sort function
    array = [12, 11, 13, 5, 6, 7]
    print("The original array is:", array)

    insertionSort(array)
    print("The sorted array is:", array)
