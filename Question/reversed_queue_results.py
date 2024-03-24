# Create a list of N Integers. Raise an appropriate built-in exception when a 
# float or string value is entered in the list. Write a Python program using 
# functions to reverse the contents of a queue according to its Size N.
# • If N is even, reverse it in a group of N/2 nodes and store the contents 
# in a list.
# • If N is odd, keep the middle node as it is, reverse the first N/2 
# elements and reverse the last N/2 elements, and store it in another list
# Create a file in an appropriate mode and store the inputs and outputs in a text 
# file. 
# Examples:
# Input: 1,2,3,4,5,6 (N is even)
# Output: 3,2,1,6.5,4
# Input: 1,2,3,4,5,6,7 (N is odd)
# Output: 3,2,1,4,7, 6,5
# Outputs should be displayed for both the even and odd conditions and also 
# stored in a text file

def reverse_queue(queue):
    n = len(queue)

    if n % 2 == 0:
        # N is even, reverse in groups of N/2 nodes
        reversed_queue = queue[:n//2][::-1] + queue[n//2:][::-1]
    else:
        # N is odd, reverse first N/2 elements, keep the middle, reverse last N/2 elements
        reversed_queue = queue[:n//2][::-1] + [queue[n//2]] + queue[n//2+1:][::-1]

    return reversed_queue

try:
    elements = input("Enter space-separated integers for the list: ")
    my_list = []

    for element in elements.split():
        # Raise exception for float or string values
        if not element.isdigit():
            raise ValueError("Only integers are allowed in the list.")
        my_list.append(int(element))

    # Reverse the contents of the queue
    reversed_list = reverse_queue(my_list)

    # Display the output
    print("Input:", my_list)
    print("Output:", reversed_list)

    # Store the inputs and outputs in a text file
    with open("output.txt", "w") as file:
        file.write(f"Input: {my_list}\n")
        file.write(f"Output: {reversed_list}\n")

except ValueError as e:
    print(f"ERROR!\nError: {e}")
