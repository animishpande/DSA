# STACKS
stk = []
stk.append(5)
stk.append(4)
stk.append(3)
stk.append(2)
stk.append(1)
print(stk)
x = stk.pop()
print(x)
print(stk)
print(stk[-1])

# QUEUE
from collections import deque

q = deque()

q.append(5)
q.append(6)
q.append(7)
print(q)

# dequeue from left
x = q.popleft()
print(q)
print(x)

# Peek in queue
print(q[-1])
print(q[0])