# Write a Python Code to automate the following information for an airline Company.
# Total capacity of the aeroplane is 150 seats.
# There are two categories of classes namely Business class and the Economy class.
# The user should enter the choice of the classes. The system should allocate the seat in the requested class if it is available. If not, the user should be ask the option of allocating seat in the other class.
# Seats are numbered sequentially in each class. If the seats are not available in any of the class, the system should display a message "Flight is Full and the next flight is after 3 hours".
# After making a reservation the system should also display "Seat is confirmed" along with the seat number and the class.

# Constants
Total_Capactiy = 150
Business_Capactiy = 30
Economy_Capactiy = 120

# Initialize seat counts for both classes
b_seats = 0
e_seats = 0

# Main program
while True:
    print("\nWelcome to the Airline Reservation System")
    print("1. Business Class")
    print("2. Economy Class")
    print("3. Exit")

    choice = input("Please enter your choice (1/2/3): ")

    if choice == "1" and b_seats < Business_Capactiy:
        b_seats += 1
        print("Seat is confirmed in Business Class")
        print(f"Seat number is : {b_seats}")

    elif choice == "2" and e_seats < Economy_Capactiy:
        e_seats += 1
        print("Seat is confirmed in Economy Class")
        print(f"Seat number: {e_seats}")

    elif choice == "3":
        print("Thank you for using our system.")
        break

    else:
        print("Sorry, the requested class is full.")
        print("Would you like to book in the other class?") 

    if b_seats + e_seats == Total_Capactiy:
        print("Flight is Full, and the next flight is after 3 hours.")
        break
