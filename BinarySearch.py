A = [-3, -1, 0, 1, 4, 7]

# Naive O(n) solution
if -1 in A:
    print(True)
else:
    print(False)
    
# Traditional Binary Search - O(log N)
def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N - 1
    
    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return False

val = binary_search(A, 4)
# print(val)

# Condition Based (Sorted Array)
B = [False,False,False,True,True,True]
def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1
    
    while L < R:
        M = (L + R) // 2
        
        if arr[M]:
            R = M
        else:
            L = M + 1
            
        return L
    
print(binary_search_condition(B))