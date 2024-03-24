# Create two lists of integers with different lengths. Add the Contents of the list from the left and create a new list which contain the sum of elements.
# Example:
# Original lists:
# [2, 4, 7, 0, 5, 8] 
# [3, 3, -1, 7] 
# Sum of lists from left:
# [5, 7, 6, 7, 5, 8]

# Take user input for the two lists
list1 = [int(x) for x in input("Enter the first list of integers (separated by spaces): ").split()]
list2 = [int(x) for x in input("Enter the second list of integers (separated by spaces): ").split()]

# Determine the shorter list
shorter_list = list1 if len(list1) <= len(list2) else list2

# Calculate the sum of lists element-wise from left to right
sum_list = []

# Iterate through the shorter list and add corresponding elements from both lists
for i in range(len(shorter_list)):
    sum_list.append(list1[i] + list2[i])

# Extend sum_list with any remaining elements from the longer list
if len(list1) > len(list2):
    sum_list.extend(list1[len(shorter_list):])
else:
    sum_list.extend(list2[len(shorter_list):])

# Print the original lists and the sum of lists from left
print("Original lists:")
print(list1)
print(list2)
print("Sum of lists from left:")
print(sum_list)
