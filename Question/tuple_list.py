"""
Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
# Sample list
tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Original List{tuples_list}")
# New value to replace the last element
new_value = 100

# Replace the last value in each tuple directly in the list
tuples_list = [(t[0], t[1], new_value) for t in tuples_list]

# Output the result
print(f"Modified List: {tuples_list}")
