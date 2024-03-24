# Input the list of integers
original_list = [12, 34, 56, 78]

# Initialize a new list to store the result
result_list = []

# Iterate through the original list
for i in range(len(original_list)):
    result_list.append(original_list[i])  # Append the current element
    
    # Check if it's not the last element
    if i < len(original_list) - 1:
        average = (original_list[i] + original_list[i + 1]) // 2  # Calculate the average
        result_list.append(average)  # Append the average

# Print the result
print(result_list)
