# SINGLY LINKED LIST
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
        
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

# print(Head)


# TRAVERSING A SINGLY LINKED LIST
curr = Head
while curr:
    print(curr)
    curr = curr.next
    
    
# DISPLAYING A SINGLY LINKED LIST
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        
    print(' -> '.join(elements))
    
display(Head)

# SEARCH FOR A NODE VALUE
def search(head, val):
    curr = head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next
    return False

ans = search(Head, 4)
print(ans)



# DOUBLY LINKED LIST
class DoubleNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

head = tail = DoubleNode(1)

# DISPLAY A DOUBLY LINKED LIST
def displayDouble(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        
    print(' <-> '.join(elements))
    
displayDouble(head)

# INSERTING AT THE BEGINNING
def insertInBeginning(head, tail, val):
    new_node = DoubleNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insertInBeginning(head, tail, 3)
displayDouble(head)

# INSERTING AT THE END
def insertInEnd(head, tail, val):
    new_node = DoubleNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insertInEnd(head, tail, 7)
displayDouble(head)