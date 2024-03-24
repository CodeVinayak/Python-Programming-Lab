def count_divisible_digits(n):
    # Convert the number to a string to iterate through its digits
    str_n = str(n)
    
    count = 0
    for digit_str in str_n:
        digit = int(digit_str)
        if digit != 0 and n % digit == 0:
            count += 1

    return count

# Example usage:
number = 122  # Replace with the desired integer N
result = count_divisible_digits(number)
print(f"The count of digits that exactly divide {number} is: {result}")
