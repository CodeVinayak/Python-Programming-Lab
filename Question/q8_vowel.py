# Write a Python program that accepts input as a sentence (String) as shown and does the following tasks and displays the output.
# a)Check if the first and last character in the string is a vowel and find the longest word and its length from the input string.
# b)Check whether the first word ends with a vowel and the second word begins with a vowel. If the program meets the condition, return true, otherwise false. Only one space is allowed between the words.
# Sample Data:
# ("These exercises can be used for practice.") False for a) and True for b)
# ("I use these books in my classroom for reference.")-> True for both a and b)

# Input sentence
input_sentence = input("Enter a sentence: ")

# Define a function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in 'aeiou'

# Function to find the longest word and its length
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    max_length = 0

    for word in words:
        # Remove punctuation
        clean_word = ''.join(char for char in word if char.isalnum())
        if len(clean_word) > max_length:
            max_length = len(clean_word)
            longest_word = clean_word

    return longest_word, max_length

# Check conditions for part (a)
first_char = input_sentence[0]
last_char = input_sentence[-1]

if is_vowel(first_char) and is_vowel(last_char):
    longest_word, word_length = find_longest_word(input_sentence)
    print(f'a) True (Longest word: "{longest_word}", Length: {word_length})')
else:
    print('a) False')

# Check conditions for part (b)
words = input_sentence.split()

if len(words) >= 2:
    first_word = words[0]
    second_word = words[1]

    if is_vowel(first_word[-1]) and is_vowel(second_word[0]):
        print('b) True')
    else:
        print('b) False')
else:
    print('b) False')
