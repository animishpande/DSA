# Merge Sort Algorithm Implementation
# Time: O(nlogn), Space: O(n)
D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        
        left_arr = arr[:m]
        right_arr = arr[m:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # arr idx
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
     
print(D)       
merge_sort(D)
print(D)



'''
Pseudo Code for Merge Sort
MERGE_SORT(array):
    if length of array <= 1:
        return array
    
    mid = length of array / 2

    left = MERGE_SORT(array left of mid)
    right = MERGE_SORT(array right of mid)

    return MERGE(left, right)

MERGE(left, right):
    result = []

    while both are non empty:
        if left[i] <= right[j]:
            add left[i]
        else:
            add right[j]

    dump remaining elements to whichever side isn't empty into result

    return result
'''
X = [2, 4, 3, 1, 8, 7, 9, 5]
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)
    
Y = mergeSort(X)
print(X)
print(Y)

'''
merge_sort([3, 1, 2])
├── merge_sort([3])        ← base case, returns [3]
├── merge_sort([1, 2])
│   ├── merge_sort([1])   ← base case, returns [1]
│   ├── merge_sort([2])   ← base case, returns [2]
│   └── merge([1], [2])  → [1, 2]
└── merge([3], [1, 2])   → [1, 2, 3]  ✅
'''