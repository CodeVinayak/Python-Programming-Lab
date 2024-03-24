import sqlite3

# Function to create the customer schema
def create_customer_schema(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID INTEGER PRIMARY KEY,
            CustomerName VARCHAR(255),
            AccountNo INTEGER,
            AccountType VARCHAR(20),
            AccountBalance INTEGER
        )
    ''')
    conn.commit()

# Function to insert new customer records
def insert_customer_records(conn, records):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO Customer (CustomerName, AccountNo, AccountType, AccountBalance)
        VALUES (?, ?, ?, ?)
    ''', records)
    conn.commit()

# Function to add Rs.500 to customers with savings account and minimum balance > Rs.90000
def update_customer_balances(conn):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Customer
        SET AccountBalance = AccountBalance + 500
        WHERE AccountType = 'Savings' AND AccountBalance > 90000
    ''')
    conn.commit()

# Function to delete customer record by name
def delete_customer_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Customer
        WHERE CustomerName = ?
    ''', (name,))
    conn.commit()

# Function to display all customer information
def display_all_customers(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customer')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Main program
if __name__ == "__main__":
    # Connect to SQLite database (create a new one if not exists)
    conn = sqlite3.connect('customer_database.db')

    # Create customer schema
    create_customer_schema(conn)

    # Insert new customer records
    customer_records = [
        ('Alice', 123456, 'Savings', 95000),
        ('Bob', 789012, 'Current', 75000),
        ('Rohan', 345678, 'Savings', 100000)
    ]
    insert_customer_records(conn, customer_records)

    # Add Rs.500 to customers with savings account and minimum balance > Rs.90000
    update_customer_balances(conn)

    # Delete the customer record whose name is "Rohan"
    delete_customer_by_name(conn, 'Rohan')

    # Display all customer information
    print("All Customer Information:")
    display_all_customers(conn)

    # Close the database connection
    conn.close()
