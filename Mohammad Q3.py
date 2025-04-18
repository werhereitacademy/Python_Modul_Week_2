

# Question 3: Customer Management System
print("Question 3")
customers = {}
def add_customer():
    customer_id = input("Enter a unique Customer ID: ")
    if customer_id in customers:
        print("Customer ID already exists!")
        return
    name = input("Enter Customer's First Name: ")
    surname = input("Enter Customer's Last Name: ")
    email = input("Enter Customer's Email: ")
    phone = input("Enter Customer's Phone Number: ")
    
    customers[customer_id] = {
        'Name': name,
        'Surname': surname,
        'Email': email,
        'Phone': phone
    }
    print(f"Customer {name} {surname} added successfully.")

#Function to update customer information
def update_customer():
    customer_id = input("Enter the Customer ID to update: ")
    if customer_id not in customers:
        print("Customer not found!")
        return
    print("Current Information:")
    print(customers[customer_id])
    
    name = input("Enter new Customer's First Name: ")
    surname = input("Enter new Customer's Last Name: ")
    email = input("Enter new Customer's Email: ")
    phone = input("Enter new Customer's Phone Number: ")

    customers[customer_id] = {
        'Name': name,
        'Surname': surname,
        'Email': email,
        'Phone': phone
    }
    print(f"Customer ID {customer_id} updated successfully.")

# Function to delete a customer
def delete_customer():
    customer_id = input("Enter the Customer ID to delete: ")
    if customer_id in customers:
        del customers[customer_id]
        print(f"Customer ID {customer_id} deleted successfully.")
    else:
        print("Customer not found!")

# Function to list all customers
def list_customers():
    if customers:
        for customer_id, info in customers.items():
            print(f"Customer ID: {customer_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("-" * 20)
    else:
        print("No customers available.")

# Function to exit the system
def check_out():
    print("Logging out. Goodbye!")
    exit()

# Main
def customer_management_system():
    while True:
        print("\nCustomer Management System")
        print("1. Add new customer")
        print("2. Update customer information")
        print("3. Delete customer")
        print("4. List all customers")
        print("5. Check out (Exit)")
        
        choice = input("Please choose an action (1-5): ")
        
        if choice == '1':
            add_customer()
        elif choice == '2':
            update_customer()
        elif choice == '3':
            delete_customer()
        elif choice == '4':
            list_customers()
        elif choice == '5':
            check_out()
        else:
            print("Invalid choice, please try again.")

# Run the customer management system
customer_management_system()


