print("Name: Vinayak Kumar Singh")
print("Register Number: 23MCA1030")

L1 = [3, 5, 2, 4, 6]
L2 = [1, 2, 7, 9, 12]
print(f"Starting value of L1 is {L1}")
print(f"Starting value of L2 is {L2}")

def insert_largest(L1, L2):
    if len(L1) == 0:
        return
    largest = max(L1)
    if largest in L2:
        raise ValueError("Duplicate found in L2")
    L2.append(largest)
    L2.sort()
    L1.remove(largest)

file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        file.write("Input Values:\n")
        file.write(f"L1: {L1}\n")
        file.write(f"L2: {L2}\n\n")

        while len(L1) > 0:
            try:
                insert_largest(L1, L2)
                file.write(f"Now L1: {L1}\n")
                file.write(f"Now L2: {L2}\n")
            except ValueError as e:
                file.write(f"Exception: {e}\n")
                break  # Exit the loop if a duplicate is found

except OSError as e:
    print(f"Error: {e}")

print(f"Operation completed. Check '{file_path}' for details.")
