# Write a Python program to implement the following:
# 1.Create a list of flowers containing strings 'rose', 'bougainvillea', 'yucca', 'marigold, 'daylily', and 'lily of the valley'.
# 2.Develop a Boolean expression that evaluates to True if string 'mango' is in list flowers otherwise False.
# 3.Make a list thorny which is the sub list of list flowers consisting of the first three elements of flowers list.
# 4.Create a list poisonous which is the sub list of list flowers consisting of just the last element of list flowers.

# Create a list of flowers
flower_list = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylily', 'lily of the valley']

# Check if 'mango' is in the list of flowers
is_mango_present = 'mango' in flower_list

# Create a list of thorny flowers consisting of the first three elements
thorny_flowers = flower_list[:3]

# Create a list of poisonous flowers consisting of just the last element
poisonous_flowers = [flower_list[-1]]

# Print the results
print("List of flowers:", flower_list)
print("Is 'mango' in the list of flowers?", is_mango_present)
print("List of thorny flowers:", thorny_flowers)
print("List of poisonous flowers:", poisonous_flowers)