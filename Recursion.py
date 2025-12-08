def recursion(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return recursion(n - 1) + recursion(n - 2)
    
recursiveVal = recursion(15)
print(recursiveVal)