# Write a Python Program that creates an array of elements and handles various exceptions.
# including ZeroDivisionError, IndexError, ValueError, TypeError, and AttributeError. The
# program demonstrates how to handle these exceptions. (2 Marks Each)
def handle_exceptions():
    try:
        # Creating an array of elements
        elements = [1, 2, 3, 4, 5]

        # Handling ZeroDivisionError
        result = 10 / 0

        # Handling IndexError
        index_error = elements[10]

        # Handling ValueError
        value = int("abc")

        # Handling TypeError
        result = "5" + 3

        # Handling AttributeError
        attribute_error = elements.non_existent_method()

    except ZeroDivisionError as zd_error:
        print(f"Caught ZeroDivisionError: {zd_error}")

    except IndexError as index_error:
        print(f"Caught IndexError: {index_error}")

    except ValueError as value_error:
        print(f"Caught ValueError: {value_error}")

    except TypeError as type_error:
        print(f"Caught TypeError: {type_error}")

    except AttributeError as attr_error:
        print(f"Caught AttributeError: {attr_error}")

    else:
        print("No exceptions occurred.")

    finally:
        print("Finally block executed.")

# Call the function to demonstrate exception handling
handle_exceptions()
