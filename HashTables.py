# Hash Sets - Set in python
s = set()

# Add item to hash set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)

# Lookup if an item is in the set
if 71 in s:
    print(True)
else:
    print(False)
    
# Remove an item from the set
s.remove(3)
print(s)

# Set construction with string - O(S) where S is the length of the string
mystring = "aaaaaaaaaaaaaaaaassssssssssssssssssddddddddddddddddwwwwwwwwwwewewew"
sett = set(mystring)
print(sett)

# Loop over every item
for x in s:
    print(x)
 
    
# Hash Maps - Dictionary in python
d = {'tiger': 1, 'lion': 2, 'giraffe': 3}
print(d)

# Add key value pair in dict - O(1)
d['zebra'] = 4
print(d)

# Check if a key is in dictionary - O(1)
if 'lion' in d:
    print(True)
    
# Check the value corresponding to a key in dictionary - O(1)
print(d['lion'])

# Loop over the key value pairs of the dictionary - O(n)
for key, val in d.items():
    print(f"{key} : {val}")
    
# Default Dict is a default hash map which returns 0 when the element looking up is not present in the dict
# It also creates a new dict key value with the passed in element
from collections import defaultdict

default = defaultdict(int)
print(default[2])
print(default)

# Counter is used to count the number of unique elements in the given set
from collections import Counter
counter = Counter(mystring)
print(counter)