def calculate_bmi(weight, height):
    bmi = (weight * 703) / (height * height)
    return bmi

# Example usage:
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi_result = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi_result}")
