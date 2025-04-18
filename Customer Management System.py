# Question 1: Use a dictionary structure to store customer info with unique ID
customers = {}

# Question 2: Provide a menu for user actions
while True:

    print("\n1. Add new customer")
    print("2. Update customer")
    print("3. Delete customer")
    print("4. List all customers")
    print("5. Check out (exit)")

    choice = input("Choose an option: ")

    # Question 3: Perform action based on user choice — Add customer
    if choice == "1":
        customer_id = input("Enter customer ID: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        customers[customer_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone
        }

        print("Customer added!")

    # Question 4: Update customer info using ID
    elif choice == "2":
        customer_id = input("Enter customer ID to update: ")
        if customer_id in customers:
            print("Current info:", customers[customer_id])
            first_name = input("New first name: ")
            last_name = input("New last name: ")
            email = input("New email: ")
            phone = input("New phone number: ")

            customers[customer_id] = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone
            }
            print("Customer updated.")
        else:
            print("Customer not found.")

    # Question 5: Delete customer by ID
    elif choice == "3":
        customer_id = input("Enter customer ID to Delete: ")
        if customer_id in customers:
            del customers[customer_id]
            print("Customer deleted.")
        else:
            print("Customer not found!")

    # Question 6: List all customers
    elif choice =="4":
        if customers:
            for customer_id, info in customers.items():
                print("ID:", customer_id)
                print("Name:", info["first_name"], info["last_name"])
                print("Email:", info["email"])
                print("Phone:", info["phone"])
                print("-" * 10)
        else:
            print("No customers yet.")

    # Question 7: Repeat until user logs out
    elif choice == "5":
        print("Exiting Customer Management System. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1–5.")