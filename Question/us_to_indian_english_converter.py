import re

def us_to_indian_english(text):
    # Replace 'color' with 'colour'
    text = re.sub(r'\bColor\b', 'Colour', text)

    # Replace 'z' with 's' when it appears as 'z' or 'Z' in words
    text = re.sub(r'\bz', 's', text)
    text = re.sub(r'\bZ', 'S', text)

    # Replace 'z' with 's' at the end of words (e.g., 'synchronize' to 'synchronise')
    text = re.sub(r'z\b', 's', text)
    text = re.sub(r'Z\b', 'S', text)

    return text

# Load the US English scientific report (replace with your actual text)
us_english_report = """
This is a scientific report in US English. It contains words like color and synchronize with 'z'. 
"""

# Convert to Indian English
indian_english_report = us_to_indian_english(us_english_report)

# Print the converted report
print(indian_english_report)

# # Take input from the user
# us_english_report = input("Enter the US English scientific report: ")

# # Convert to Indian English
# indian_english_report = us_to_indian_english(us_english_report)

# # Print the converted report
# print("Converted Indian English report:")
# print(indian_english_report)