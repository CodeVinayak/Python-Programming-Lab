# Write a python program to insert a number in a list of sorted numbers without using built in function.

def insert_into_sorted_list(sorted_list, number_to_insert):
    index = 0

    # Find the correct position to insert the number
    while index < len(sorted_list) and sorted_list[index] < number_to_insert:
        index += 1

    # Insert the number at the correct position
    sorted_list.insert(index, number_to_insert)

# Example Usage:
sorted_numbers = [10, 20, 30, 40, 50]
number_to_insert = 25

print(f"Original Sorted List: {sorted_numbers}")
insert_into_sorted_list(sorted_numbers, number_to_insert)
print(f"List after Inserting {number_to_insert}: {sorted_numbers}")
