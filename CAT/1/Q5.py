# Given sentence
# sentence = "All our dreams can come true, if we have the courage to pursue them"
sentence = "Do geese see God"

# (i) Remove all vowels from the string
vowels = "AEIOUaeiou"
filtered_sentence = "".join([char for char in sentence if char not in vowels])
print("(i) String with vowels removed:", filtered_sentence)

# (ii) Convert the string to a list of words
word_list = sentence.split()
print("(ii) List of words:", word_list)

# (iii) Remove all whitespace characters from the whole string
no_whitespace_sentence = "".join(sentence.split())
print("(iii) String with whitespace removed:", no_whitespace_sentence)

# (iv) Convert the string to all uppercase and lowercase letters
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
print("(iv) Uppercase:", uppercase_sentence)
print("    Lowercase:", lowercase_sentence)

# (v) Check if a string is a palindrome or not
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if it's the same forwards and backwards

is_palindrome_result = is_palindrome(sentence)
print("(v) Is the string a palindrome?", is_palindrome_result)
