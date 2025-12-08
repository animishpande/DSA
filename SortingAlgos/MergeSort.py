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