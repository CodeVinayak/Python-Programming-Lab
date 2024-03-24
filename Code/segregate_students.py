def segregate_students(cgpa):
    if cgpa <= 10 and cgpa > 9:
        return "Outstanding"
    elif cgpa <= 9 and cgpa > 8:
        return "Excellent"
    elif cgpa <= 8 and cgpa > 7:
        return "Good"
    elif cgpa <= 7 and cgpa > 6:
        return "Average"
    elif cgpa <= 6 and cgpa > 5:
        return "Better"
    elif cgpa < 5:
        return "Poor"
    else:
        return "Invalid CGPA"

# Example usage:
student_cgpa = 8.5  # Replace with the actual CGPA of the student
result = segregate_students(student_cgpa)
print(f"The student score is {student_cgpa} which is a {result}")
