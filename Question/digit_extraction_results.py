# Create a tuple containing N integers. Write a Python program using functions 
# to convert it into a list and then extract the first two digits of each number in the 
# list and store it in another list. The input list must contain only integer values. 
# Raise an appropriate built-in exception when a float or string value is entered in 
# the list. Use the output list to create a dictionary that will have all these elements 
# which contain the elements as keys and the value is the sum of the digits of each 
# element. Sort the dictionary based on the key values.
# Create a file in an appropriate mode and store the inputs and outputs in a text file.
# Example:
# Input: 123,155,261,147
# Output: 12,15,26,14
# Dictionary Values: {12:3,15:6,26:8,14:5}
# Sorted Dictionary: {12:3, 14:5,15:6,26:8}

def convert_to_list_and_extract_digits(input_tuple):
    input_list = list(input_tuple)
    extracted_digits_list = []

    for num in input_list:
        if not isinstance(num, int):
            raise ValueError("Only integers are allowed in the list.")
        extracted_digits_list.append(int(str(num)[:2]))

    return extracted_digits_list

def calculate_digit_sum(dictionary_values):
    result_dict = {}
    for num in dictionary_values:
        digit_sum = sum(int(digit) for digit in str(num))
        result_dict[num] = digit_sum
    return result_dict

try:
    input_str = input("Enter comma-separated integers for the tuple: ")
    input_tuple = tuple(map(int, input_str.split(',')))

    # Convert to list and extract first two digits
    extracted_digits_list = convert_to_list_and_extract_digits(input_tuple)

    # Create dictionary with elements and sum of digits
    result_dict_values = calculate_digit_sum(extracted_digits_list)

    # Sort the dictionary based on key values
    sorted_result_dict = dict(sorted(result_dict_values.items()))

    # Display the output
    print("Input:", input_tuple)
    print("Output:", extracted_digits_list)
    print("Dictionary Values:", result_dict_values)
    print("Sorted Dictionary:", sorted_result_dict)

    # Store the inputs and outputs in a text file
    with open("output.txt", "w") as file:
        file.write(f"Input: {input_tuple}\n")
        file.write(f"Output: {extracted_digits_list}\n")
        file.write(f"Dictionary Values: {result_dict_values}\n")
        file.write(f"Sorted Dictionary: {sorted_result_dict}\n")

except ValueError as e:
    print(f"Error: {e}")
