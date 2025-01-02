"""
Question 3: Customer Management System
Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.

2-Provide a menu where the user can choose the following actions:

Add new customers
Updating customer information
Delete customer
List all customers
Check out
3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.

4-When updating customer information, view the current information using the customer ID and save the updated information.

5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.

6-In the process of listing all customers, view the list of existing customers.

7-Repeat the process until the user logs out.
"""
import os
import json

def save_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # print(f"Data was successfully written to file: {file_path}")
    except Exception as e:
        print(f"Error: Data could not be written to file. Details: {e}")
def load_file(file_path):   
    """
    Reads a list from a file in JSON format.
    """
    if not os.path.exists(file_path):
        save_file(file_path, [])
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON format is invalid.")
        return []
    except Exception as e:
        print(f"Error: File could not be read. Details: {e}")
        return []


def add_customer(customers, customers_file):
    """
    Adds a new customer to the customer list.
    """
    customer_id = max(customer["id"] for customer in customers) + 1 if customers else 1
    name = input("Enter customer name: ")
    surname = input("Enter customer surname: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")
    customers.append({"id": customer_id, "name": name, "surname": surname, "email": email, "phone": phone, "address": address})
    save_file(customers_file, customers)
    print(f"Customer {name} {surname} added successfully.")
    return True

def update_customer(customers, customer_id, customers_file):
    """
    Updates the information of an existing customer.
    """
    for customer in customers:
        if customer["id"] == customer_id:
            customer["name"] = input("Enter new name: ")
            customer["surname"] = input("Enter new surname: ")
            customer["email"] = input("Enter new email: ")
            customer["phone"] = input("Enter new phone number: ")
            customer["address"] = input("Enter new address: ")  
            save_file(customers_file, customers)
            print(f"Customer {customer['name']} {customer['surname']} updated successfully.")
            return True
    return False

def delete_customer(customers, customer_id, customers_file):
    """
    Deletes a customer from the customer list.
    """
    for customer in customers:
        if customer["id"] == customer_id:
            customers.remove(customer)
            print(f"Customer {customer['name']} {customer['surname']} deleted successfully.")
            save_file(customers_file, customers)
            return True
    return False

def list_customers(customers):
    """
    Lists all customers in the customer list.
    """
    if not customers:
        print("No customers found.")
    else:
        print("----------".center(130, "-"))
        print("ID".center(10, " "), "Name".center(20, " "), "Surname".center(20, " "), "Email".center(30, " "), "Phone".center(15, " "), "Address".center(35, " "))
        print("----------".center(130, "-"))
        for customer in customers:
            print(str(customer['id']).center(10, " "),customer['name'].center(20," "),customer['surname'].center(20, " "),customer['email'].center(30, " "),customer['phone'].center(15," "),customer['address'].center(30, " "))
            print("----------".center(130, "-"))
        print()

# Main Program
if __name__ == "__main__":
    customers_file = "customers.txt"
    customers = load_file(customers_file)
    incorrectly_entered = False
    exit_confirmation = True
    while exit_confirmation:
        os.system("clear") if os.name == "posix" else os.system("cls")
        list_customers(customers)

        main_menu = ["╔════════════════════════════════════════════════════════════╗ ",
                    "║                      WELCOME TO                            ║ ",
                    "║            The Customer Management System                  ║ ",
                    "╠════════════════════════════════════════════════════════════╣ ",
                    "║               (1) Add new customers                        ║ ",
                    "║               (2) Update customer information              ║ ",
                    "║               (3) Delete customer                          ║ ",
                    "║               (4) List all customers                       ║ ",
                    "║                                                            ║ ",
                    "╠════════════════════════════════════════════════════════════╣ ",
                    "║                  (Q) Quit // Check Out                     ║ ",
                    "╚════════════════════════════════════════════════════════════╝ "
                ]
        for i in main_menu:
            print(i)
        if incorrectly_entered:
            print('\t'.expandtabs(2), "You have entered incorrectly. Please check the menu and make your selection again!")
            incorrectly_entered = False

        print('\t'.expandtabs(2), "Please select the action you wish to perform:", end=" ")
        select_menu = input()

        if select_menu in ["q", "Q"]:
            exit_confirmation = False
        elif select_menu == "1":
            add_customer(customers, customers_file)
        elif select_menu == "2":
            os.system("clear") if os.name == "posix" else os.system("cls")  
            list_customers(customers)
            update_customer_id = input("Enter customer ID to update: ")
            if update_customer_id.isdigit():
                update_customer_id = int(update_customer_id)
                if update_customer(customers, update_customer_id, customers_file):
                    input("Press Enter to continue...")
                else:
                    print("Customer not found.")
                    input("Press Enter to continue...")
            else:
                print("Invalid customer ID. Please enter a valid ID.")
                input("Press Enter to continue...")            
        elif select_menu == "3":
            os.system("clear") if os.name == "posix" else os.system("cls")
            list_customers(customers)
            delete_customer_id = input("Enter customer ID to delete: ")
            if delete_customer_id.isdigit():
                delete_customer_id = int(delete_customer_id)
                if delete_customer(customers, delete_customer_id, customers_file):
                    input("Press Enter to continue...")
                else:
                    print("Invalid customer ID. Please enter a valid ID.")
                    input("Press Enter to continue...")
            else:   
                print("Invalid customer ID. Please enter a valid ID.")
                input("Press Enter to continue...")
        elif select_menu == "4":
            list_customers(customers)
            input("Press Enter to continue...")
        else:
            incorrectly_entered = True
