# Create a dictionary which contains the following keys (Name, Score, Attempts, Qualify) and Values for five students (name of students, score (marks of student), Attempts to clear(1,2 or 3). and Qualify(yes or No) 
# Write a Python Program importing appropriate packages to
# Create and display a DataFrame from the dictionary create
# Summary of the basic information about this DataFrame and its data
# Select the 'name' and 'score' columns from the following DataFrame.
# Select the rows where the number of attempts in the examination is greater than 2.


import pandas as pd

# Create a dictionary with student data
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 92, 78, 65, 88],
    'Attempts': [1, 3, 2, 3, 1],
    'Qualify': ['Yes', 'Yes', 'No', 'No', 'Yes']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(student_data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Summary of basic information about the DataFrame and its data
print("\nSummary of Basic Information:")
print(df.info())

# Select the 'Name' and 'Score' columns
selected_columns = df[['Name', 'Score']]
print("\nSelected 'Name' and 'Score' columns:")
print(selected_columns)

# Select the rows where the number of attempts is greater than 2
attempts_greater_than_2 = df[df['Attempts'] > 2]
print("\nRows where Attempts > 2:")
print(attempts_greater_than_2)
