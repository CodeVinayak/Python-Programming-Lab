# Consider two sets with the following data.
# S1={1,4,5,6,9,11}
# S2={2,3,4,6,11}

# Create two sets.
s1 = {1, 4, 5, 6, 9, 11}
s2 = {2, 3, 4, 6, 11}

# (i) Merged set without duplicates
merged = s1.union(s2)
print("(i) Merged set:", merged)

# (ii) Common elements from both sets.
common = s1.intersection(s2)
print("(ii) Common set:", common)

# (iii) Remove an element and handle errors.
element = 10
try:
    s1.remove(element)
except KeyError:
    print("(iii) Element", element, "not found in s1")

# (iv) Set difference (items in either set but not both).
diff = s1.symmetric_difference(s2)
print("(iv) Set difference:", diff)

# (V) Elements in the first set and not in the second one.
diff2 = s1.difference(s2)
print("(V) Set difference 2:", diff2)
