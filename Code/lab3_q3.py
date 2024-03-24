def count_and_find_digit(k, d):
    num_str = str(k)
    digit_str = str(d)
    
    if digit_str in num_str:
        print(f"The digit {d} is present in the number {k}.")
    else:
        print(f"The digit {d} is not present in the number {k}.")
        return
    
    occurrences = num_str.count(digit_str)
    print(f"The digit {d} appears {occurrences} times in the number {k}.")

    positions = [i + 1 for i, digit in enumerate(num_str) if digit == digit_str]
    print(f"The digit {d} is found at position(s): {positions}")

print("Register Number = 23MCA1030")
print("Name = Vinayak Kumar Singh")
number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
count_and_find_digit(number, digit)

