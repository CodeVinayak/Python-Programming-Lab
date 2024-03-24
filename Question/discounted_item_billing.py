# Develop a python program using conditional statements to find out discounted price for an item depending upon its category such as (a) seasonal-food-items with expiry date within in a month at 10% and otherwise 5% 
# (b) seasonal-clothes with sizes extra-small or extra-extra-large at 20% and otherwise 5%. The program should display the bill consisting of customer details (id, name and number), list of items bought with their respective item-code and product details. The original cost and discounted cost of the products to be included in the bill.
# Input customer details 

customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")
customer_number = input("Enter customer phone number: ")

# Initialize the bill
bill = {
    "Customer ID": customer_id,
    "Customer Name": customer_name,
    "Phone Number": customer_number,
    "Items": []
}

# Input and process item details
num_items = int(input("Enter the number of items bought: "))
for i in range(num_items):
    item_code = input(f"Enter item code for item {i + 1}: ")
    item_name = input(f"Enter item name for item {i + 1}: ")
    item_category = input(f"Enter item category for item {i + 1} (seasonal-food-items/seasonal-clothes/other): ")
    item_price = float(input(f"Enter item price for item {i + 1}: "))

    # Calculate discounted price based on category
    if item_category == "seasonal-food-items":
        expiry_within_month = input("Is the expiry date within a month? (yes/no): ").lower()
        if expiry_within_month == "yes":
            discounted_price = item_price * 0.90  # 10% discount
        else:
            discounted_price = item_price * 0.95  # 5% discount
    elif item_category == "seasonal-clothes":
        size = input("Enter the size (XS/XXL/other): ").lower()
        if size in ["xs", "xxl"]:
            discounted_price = item_price * 0.80  # 20% discount
        else:
            discounted_price = item_price * 0.95  # 5% discount
    else:
        discounted_price = item_price  # No discount for other categories

    # Add item details to the bill
    bill["Items"].append({
        "Item Code": item_code,
        "Item Name": item_name,
        "Item Category": item_category,
        "Original Price": item_price,
        "Discounted Price": discounted_price
    })

# Display the bill
print("\nCustomer Bill:")
print(f"Customer ID: {bill['Customer ID']}")
print(f"Customer Name: {bill['Customer Name']}")
print(f"Phone Number: {bill['Phone Number']}")
print("\nItems Bought:")
for item in bill["Items"]:
    print(f"Item Code: {item['Item Code']}")
    print(f"Item Name: {item['Item Name']}")
    print(f"Item Category: {item['Item Category']}")
    print(f"Original Price: {item['Original Price']:.2f}")
    print(f"Discounted Price: {item['Discounted Price']:.2f}\n")
