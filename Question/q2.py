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

# Initialize an empty list for the sum
sum_list = []

# Calculate the minimum length of the two lists
min_len = min(len(list1), len(list2))

# Add elements from both lists up to the length of the shorter list
for i in range(min_len):
    sum_list.append(list1[i] + list2[i])

# Add any remaining elements from the longer list (if any)
if len(list1) > len(list2):
    sum_list.extend(list1[min_len:])
else:
    sum_list.extend(list2[min_len:])

# Print the original lists and the sum of lists from left
print("Original lists:")
print(list1)
print(list2)
print("Sum of lists from left:")
print(sum_list)
