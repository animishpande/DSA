# Two pointer approach to sort an algorithm with squares of that number
# A = [-4, -1, 0, 3, 10]
A = [5, 25, 75]

def sortedSquares(arr):
    left = 0
    right = len(arr) - 1
    result = []
    
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1
        else:
            result.append(arr[right] ** 2)
            right -= 1
            
    result.reverse()
    
    return result


val = sortedSquares(A)

print(val)