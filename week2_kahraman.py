#QUESTION 1

students = {} #DEFINE A DICT

for i in range(1, 11):    #GET STUDENTS INFORMATIONS
    print(f"\n{i}. please write the informatin of student:")
    name = input("name: ")
    surname = input("surname: ")
    
    midterm = int(input("midterm (0-100): "))
    while (midterm < 0 or midterm > 100) :
        print("you have to write a number that between 0 to 100. write again:")
        midterm = int(input("midterm (0-100): "))

    final = int(input("Final (0-100): "))
    while (final < 0 or final > 100) :
        print("Final has to be between 0-100 . write again: ")
        final = int(input("Final (0-100): "))

    oral = int(input("oral degree (0-100): "))
    while (oral < 0 or oral > 100) :
        print("oral degree has to be between 0-100. write again: ")
        oral = int(input("oral degree (0-100): "))

    average = (midterm * 0.3) + (final * 0.5) + (oral * 0.2)
    students[i] = {
        'name': name,
        'surname': surname,
        'grades': {'midterm': midterm, 'Final': final, 'oral degree': oral},
        'average': round(average, 2)
    }


highest_gpa = 0  #highest degree
highest_student = ""
for i in students:
    if students[i]['average'] > highest_gpa:
        highest_gpa = students[i]['average']
        highest_student = students[i]['name'] + " " + students[i]['surname']
    elif students[i]['average'] == highest_gpa:
        highest_student.append(students[i]['name']+' '+students[i]['surname'])

print(f"\nthe student that has the highest degree: {highest_student} (average: {highest_gpa})")


name_list = [] #separate as a tuple
for i in students:
    name_list.append((students[i]['name'], students[i]['surname']))
print("\nname list:", name_list)


names = []     # order
for i in students:
    names.append(students[i]['name'])
order = sorted(names)
print("\n order the names:", order)


the_students_have_less_average = set()   #the student has an average that below 70
for i in students:
    if students[i]['average'] < 70:
        the_students_have_less_average.add(students[i]['name'] + " " + students[i]['surname'])
print("\nthe students have an average that below 70:", the_students_have_less_average)



#QUESTION 2

import json


movie_collection = []                                                   #save the movies

def save_data():
    file = open("movie_collection.json", 'w')  
    json.dump(movie_collection, file)  
    file.close() 


def load_data():                                                          #load the movies data
    try:
        file = open("movie_collection.json", 'r') 
        data = json.load(file) 
        file.close()  
        return data
    except FileNotFoundError:
        return []  


def add_movie():                                                             #add a movie
    title = input("name of movie: ")
    director = input("director: ")
    year = input("year: ")
    genre = input("genre: ")
    
    movie = {
        'title': title,
        'director': director,
        'year': year,
        'genre': genre
    }
    movie_collection.append(movie)
    print(f"the {title} added in movie collection.\n")
    save_data()


def delete_movie():                                                             #deleting
    title = input("The name of the movie you want to delete: ")
    for movie in movie_collection:
        if movie['title'].lower() == title.lower():
            movie_collection.remove(movie)
            print(f"{title} is deleted.\n")
            save_data()
            return
    print(f"{title} is not found.\n")


def edit_movie():                                                                 #fixing
    title = input("The name of the movie you want to edit: ")
    for movie in movie_collection:
        if movie['title'].lower() == title.lower():
            print(f"Film: {movie['title']}")
            movie['director'] = input("new director: ")
            movie['year'] = input("new year: ")
            movie['genre'] = input("new genre: ")
            print(f"{title} is edited.\n")
            save_data()
            return
    print(f"{title} is not found.\n")


def look_at_collection():                                     #looking at the collection
    if not movie_collection:
        print("there is no any movies in your collection.\n")
        return
    print("\n📖 THE MOVIE COLLECTION:")
    for movie in movie_collection:
        print(f"Movie Name: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}, Genre: {movie['genre']}")
    print()

def ana_menu():                                                          #MENU
    print("\n" + "=" * 40)
    print("       📚 MY MOVIE COLLECTION")
    print("=" * 40)
    print("1️⃣  ADD A MOVIE")
    print("2️⃣  DELETE A MOVIE")
    print("3️⃣  LOOK AT THE MOVIE COLLECTION")
    print("4️⃣  EDIT A MOVIE")
    print("5️⃣  EXIT")
    print("=" * 40)
    choise = input("please coise a number (1-5): ")
    return choise
def main():
    global movie_collection
    movie_collection= load_data()                                              #download current data

    while True:
        choice = ana_menu()

        if choice == "1":                                                         #adding movie
            print("\n👩‍🎓 now you are adding movies")
            add_movie()
       
        elif choice == "2":                                                       #deleting movie
            print("\n🧑‍🎓 you are deleting movies")
            delete_movie()
        elif choice == "3":                                                        #looking movies
            print("\n📝 you are looking at the movie collection")
            look_at_collection()
        elif choice == "4":                                                         #fixing
            print('\n📝 you are editing movies')
            edit_movie()
        elif choice == "5":                                                         #exit
            print("\n🚪 Good bye! 🚪")
            break
        else:
            print("\n❌ please write a number between 1-5.")
if __name__ == "__main__":
    main()





#QUESTION 3

customer_data = {}



def add_customer():                                                                #new customer
    customer_id = input("Enter a unique customer ID: ")
    if customer_id in customer_data:
        print("This ID already exists. Please use a different ID.\n")
        return

    name = input("Name: ")
    surname = input("Surname: ")
    email = input("Email: ")
    phone = input("Phone: ")

    customer_data[customer_id] = {
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone
    }
    print(f"Customer {name} {surname} added successfully!\n")


def update_customer():                                                             #update customer
    customer_id = input("Enter the customer ID to update: ")
    if customer_id not in customer_data:
        print("Customer ID not found.\n")
        return

    print("Current information:")
    print(f"Name: {customer_data[customer_id]['name']}, Surname: {customer_data[customer_id]['surname']}, Email: {customer_data[customer_id]['email']}, Phone: {customer_data[customer_id]['phone']}")

    name = input("New Name (leave blank to keep current): ") or customer_data[customer_id]['name']
    surname = input("New Surname (leave blank to keep current): ") or customer_data[customer_id]['surname']
    email = input("New Email (leave blank to keep current): ") or customer_data[customer_id]['email']
    phone = input("New Phone (leave blank to keep current): ") or customer_data[customer_id]['phone']

    customer_data[customer_id] = {
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone
    }
    print(f"Customer {customer_id} updated successfully!\n")


def delete_customer():                                                               #delete customer
    customer_id = input("Enter the customer ID to delete: ")
    if customer_id in customer_data:
        del customer_data[customer_id]
        print(f"Customer {customer_id} deleted successfully!\n")
    else:
        print("Customer ID not found.\n")


def list_customers():                                                                   #lsit customer
    if not customer_data:
        print("\n\n\n\nNo customers in the system.\n")
        return

    print("\nCustomer List:")
    for customer_id, info in customer_data.items():
        print(f"ID: {customer_id}, Name: {info['name']}, Surname: {info['surname']}, Email: {info['email']}, Phone: {info['phone']}")
    print()


def main_menu():                                                                        #menu
    print("\n" + "=" * 45)
    print("       \U0001F4DA CUSTOMER MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1️⃣  Add New Customer")
    print("2️⃣  Update Customer Information")
    print("3️⃣  Delete Customer")
    print("4️⃣  List All Customers")
    print("5️⃣  Exit")
    print("=" * 45)
    choice = input("Please choose an option (1-5): ")
    return choice


def main():
    while True:
        choice = main_menu()

        if choice == "1":
            print("\n👤 Adding a new customer")
            add_customer()

        elif choice == "2":
            print("\n✏️ Updating customer information")
            update_customer()

        elif choice == "3":
            print("\n🗑️ Deleting a customer")
            delete_customer()

        elif choice == "4":
            print("\n📋 Listing all customers")
            list_customers()

        elif choice == "5":
            print("\n🚪 Exiting the program. Goodbye! 🚪\n")
            break

        else:
            print("\n❌ Invalid choice. Please select an option between 1-5.\n")

if __name__ == "__main__":
    main()

