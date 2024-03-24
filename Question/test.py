# Create the dictionary
my_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white'}

# (1) Convert the dictionary into a list of tuples
tuple_list = list(my_dict.items())
print("Converted Dictionary to List of Tuples:")
print(tuple_list)

# (2) Find the length of values in the dictionary and create a dictionary
value_lengths = {value: len(value) for value in my_dict.values()}
print("\nLength of Values in the Dictionary:")
print(value_lengths)

# (3) Search for a key-value pair in the dictionary
key_search = 3
value_search = 'black'
pair_exists = key_search in my_dict and my_dict[key_search] == value_search

# Print the results
print("\nSearch for Key-Value Pair:")
if pair_exists:
    print("The key-value pair ({}, '{}') exists in the dictionary.".format(key_search, value_search))
else:
    print("The key-value pair ({}, '{}') does not exist in the dictionary.".format(key_search, value_search))
