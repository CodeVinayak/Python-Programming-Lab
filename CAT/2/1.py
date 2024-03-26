# Write a Python Program using regular expression methods only.
# (i) To remove leading zeros from an IP address. (2 Marks)
# Example IP address= 116.08.094.096 Output = 116.8.94.96
# (ii) To find all three, four, and five character words in a string.(2 Marks)
# (iii)To convert a date of yyyy-mm-dd format to dd-mm-yyyy format.(2 Marks)
# (iv) To search for a word in a sentence and also find the location within the original sentence where the pattern occurs. If the word is not present in the sentence then it should prompt “Not Found” (4 marks)
# Example Sentence : There is no success without hardship
# Search String/word: success Output: Found in the location 12 to 19
# Search String/word: Workship Output: Not Found

import re

#  (i) Remove leading zeros from an IP address
def remove_leading_zeros_from_ip(ip_address):
  pattern = r'\.[0]*'
  return re.sub(pattern, '.', ip_address)
ip_address = '116.08.094.096'
output_ip = remove_leading_zeros_from_ip(ip_address)
print("Output (i):",output_ip)

# (ii) Find all three, four, and five character words in a string
def find_words_of_length(string):
    words = re.findall(r'\b\w{3,5}\b', string)
    return words

# Example usage:
input_string = "This is a sample string with various words of different lengths."
output_words = find_words_of_length(input_string)
print("Output (ii):", output_words)

# (iii) Convert yyyy-mm-dd format to dd-mm-yyyy format
def convert_date_format(date_str):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    replacement = r'\3-\2-\1'
    return re.sub(pattern, replacement, date_string)
# Example usage:
date_string = '2023-11-13'
output_date = convert_date_format(date_string)
print("Output (iii):",output_date)

# (iv) Search for a word in a sentence and find its location
def search_word_in_sentence(sentence, search_word):
    match = re.search(r'\b' + re.escape(search_word) + r'\b', sentence)
    if match:
        return f"Found in the location {match.start()} to {match.end()}"
    else:
        return "Not Found"

# Example usage:
example_sentence = "There is no success without hardship"
search_word_1 = "success"
search_word_2 = "Workship"
output_search_1 = search_word_in_sentence(example_sentence, search_word_1)
output_search_2 = search_word_in_sentence(example_sentence, search_word_2)
print("Output (iv) - Search 1:", output_search_1)
print("Output (iv) - Search 2:", output_search_2)