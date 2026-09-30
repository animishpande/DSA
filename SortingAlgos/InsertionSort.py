# Insertion Sort Implementation
# Time: O(n^2), Space: O(1)
B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
            
insertion_sort(B)
print(B)

'''
Pseudo Code for Insertion Sort
for i: 1 to length(A) - 1
    j = i
    while j > 0 and A[j - 1] > A[j]
        swap A[j] and A[j - 1]
        j = j - 1
'''
A = [2, 5, 3, 7, 4, 9, 8]

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if (arr[j - 1] > arr[j]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j = j - 1

insertionSort(A)
print(A)