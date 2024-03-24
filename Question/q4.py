# Write Python Programs to
# (1) Create a dictonary of elements as shown below.
#  {1: 'red', 2: 'green', 3: 'black', 4: 'white'} and Convert the given dictionary into a list of tuples 
# (ii) Find the length of value of each element in the above created dictionary 
# Example Output: {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# (ii) Search for a given key value pair from the dictionary and display if it exists or not in the dictionary.


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
    print(f"The key-value pair ({key_search}, '{value_search}') exists in the dictionary.")
else:
    print(f"The key-value pair ({key_search}, '{value_search}') does not exist in the dictionary.")
