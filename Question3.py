#Question 3: Customer Management System
#1)Use a dictionary structure to store customer information. 
# Assign a unique customer identification (ID) for each customer and associate customer information with this ID. 
# You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.
customers = {}   #empty dictionary to hold all customers record
                 #the key will be the Customer ID 
                 #the value will be another dictionary with customer details

#2)Provide a menu where the user can choose the following actions:
#3)Add New Customer              
def add_customer(customers):
    cid = input("Enter customer ID: ")
    
    if cid in customers:
        print("Customer ID already exists.")
        return

    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    customers[cid] = {
        "name": name,
        "surname": surname,
        "email": email,
        "phone": phone
    }

    print("Customer added successfully.")

#4)Update Customer Info
def update_customer(customers):
    cid = input("Enter customer ID to update: ")
    
    if cid not in customers:  # check if the ID exists
        print("Customer not found.")
        return

    print("Current info:", customers[cid])
    #get new info from the user
    name = input("Enter new name: ")
    surname = input("Enter new surname: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone number: ")

    customers[cid] = {  #update the customer details
        "name": name,
        "surname": surname,
        "email": email,
        "phone": phone
    }

    print("Customer updated.")

#5)Delete a Customer
def delete_customer(customers):
    cid = input("Enter customer ID to delete: ")

    if cid in customers:     #check if the ID exists
        del customers[cid]   #del removes an item from a dictionary
        print("Customer deleted.")
    else:
        print("Customer not found.")

#6)List All Customers
def list_customers(customers):
    if not customers:
        print("No customers in the system.")
        return
    #Loop through all customers and print their details
    for cid, info in customers.items():   #.items() lets us loop through the key and value in the dictionary
        print(f"ID: {cid}, Name: {info['name']} {info['surname']}, Email: {info['email']}, Phone: {info['phone']}")

#7)Menu System (Loop until logout)
def main():
    customers = {}  # main dictionary to store customer data.start with an empty dictionary for customers

    while True: #display the menu
        print("\nCustomer Management System")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. List All Customers")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_customer(customers)
        elif choice == "2":
            update_customer(customers)
        elif choice == "3":
            delete_customer(customers)
        elif choice == "4":
            list_customers(customers)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()