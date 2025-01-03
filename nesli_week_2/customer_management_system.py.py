#Customer Management System
# Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

# 1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.
# 2-Provide a menu where the user can choose the following actions:

# * Add new customers
# * Updating customer information
# * Delete customer
# * List all customers
# * Check out

# 3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.
# 4-When updating customer information, view the current information using the customer ID and save the updated information.
# 5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.
# 6-In the process of listing all customers, view the list of existing customers.
# 7-Repeat the process until the user logs out.

def customer_management_system():
    # Dictionary to store customer information
    ##glossary/dictionary structure to store customer information
    customers = {}

    while True:
        print("\nCustomer Management System")
        print("1. Add New Customer")
        print("2. List All Customers")
        print("3. Delete Customer")
        print("4. Update Customer Information")
        print("5. Exit")

        selected = input("Select the operation you want to perform (1-5): ").strip()

        if selected == "1":
            id = input("Customer ID: ").strip()
            if not id:
                print("ID cannot be empty. Please try again.")
                continue
            if id in customers:
                print("This ID is already in use. Please use a different ID.")
                continue

            name = input("Customer Name: ").strip()
            surname = input("Customer Surname: ").strip()
            e_mail = input("Customer Email Address: ").strip()
            phone = input("Customer Phone Number: ").strip()

            customers[id] = {
                "name": name,
                "surname": surname,
                "e_mail": e_mail,
                "phone": phone
            }
            print(f"Customer {name} {surname} added successfully.")

        elif selected == "2":
            if not customers:
                print("There are no customer records.")
            else:
                print("\nRegistered Customers:")
                for id, information in customers.items():
                    print(f"ID: {id}, Name: {information['name']}, Surname: {information['surname']}, "
                          f"Email: {information['e_mail']}, Phone: {information['phone']}")

        elif selected == "3":
            id = input("The customer ID you want to delete: ").strip()
            if id in customers:
                del customers[id]
                print("Customer successfully deleted.")
            else:
                print("No customer with this ID was found.")

        elif selected == "4":
            id = input("Enter the Customer ID you want to update: ").strip()
            if id in customers:
                print(f"Current Information: Name: {customers[id]['name']}, Surname: {customers[id]['surname']}, "
                      f"Email: {customers[id]['e_mail']}, Phone: {customers[id]['phone']}")
                new_name = input("Enter a new name: ").strip()
                new_surname = input("Enter a new surname: ").strip()
                new_e_mail = input("Enter a new email address: ").strip()
                new_phone = input("Enter a new phone number: ").strip()

                customers[id] = {
                    "name": new_name,
                    "surname": new_surname,
                    "e_mail": new_e_mail,
                    "phone": new_phone
                }

                print("Customer information updated successfully.")
            else:
                print("No customer with this ID found.")

        elif selected == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

# Call the function to start the system
customer_management_system()
