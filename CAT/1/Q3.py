# Create a list of tuples with student details
student_details = [("Anish", 189.4, 73.5), ("Raj", 175, 60.3), ("Sara", 160, 55.0),("Aman",170,99.5)]

# Sort the list by height (second element in each tuple)
sorted_students = sorted(student_details, key=lambda x: x[1])

print("Students sorted by height:")
for student in sorted_students:
    name, height, weight = student
    print(f"Name: {name}, Height: {height} cm, Weight: {weight} kg")

print("\nStudents who are overweight:")
for student in student_details:
    name, height, weight = student
    # Convert height from cm to meters
    height_meter = height / 100
    # Calculate BMI
    bmi = weight / (height_meter ** 2)
    
    if bmi >= 25.0:
        print(f"Name is {name} and Weight is {weight} kg")
