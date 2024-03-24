# Custom Exception classes
class InvalidCardNumberException(Exception):
    pass

class InvalidNameFormatException(Exception):
    pass

class InvalidCvvException(Exception):
    pass

def validate_credit_card(card_number, name, validity_date, cvv):
    try:
        # Validate card number length
        if len(card_number) != 16:
            raise InvalidCardNumberException("Invalid Card Number")

        # Validate name format
        name_parts = name.split()
        if len(name_parts) != 2 or not all(part.isalpha() for part in name_parts):
            raise InvalidNameFormatException("Invalid Name Format")

        # Validate CVV format
        if len(cvv) != 3 or cvv[0] == '0':
            raise InvalidCvvException("Invalid CVV Format")

        # If all checks pass, the data is valid
        print("Credit Card Details are Valid.")
    
    except InvalidCardNumberException as e:
        print(e)
    except InvalidNameFormatException as e:
        print(e)
    except InvalidCvvException as e:
        print(e)

# Input credit card details
card_number = input("Enter Credit Card Number: ")
name = input("Enter Name (Last Name First Name): ")
validity_date = input("Enter Validity Date (MM/YY Format): ")
cvv = input("Enter CVV Number: ")

# Call the validation function
validate_credit_card(card_number, name, validity_date, cvv)
