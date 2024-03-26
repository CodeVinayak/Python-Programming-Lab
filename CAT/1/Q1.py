# Task 1: Get two numbers from the user and find the sum along with 12% of the first input.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum of the inputs along with 12% of the first input
result = num1 + num2 + (0.12 * num1)
print("Sum of the inputs along with 12% of the first input:", result)

# Task 2: Insert a number into a given list at a specified position.
original_list = [1, 2, 3, 4, 5]
print("Original list:", original_list)

# Get the number to be inserted and the position from the user
insert_number = int(input("Enter the number to be inserted: "))
insert_position = int(input("Enter the position to insert the number: "))

# Insert the number at the specified position
original_list.insert(insert_position, insert_number)
print("Modified list:", original_list)

# Task 3: Display integers between 200 and 250 whose sum of digits is an odd number.
print("Integers between 200 and 250 whose sum of digits is odd:")
for num in range(200, 251):
    # Calculate the sum of digits of the current number
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    if sum_of_digits % 2 != 0:
        print(num)
