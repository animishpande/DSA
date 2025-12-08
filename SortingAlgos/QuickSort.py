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