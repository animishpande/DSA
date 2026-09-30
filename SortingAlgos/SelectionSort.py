# Selection Sort Implementation
# Time: O(n^2), Space: O(1)
C = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(C)
print(C)


'''
Pseudo Code for Selection Sort
for (j = 0; j < n - 1; j++)
    int iMin = j;
    for (i = j + 1; i < n; i++)
        if (a[i] < a[iMin])
            iMin = i
    if (iMin != j)
        swap(a[j], a[iMin])
'''
A = [8,5,3,4,9,2,1]

def selectionSort(arr):
    n = len(arr)
    for j in range(0, n - 1):
        iMin = j
        for i in range(j + 1, n):
            if (arr[i] < arr[iMin]):
                iMin = i
        if iMin != j:
            arr[j], arr[iMin] = arr[iMin], arr[j]

selectionSort(A)
print(A)