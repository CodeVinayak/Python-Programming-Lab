# Write a Python Program to create a text file “Myhobby.txt” which contains a few sentences of your favourite hobby. The file should always have the option of adding new lines to it. Perform the following operations with the file (3 marks)
# (i) Read a word from the user as input and count the number of occurrences of that, particular word in the text file “Myhobby.txt” (5 Marks) .
# (ii) Handle the exceptions when you attempt to read or write a file that doesn't exist in the specified location. (2 Marks)

def create_file():
    try:
        with open("Myhobby.txt", "w") as file:
            # Create the file and add initial content
            file.write("My favorite hobby is reading.\n")
            file.write("I enjoy exploring new books and genres.\n")
            file.write("Reading helps me relax and expand my knowledge.\n")
        print("File 'Myhobby.txt' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_line_to_file():
    try:
        with open("Myhobby.txt", "a") as file:
            # Allow the user to add a new line to the file
            new_line = input("Enter a new line to add to the file: ")
            file.write(new_line + "\n")
        print("Line added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_word_occurrences(word):
    try:
        with open("Myhobby.txt", "r") as file:
            content = file.read()
            # Count the occurrences of the specified word
            word_count = content.lower().split().count(word.lower())
        print(f"The word '{word}' occurs {word_count} times in the file.")
    except FileNotFoundError:
        print("The file 'Myhobby.txt' does not exist. Please create the file first.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create the file
create_file()

# Add a new line to the file
add_line_to_file()

# Read a word from the user and count its occurrences in the file
user_input_word = input("Enter a word to count its occurrences in the file: ")
count_word_occurrences(user_input_word)
