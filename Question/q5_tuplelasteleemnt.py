# Write a python program to create a list and compute the sum of all the elements of each tuple stored inside a list of tuples.
# From the original list of tuples replace 10 with the last each number in each tuple.
# Example
# list of tuples [(1,2,6),(2,3,-6),(3,4),(2,2,2,2)]
# Sum of all elements of each tuple stored inside the list. 
# [9,-1,7,8]
# After replacement [(1,2,10),(2,3,10),(3,10),(2,2,2,10)]

# Original list of tuples
tuples = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

# Initialize a list to store the store_sum
store_sum = []

# Calculate the sum of all elements of each tuple and replace the last element with 10
modified = []
for i in tuples:
    # Calculate the sum of elements in the tuple
    tuple_sum = sum(i)

    # Store the sum in the store_sum list
    store_sum.append(tuple_sum)

    # Replace the last element with 10
    i = i[:-1] + (10,)

    # Append the modified tuple to the new list
    modified.append(i)

# Print the store_sum list and modified list
print("Sums of elements in each tuple:", store_sum)
print("Modified list:", modified)
