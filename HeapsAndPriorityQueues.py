# Building Min Heap using Heapify Function
# Time: O(n), Space: O(1)
print("MIN HEAP: ")
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

print("Heapify the Array A:")
print(A)

# Heap push - Inserting an element into the heap
# Time: O(log N)

heapq.heappush(A, 4)
print("Heap Push element - 4:")
print(A)

# Heap pop - Extracting minimum element out of the heap
# Time: O(log N)

minE = heapq.heappop(A)
print("Heap Pop element - 3:")
print(A, minE)

# Peek at min heap value
# Time: O(1)
print(A[0])

# Heap Sort - Sorting the array
# Time: O(n log n), Space: O(n)

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    newlist = [0] * n
    
    for i in range(n):
        minn = heapq.heappop(arr)
        newlist[i] = minn
        
    return newlist

myheap = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(heapsort(myheap))

# Heap Push Pop
# Time: O(log n)
heapq.heappushpop(A, 199)
print(A)


# Max Heap
print("MAX HEAP:")
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
print(f'Before heapify {B}')
for i in range(n):
    B[i] = -B[i]
    
heapq.heapify(B)
n = len(B)

for i in range(n):
    B[i] = -B[i]

print(f'After heapify {B}')
largest = heapq.heappop(B)
print(largest)

# Max heap push
heapq.heappush(B, -7)
print(B)


# Building Heap from Scratch
# Time: O(n log n)
print("BUILDING HEAP FROM SCRATCH")
C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for x in C:
    heapq.heappush(heap, x)
    print(heap)
    
    
# ******IMPORTANT******
# Putting tuples as items on the heap
D = {
    5: 4,
    3: 2,
    4: 4
}

heap = []

for k, v in D.items():
    print(k, v)
    heapq.heappush(heap, (v, k))
    
print(heap)
