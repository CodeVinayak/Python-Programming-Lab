# Define a function to check if a number is a perfect square
def is_perfect_square(num):
    sqrt = int(num**0.5)
    return sqrt * sqrt == num

# Define a function to generate the PIN number
def generate_pin(birth_year):
    # Convert the 4-digit birth year to individual digits
    R, S, T, U = map(int, str(birth_year))

    # Apply the constraints
    # Constraint 1: Check if U is odd and update if needed
    if U % 2 == 0:
        U += 1

    # Constraint 2: Check if T is a multiple of 4 and update if needed
    if T % 4 != 0:
        U += T
        U %= 10  # Discard carry digit if any

    # Constraint 3: Check if RS forms a perfect square and update if needed
    RS = R * 10 + S
    if not is_perfect_square(RS):
        RS = 16  # The least two-digit perfect square number

    # Combine the updated digits to form the PIN
    new_pin = RS * 100 + T * 10 + U

    return new_pin

# Input the 4-digit birth year from the user
birth_year = int(input("Enter your 4-digit birth year: "))

# Generate and print the PIN number
pin_number = generate_pin(birth_year)
print("Your PIN number is:", pin_number)
