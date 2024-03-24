def calculate_curtain_material(width, height, material_width=140, price_per_meter=5):
    # Calculate the total area of the curtains needed
    total_area = width * height

    # Calculate the required length of material in meters
    required_length = total_area / material_width

    # Calculate the cost of the material
    material_cost = required_length * price_per_meter

    return required_length, material_cost

# Example usage:
window_width = float(input("Enter the width of the window in cm: "))
window_height = float(input("Enter the height of the window in cm: "))

material_length, cost = calculate_curtain_material(window_width, window_height)

print(f"To make curtains for the window, you need {material_length:.2f} meters of material.")
print(f"The estimated cost of the material is {cost:.2f} units of rupees.")
