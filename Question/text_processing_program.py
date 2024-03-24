import re

# Input list
input_list = ["example (.com)", "w3resource", "github2 (.com)", "stack1overflow2 (.com)"]

# (i) Remove the parenthesized segment from the string
result_i = [re.sub(r'\s*\(.*\)', '', item) for item in input_list]

# (ii) Remove the digits/numbers from the string
result_ii = [re.sub(r'\d', '', item) for item in result_i]

# (iii) Create a dictionary with words and their lengths
word_lengths = {word: len(word) for word in result_ii}

# Print results
print("Result (i):", result_i)
print("Result (ii):", result_ii)
print("Result (iii):", word_lengths)