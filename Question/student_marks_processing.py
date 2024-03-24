# The university system reads in a dictionary containing key/value pairs of register number and marks for a list of students. Write a python program to read the marks of a particular student of respective register number in four subjects. Display their result as given below: 
# (i) If the student scores an aggregate greater than 75%, then the grade is distinction. (ii) If aggregate is 60>= and < 75, then the grade is first division.
# (iii) If aggregate is 50 >= and <60, then the grade is second division.
# (iv) If aggregate is 40>= and < 50, then the grade is third division. 
# (v) Else the grade is failed.
# Upon request by a parent on the aggregate of a particular student the code should display the student details, marks, the aggregate and the grade obtained by the student

# Dictionary containing register numbers as keys and marks as values
student_marks = {
    101: [85, 90, 78, 92],
    102: [75, 80, 65, 70],
    103: [55, 60, 58, 62],
    # Add more students and their marks here
}

# Input student's register number
register_number = int(input("Enter the student's register number: "))

# Check if the register number exists in the dictionary
if register_number in student_marks:
    student_marks_list = student_marks[register_number]
    
    # Calculate aggregate
    aggregate = sum(student_marks_list) / len(student_marks_list)
    
    # Determine the grade
    if aggregate > 75:
        grade = "Distinction"
    elif 60 <= aggregate < 75:
        grade = "First Division"
    elif 50 <= aggregate < 60:
        grade = "Second Division"
    elif 40 <= aggregate < 50:
        grade = "Third Division"
    else:
        grade = "Failed"
    
    # Display student details, marks, aggregate, and grade
    print(f"Student Register Number: {register_number}")
    print(f"Marks in Four Subjects: {student_marks_list}")
    print(f"Aggregate: {aggregate:.2f}")
    print(f"Grade: {grade}")
else:
    print("Student not found in the database.")
