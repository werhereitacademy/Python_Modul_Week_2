#questions 1
#Stap 1: Informatie en cijfers voor 10 studenten opslaan
students = {
    1: {"name": "Ahmet Yilmaz", "midterm": 85, "final": 90, "oral": 80},
    2: {"name": "Mehmet Demir", "midterm": 78, "final": 82, "oral": 88},
    3: {"name": "Ayse Kaya", "midterm": 92, "final": 88, "oral": 91},
    4: {"name": "Zeynep Celik", "midterm": 70, "final": 75, "oral": 68},
    5: {"name": "Ali Kara", "midterm": 88, "final": 85, "oral": 90},
    6: {"name": "Fatma Yildiz", "midterm": 95, "final": 92, "oral": 94},
    7: {"name": "Murat Aydin", "midterm": 60, "final": 65, "oral": 70},
    8: {"name": "Elif Aksoy", "midterm": 82, "final": 78, "oral": 80},
    9: {"name": "Hakan Ozturk", "midterm": 90, "final": 85, "oral": 88},
    10: {"name": "Canan Tas", "midterm": 75, "final": 80, "oral": 78}
}

# Stap 2: Bereken de GPA van elke student en voeg deze toe aan het woordenboek
for student_id, student_info in students.items():
    gpa = (student_info["midterm"] + student_info["final"] + student_info["oral"]) / 3
    students[student_id]["gpa"] = gpa

# Stap 3: Vind de student met de hoogste GPA en druk deze op het scherm af
highest_gpa_student = max(students.items(), key=lambda x: x[1]["gpa"])
print(f"Student with the highest GPA: {highest_gpa_student[1]['name']} with a GPA of {highest_gpa_student[1]['gpa']}")

# Stap 4: Scheid de voornaam van de achternaam van elke student en sla ze op in een aparte tuple en voeg ze toe aan een lijst
name_surname_list = [(info["name"].split()[0], info["name"].split()[1]) for info in students.values()]
print(name_surname_list)

# Stap 5: Sorteer de namen in alfabetische volgorde en druk de gesorteerde lijst op het scherm af
sorted_names = sorted(name_surname_list, key=lambda x: x[0])
print("Sıralanmış isimler:")
for name, surname in sorted_names:
    print(name, surname)

# Stap 6: Houd studenten met een GPA onder de 70 in een cluster (set)
low_gpa_students = {info["name"] for info in students.values() if info["gpa"] < 70}
print("Students with GPA below 70:", low_gpa_students)


#quetions3
customers = {}

'''Met dit menu kunnen we bewerkingen uitvoeren zoals het opslaan van klantgegevens, 
het toevoegen van nieuwe klanten, het bijwerken van klantgegevens, 
het verwijderen van klanten en het bekijken van de klantenlijst.'''

while True: #Een lus die continu blijft draaien wordt gestart
    print("\nCustomer Management System")
    print("1. Add New Customer")
    print("2. Update Customer Information")
    print("3. Delete Customer")
    print("4. List All Customers")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        customer_id = input("Enter Customer ID (numbers only): ")
        if not customer_id.isdigit():  # Controleer of het een getal is
            print("Invalid input! Customer ID must be numbers only.")
            continue
        if customer_id in customers:
            print("This ID already exists. Please choose another ID.")
            continue
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        # Nieuwe klantinformatie wordt aan de woordenlijst toegevoegd
        customers[customer_id] = {"Name": name, "Surname": surname, "Email": email, "Phone": phone}
        print("Customer added successfully!")

    elif choice == "2":
        customer_id = input("Enter the ID of the customer you want to update: ")
        if customer_id not in customers:
            print("No customer found with this ID.")
            continue
        print("Current information: ", customers[customer_id])
        name = input("New Name (leave blank to keep current): ")
        surname = input("New Surname (leave blank to keep current): ")
        email = input("New Email (leave blank to keep current): ")
        phone = input("New Phone Number (leave blank to keep current): ")
        # Update acties
        if name:
            customers[customer_id]["Name"] = name
        if surname:
            customers[customer_id]["Surname"] = surname
        if email:
            customers[customer_id]["Email"] = email
        if phone:
            customers[customer_id]["Phone"] = phone
        print("Customer information updated successfully!")

    elif choice == "3":
        customer_id = input("Enter the ID of the customer you want to delete: ")
        if customer_id in customers:
            del customers[customer_id]
            print("Customer deleted successfully!")
        else:
            print("No customer found with this ID.")

    elif choice == "4":
        if not customers:
            print("No customers found.")
        else:
            print("\nAll Customers:")
            for customer_id, info in customers.items():
                print(f"ID: {customer_id}, Info: {info}")
    # Afsluiten
    elif choice == "5":
        print("Exiting. Have a nice day!")
        break
    # Ongeldige keuze
    else:
        print("Invalid choice. Please select an option between 1-5.")
