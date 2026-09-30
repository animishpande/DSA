# Bubble Sort Algorithm Implementation
# Time: O(n^2), Space: O(1)
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                
bubble_sort(A)
print(A)

'''
Pseudo Code for bubble sort
for i from 1 to N
    for j from 0 to N - 1
        if a[j] > a[j + 1]
            swap(a[j], a[j + 1])
'''
arr = [2, 3, 9, 5, 4, 8, 1]
def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    
bubbleSort(arr)
print(arr)