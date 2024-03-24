def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Input the value of N
N = int(input("Enter the value of N: "))

if N <= 0:
    print("Invalid input. N should be a positive integer.")
else:
    if N % 2 == 1:
        # Odd terms are from the Fibonacci series
        a, b = 1, 1
        for i in range((N + 1) // 2 - 1):
            a, b = b, a + b
        result = a
    else:
        # Even terms are prime numbers
        prime_count = 0
        num = 2
        while True:
            if is_prime(num):
                prime_count += 1
                if prime_count == N // 2:
                    result = num
                    break
            num += 1

    print(f"The {N}th term in the series is: {result}")
