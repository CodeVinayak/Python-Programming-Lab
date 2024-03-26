# Create a dictionary of faculty and the courses they handle
faculty_courses = {
    5001: ["SWE1001", "CSE1001", "CSE3002"],
    5023: ["PMCA601L", "CSE1001"],
    5045: ["SWE2001", "CSE3001", "PMCA301"],
}

# Task 1: List the employee IDs of faculty handling more than two subjects
faculty_more_than_two_subjects = [emp_id for emp_id, courses in faculty_courses.items() if len(courses) > 2]
print("Faculty handling more than two subjects:", faculty_more_than_two_subjects)

# Task 2: List the employee IDs of faculties handling CSE1001
faculty_handling_CSE1001 = [emp_id for emp_id, courses in faculty_courses.items() if "CSE1001" in courses]
print("Faculty handling CSE1001:", faculty_handling_CSE1001)
