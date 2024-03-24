# Constants
TOTAL_CAPACITY = 5
BUSINESS_CAPACITY = 3
ECONOMY_CAPACITY = 2

# Initialize seat counts for both classes
business_seats_booked = 0
economy_seats_booked = 0

# Function to check seat availability and make a reservation
def reserve_seat(class_choice):
    global business_seats_booked, economy_seats_booked

    if class_choice == "B" and business_seats_booked < BUSINESS_CAPACITY:
        business_seats_booked += 1
        return f"Seat is confirmed in Business Class. Seat number: {business_seats_booked}"
    elif class_choice == "E" and economy_seats_booked < ECONOMY_CAPACITY:
        economy_seats_booked += 1
        return f"Seat is confirmed in Economy Class. Seat number: {economy_seats_booked}"
    else:
        return "Sorry, the requested class is full. Would you like to book in the other class? (Y/N)"

# Main program
while True:
    print("\nWelcome to the Airline Reservation System")
    print("1. Business Class")
    print("2. Economy Class")
    print("3. Exit")

    choice = input("Please enter your choice (1/2/3): ")

    if choice == "1":
        result = reserve_seat("B")
        print(result)
    elif choice == "2":
        result = reserve_seat("E")
        print(result)
    elif choice == "3":
        print("Thank you for using our system.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    # Check if the plane is full
    if business_seats_booked + economy_seats_booked == TOTAL_CAPACITY:
        print("Flight is Full, and the next flight is after 3 hours.")
        break
