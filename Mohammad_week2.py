# Question1: Student Grades Processing
students = {
    1: {'name': 'Ahmet Yilmaz', 'midterm': 85, 'final': 90, 'oral': 78},
    2: {'name': 'Mehmet Demir', 'midterm': 92, 'final': 88, 'oral': 76},
    3: {'name': 'Ayse Kaya', 'midterm': 78, 'final': 89, 'oral': 95},
    4: {'name': 'Zeynep Celik', 'midterm': 50, 'final':60, 'oral': 55},
    5: {'name': 'Ali Kara', 'midterm': 50, 'final': 60, 'oral': 55},
    6: {'name': 'Fatma Yildiz', 'midterm': 88, 'final': 85, 'oral': 90},
    7: {'name': 'Murat Aydin', 'midterm': 72, 'final': 68, 'oral': 74},
    8: {'name': 'Elif Aksoy', 'midterm': 95, 'final': 90, 'oral': 88},
    9: {'name': 'Hakan Öztürk', 'midterm': 45, 'final': 50, 'oral': 55},
    10: {'name': 'Canan Tas', 'midterm': 80, 'final': 75, 'oral': 82}
}

# 1.  GPA 
for student in students.values():
    gpa = (student['midterm'] * 0.3 + student['final'] * 0.5 + student['oral'] * 0.2)
    student['GPA'] = gpa

# 2.  highest GPA
highest_gpa = max(students.items(), key=lambda item: item[1]['GPA'])
print("Student with highest GPA:")
print(f"{highest_gpa[1]['name']} with GPA: {highest_gpa[1]['GPA']}")

# 3. Separate names and surnames 
full_name = []
for student in students.values():
    firstname, lastname = student['name'].split()
    full_name.append((firstname, lastname))

# 4. Sort names alphabetically 
sorted_names = sorted(full_name)
print("\nSorted names:")
for name in sorted_names:
    print(name)

# 5. Store students with GPA < 70 
low_gpa = {student['name'] for student in students.values() if student['GPA'] < 70}
print("\nStudents with GPA below 70:")
print(low_gpa)


# Question 2: Film Library Management System Project
print("Question 2")
import json

# File to store the movie data
MOVIE_FILE = 'movies.json'

# Load movie data from file
def load_movie():
    name = input("Enter movie name: ")
    director = input("Enter director: ")
    year = input("Enter release year: ")
    genre = input("Enter genre: ")
    movie = {
        "name": name,
        "director": director,
        "release_year": year,
        "genre": genre
    }
    return movie

# Save movie data to file
def save_movies(movies):
    with open(MOVIE_FILE, 'w') as f:
        json.dump(movies, f, indent=4)

# Add a new movie
def add_movie(movies):
    name = input("Enter movie name: ").strip()
    if not name:
        print("Movie name cannot be empty.")
        return
    if name in movies:
        print("Movie already exists.")
        return
    director = input("Enter director: ").strip()
    year = input("Enter release year: ").strip()
    while not year.isdigit():
        year = input("Invalid year. Enter a valid release year: ").strip()
    genre = input("Enter genre: ").strip()

    movies[name] = {
        'director': director,
        'year': year,
        'genre': genre
    }
    print("Movie added.")

# Edit movie details
def edit_movie(movies):
    name = input("Enter movie name to edit: ").strip()
    if name not in movies:
        print("Movie not found.")
        return
    print("What do you want to edit?")
    print("1. Director")
    print("2. Release Year")
    print("3. Genre")
    choice = input("Choose (1-3): ").strip()
    if choice == '1':
        movies[name]['director'] = input("Enter new director: ").strip()
    elif choice == '2':
        year = input("Enter new release year: ").strip()
        while not year.isdigit():
            year = input("Invalid year. Enter a valid release year: ").strip()
        movies[name]['year'] = year
    elif choice == '3':
        movies[name]['genre'] = input("Enter new genre: ").strip()
    else:
        print("Invalid choice.")
        return
    print("Movie updated.")

# Delete a movie
def delete_movie(movies):
    name = input("Enter movie name to delete: ").strip()
    if name in movies:
        del movies[name]
        print("Movie deleted.")
    else:
        print("Movie not found.")

# View the movie collection
def view_movies(movies):
    print("1. View all movies")
    print("2. Filter by genre")
    print("3. Filter by release year")
    choice = input("Choose an option: ").strip()
    if choice == '1':
        if not movies:
            print("No movies in the library.")
        else:
            for name, details in movies.items():
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
    elif choice == '2':
        genre = input("Enter genre to filter: ").strip().lower()
        found = False
        for name, details in movies.items():
            if details['genre'].lower() == genre:
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
                found = True
        if not found:
            print("No movies found for that genre.")
    elif choice == '3':
        year = input("Enter release year to filter: ").strip()
        found = False
        for name, details in movies.items():
            if details['year'] == year:
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
                found = True
        if not found:
            print("No movies found for that year.")
    else:
        print("Invalid choice.")

# Main menu
def main():
    movies = load_movies()
    while True:
        print("\n--- Movie Library Menu ---")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View Movies")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            edit_movie(movies)
        elif choice == '3':
            delete_movie(movies)
        elif choice == '4':
            view_movies(movies)
        elif choice == '5':
            save_movies(movies)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


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


