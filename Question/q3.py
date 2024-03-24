# Consider two sets with the following data.
# S1={1,4,5,6,9,11}
# S2={2,3,4,6,11}
# Use suitable methods to write a Python code for accomplishing the following operations on sets. 
# (i) Returns a Merged set without duplicates 
# (ii) Returns a set which contains the common elements from both the sets.
# (iii) Remove an element from the list and raise an error if the element does not exist. 
# (iv) Return a set that contains all items from both sets, except items that are present in both
# (V) Return a set which will contain all the elements of the first set and not in the second one

# Create two sets.
s1 = {1, 4, 5, 6, 9, 11}
s2 = {2, 3, 4, 6, 11}

# (i) Merged set without duplicates
merged = s1 | s2
print("(i) Merged set:", merged)

# (ii) Common elements from both sets.
common = s1 & s2
print("(ii) Common set:", common)

# (iii) Remove an element and handle errors.
element = 10
try:
    s1.remove(element)
except KeyError:
    print("(iii) Element", element, "not found in s1")

# (iv) Set difference (items in either set but not both).
diff = s1 ^ s2
print("(iv) Set difference:", diff)

# (V) Elements in the first set and not in the second one.
diff2 = s1 - s2
print("(V) Set difference 2:", diff2)
