# Get the marks for three subjects as integers
subject1 = int(input("Enter the marks for subject 1: "))
subject2 = int(input("Enter the marks for subject 2: "))
subject3 = int(input("Enter the marks for subject 3: "))

# Check if all subjects are cleared (>=50 in each subject)
if subject1 >= 50 and subject2 >= 50 and subject3 >= 50:
    # Calculate the total percentage
    total_percentage = (subject1 + subject2 + subject3) / 3.0

    # Calculate CGPA
    cgpa = total_percentage / 9.5

    # Determine the allowed credits for the current semester based on CGPA
    if cgpa >= 8.5:
        allowed_credits = 30
    elif 7 <= cgpa < 8.5:
        allowed_credits = 25
    elif 5 <= cgpa < 7:
        allowed_credits = 18
    else:
        # CGPA is less than 5, not allowed for new course registration
        print("Course Registration not allowed. Advised for CGPA improvement.")
        allowed_credits = 0

    # Print the relevant credit value to be registered (if allowed)
    if allowed_credits > 0:
        print(f"Your CGPA is {cgpa:.2f}. You are allowed to register for a total of {allowed_credits} credits in the current semester.")
else:
    print("You have not cleared all subjects (marks < 50 in one or more subjects). Course Registration not allowed.")
