# # Question 3: Customer Management System
# Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic 
# transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, 
# deleting customers and viewing the customer list. Here are the basic steps of the project:
# 1-Use a dictionary structure to store customer information. Assign a UNIQUE customer identification (ID) for each customer and associate customer 
# information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.
# 2-Provide a menu where the user can choose the following actions:
# Add new customers   # Updating customer information    # Delete customer  # List all customers  # Check out
# 3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and 
# add a new customer to the dictionary.
# 4-When updating customer information, view the current information using the customer ID and save the updated information.
# 5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.
# 6-In the process of listing all customers, view the list of existing customers.
# 7-Repeat the process until the user logs out.


import json
import os

if os.path.exists("customers.json"):
    with open("customers.json", "r", encoding="utf-8") as dosya:
        customers = json.load(dosya)
else:
    customers = []

while True:

    choice = str(input("Chooice a menu:  ------------------" \
    "\nNew customer:(N)" \
    "\nUpdate customer:(U) " \
    "\nDelete customer:(D) " \
    "\nList customers:(L) ").upper())

    if choice == "N":

        while True:

            name = input("Give customer name:...")
            surname = input("Give customer surname:...")
            id = len(customers) + 1
            phone = int(input("Give phone number:... "))
            email = input("Give email adres:...   ")
            customer = {
            "name": name,
            "surname": surname,
            "id": id,
            "phone" : phone,
            "email" : email
                    }
            
            customers.append(customer)
            print(f"{['name']} {['surname']} added!")
            print(customers)
            break
        
    elif choice == "U":
        search_name = input("Customer name for update: ")
        for person in customers:
            if person["name"] == search_name:
                print("All information:", person)
                person["name"] = input("New name: ") or person["name"]
                person["phone"] = int(input("New phone: ") or person["phone"])
                person["surname"] = input("surname: ") or person["surname"]
                person["email"] = input("New email: ") or person["email"]
                print("Informations updated:", person)
                print("------------_\n-------")

    elif choice == "D":
            deleted_customer = int(input("Give ID of customer to delete:    "))
            for deleted_customer in customers:
                confirm = input(f"Are you sure you want to delete {deleted_customer['name']} {deleted_customer['surname']}? (y/n): ")
                if confirm.lower() == "y":
                    customers.remove(deleted_customer)
                    print(f"Customer {deleted_customer} deleted successfully!")

                else:
                    print(f"Customer {deleted_customer} not found.")


    elif choice == "L":
        print(customers)
    
    else:
        print(customers)    
        with open("customers.json", "w", encoding="utf-8") as dosya:
            json.dump(customers, dosya, ensure_ascii=False, indent=2)
        print("Data saved. Exiting system.")
        break

        
