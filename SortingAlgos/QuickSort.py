# Quick Sort Algorithm
# Time: O(N*log N), Space: O(N)

E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]
    
    L = quick_sort(L)
    R = quick_sort(R)
    
    return L + [p] + R

print(E)
F = quick_sort(E)
print(F)


'''
Pseudo code for Quick Sort
function quicksort(arr):
    if length of arr <= 1:
        return arr

    pivot = arr[middle index]

    left = []
    right = []
    middle = []

    for each element x in arr:
        if x < pivot:
            append to left
        if x == pivot:
            append to middle
        if x > pivot:
            append to right
    
    return quicksort(left) + middle + quicksort(right)
'''
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        elif i > pivot:
            right.append(i)

    return quickSort(left) + middle + quickSort(right)

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(quickSort(A))