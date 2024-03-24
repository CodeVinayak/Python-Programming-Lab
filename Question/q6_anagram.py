# Write a Python program to find all the anagrams in a given list of strings and then group them together: 
# An anagram  is a word or phrase formed by changing the order of the letter in another word or phrase. 
# For example, triangle is an anagrams of integral
# Example: 
# Original list:['restful','forty five','evil','over fifty','vile','fluster','happy']
# Grouped anagrams: [['restful',fluster'],['forty five','over fifty'],['evil','vile']]

# Original list of strings
input = ['restful', 'forty five', 'evil', 'over fifty', 'vile', 'fluster', 'happy']

# Create a dictionary to group anagrams
anagrams = {}

# Iterate through each word in the list
for word in input:
    # Calculate the signature of the word by sorting its characters
    signature = ''.join(sorted(word))

    # Add the word to the list of anagrams
    if signature not in anagrams:
        anagrams[signature] = [word]
    else:
        anagrams[signature].append(word)

# Convert the values (lists of anagrams) of the dictionary to a list
grouped_anagrams = list(anagrams.values())

# Print the result
print("Original list:", input)
print("Grouped anagrams:", grouped_anagrams)
