arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    print(arr[i])

print(f"arr: {arr[-1]}")
print(f"arr elements: {arr[:-1]}")

s = "BDA"
slist = list(s)
print(slist)

n = [0] * 10
print(n)

# Adding Elements to list
# append only one element at the end 
arr.append(6)
print(arr[-1])
# append multiple elements at the end
arr.extend([7, 8, 9, 10])
print(arr)
# insert an element at a specific position
arr.insert(0, -1)
print(arr)


# Removing Elements from the list
arr.remove(-1)
print(arr)
arr.pop()
print(arr)
del arr[-3]
print(arr)