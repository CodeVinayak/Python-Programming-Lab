print("Name: Vinayak Kumar Singh")
print("Register Number: 23MCA1030")

# Example Input
input_tuple = (123, 155, 261, 147)

# Output File Path
file_path = "output.txt"

# Convert tuple to list and extract first two digits
input_list = list(input_tuple)
extracted_digits_list = [int(str(num)[:2]) for num in input_list]

# Check for non-integer values in the list
for num in input_list:
    if not isinstance(num, int):
        raise ValueError("Input list should contain only integer values.")

# Create a dictionary with digit sums
digit_sum_dict = {}
for num in extracted_digits_list:
    digit_sum = sum(int(digit) for digit in str(num))
    digit_sum_dict[num] = digit_sum

# Sort the dictionary based on keys
sorted_dict = dict(sorted(digit_sum_dict.items()))

# Write to file
with open(file_path, "w") as file:
    file.write("Input Values:\n")
    file.write(f"Tuple: {input_tuple}\n")
    file.write(f"List after extracting first two digits: {extracted_digits_list}\n\n")

    file.write("Output Values:\n")
    file.write(f"Dictionary Values: {digit_sum_dict}\n")
    file.write(f"Sorted Dictionary: {sorted_dict}\n")

print(f"Operation completed. Check '{file_path}' for details.")
