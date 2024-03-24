# a. Your company has got email messages which has to be validated. Write a regular expression that matches all lines in a text file which contains a string that starts with a valid date in YYYY-MM-DD format, followed by a space and valid time in HH: MM: SS format, and ends with one or more sentences that starts with an uppercase letter and ends with a period (.), exclamation mark (!) or question mark (?). The sentences alone should be enclosed in square brackets. 
# For example:
# text='2023-05-06 12:34:56 [Important message]'
# b.Write a function using Python that takes a sentence as an input parameter from the user where each word in the sentence is separated by a space with duplicate words in it. The function should replace each blank with a hyphen and also removing the duplicates and returning the modified sentence.
import re

# Sample text
text = '2023-05-06 12:34:56 [Important message]'
text2 = '2023-05-06 12:34:56'

# Regular expression pattern
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(?:[A-Z][^.!?]+[.!?])+]'
pattern2 = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

# Check if the text matches the pattern
# if re.match(pattern, text):
if re.match(pattern2, text2):
    print("Valid line: ", text)
else:
    print("Invalid line: ", text)

def modify_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Remove duplicates by converting the list to a set and then back to a list
    unique_words = list(set(words))

    # Join the unique words with hyphens
    modified_sentence = '-'.join(unique_words)

    return modified_sentence

# Input sentence from the user
user_sentence = input("Enter a sentence with duplicate words separated by spaces: ")

# Call the function and print the modified sentence
result = modify_sentence(user_sentence)
print("Modified sentence:", result)
