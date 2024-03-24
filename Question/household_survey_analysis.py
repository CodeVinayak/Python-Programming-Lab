"""
The results of a survey of the households in your township have been made available. Each record contains data for one household family, including a four digit integer identification number, the annual income of the household and the number of members in the family. You may assume that not more than 10 households were surveyed. Write a Python program using structured arrays and Functions to analyse the following.

(a) Calculate the average household income. List the identification number and income of each household whose income exceeds the average.
(b) Determine the percentage of households having income below the average household income and raise an exception when the income is below average.
(c) Sort the survey list based on the number of members in the family. (Largest to Smallest)
"""

import numpy as np

def calculate_average_income(survey_data):
    total_income = np.sum(survey_data['income'])
    average_income = total_income / len(survey_data)
    return average_income

def households_above_average(survey_data, average_income):
    above_average = survey_data[survey_data['income'] > average_income]
    return above_average

def percentage_below_average(survey_data, average_income):
    below_average = survey_data[survey_data['income'] < average_income]
    percentage = (len(below_average) / len(survey_data)) * 100

    if percentage > 0:
        raise Exception(f"{percentage:.2f}% of households have income below the average.")

def sort_by_family_members(survey_data):
    sorted_data = np.sort(survey_data, order='members')[::-1]
    return sorted_data

# Example Usage:
survey_dtype = np.dtype([('id', 'int32'), ('income', 'float64'), ('members', 'int32')])
survey_data = np.array([(1001, 50000, 4), (1002, 60000, 3), (1003, 75000, 5),
                        (1004, 45000, 2), (1005, 80000, 6)], dtype=survey_dtype)

# (a) Calculate the average household income
average_income = calculate_average_income(survey_data)
print(f"Average Household Income: {average_income:.2f}")

# (a) List identification number and income of each household above average
above_average_households = households_above_average(survey_data, average_income)
print("\nHouseholds with Income Above Average:")
for household in above_average_households:
    print(f"ID: {household['id']}, Income: {household['income']}")

# (b) Determine the percentage of households with income below average
try:
    percentage_below_average(survey_data, average_income)
except Exception as e:
    print(f"\nError: {e}")

# (c) Sort the survey list based on the number of members in the family
sorted_survey_data = sort_by_family_members(survey_data)
print("\nSorted Survey Data (Based on Members):")
for household in sorted_survey_data:
    print(f"ID: {household['id']}, Members: {household['members']}")
