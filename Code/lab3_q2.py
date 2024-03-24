def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm_result = greater
            break
        greater += 1
    return lcm_result

print("Register Number = 23MCA1030")
print("Name = Vinayak Kumar Singh")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 <= 0 or num2 <= 0:
    print("Please enter numbers")
else:
    gcd_result = gcd(num1, num2)
    lcm_result = lcm(num1, num2)

    print(f"The GCD of {num1} and {num2} is: {gcd_result}")
    print(f"The LCM of {num1} and {num2} is: {lcm_result}")