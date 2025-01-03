'''
#Question1: Student Grades Processing

#Listing a group of students and their grades

print("Welcome to Student Grades Processing Program")
students_grades = {
    'Cem Yakışıklı' : [50, 45, 70],
    'Ahmet Demir' : [74, 87, 56],
    'Ahmet Türkan' : [34, 70, 100],
    'Yusuf Akbaba' : [20, 100, 79],
    'Musa Kılıç' : [67, 34, 56],
    'Sinem Çelik' : [45, 40, 50],
    'Bağrım Bakır' : [90, 80, 95],
    'Çiğdem Çıldır' : [78, 44, 87],
    'Sezai Serkeş' : [45, 73, 89],
    'Yunus Kandır' : [87, 45, 90]
}

#Calculate GPA for each student
for grades in students_grades.values():
    gpa = sum(grades)/len(grades) #GPA calculated as the average of grades
    grades.append(gpa) #GPA add to the end of the grades

#Print each students names, grades and GPA
for student, grades in students_grades.items():
    print(f"\n{student}: {grades[:-1]}, GPA: {grades[-1]:.2f} ")


#Find the highest GPA and its owner
top_student = None
highest_gpa = 0

for student, grades in students_grades.items():

    if grades[-1] > highest_gpa:
        highest_gpa = grades[-1]
        top_student = student



#Print the students name and GPA having the highest GPA

print(f"\nThe student having the highest GPA is {top_student} with a GPA of {highest_gpa:.2f}")

# List to store tuples of first and last names
names_list = []  
for student in students_grades.keys():
    student_name = student.split()  
    first_name, last_name = student_name[0], student_name[1]
    names_list.append((first_name, last_name)) 

print("\nList of names (First, Last):", names_list)

#Sort the names in alphabetical order and print the sorted list on the screen.
names_list.sort()

print(f"\nList of sorted names: {names_list}")

#Keep students with a GPA below 70 in a cluster (set).

students_below_70 = set()

for student, grades in students_grades.items():
    if grades[-1] < 70:
        students_below_70.add(student)

print(f"\nStudents with GPA below 70: {students_below_70}")
'''




'''print("Film Library Management System\n") 

film_pool = {}

while True:
    
    print("1. Add Movie")
    print("2. Edit Movie")
    print("3. Delete Movie")
    print("4. View Collection")
    print("5. Save and Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    #Add Movie

    if choice == '1':

        film_name = input("Please enter the name of the movie: ")
        film_director = input("Please enter the director of the movie: ")
        film_year = input("Please enter the release year of the movie: ")
        film_genre = input("Please enter the genre of the movie: ")
        film_pool[film_name] = {
            'Director' : film_director,
            'Release Year' : film_year,
            'Genre' : film_genre

        }

        print(f"Movie '{film_name}' added successfully.")
    
    #Edit Movie

    elif choice == '2':
        film_name = input("Please enter the name you want to edit: ")

        if film_name in film_pool:
            print("What would you like to edit?")
            edit_choice = input("To edit director please press 1 \nTo edit release year press 2 \nTo edit genre press 3: ")
            if edit_choice == '1':
                film_pool['Director'] = input("Please enter the new name: ")
            elif edit_choice == '2':
                film_pool['Release Year'] = input("Please enter the new year: ")
            elif edit_choice == '3':
                film_pool['Genre'] = input("Please enter the new genre: ")

            else:
                print("Invalid choice.")

            print(f"You have edited {film_name} successfully.")

        else:
            print("Tha name you entered could not be found on the list.")


    #Delete Movie

    elif choice == '3':
        film_name = input("Please enter the movie to be deleted: ")
        if film_name in film_pool:
            del film_pool[film_name]
            print(f"{film_name} is deleted from the list")

        else:
            print("The name you entered could not be found.")

    #View Collection

    elif choice == '4':
        if not film_pool:
            print("No movies in the list yet.")

        else:
            print("What do you want to view?")
            print("1. View all movies.")
            print("2. Filte by director.")
            print("3. Filter by release date.")
            print("4. Filter by genre.")

            view_choice = input("Please enter your choice number: ")
            if view_choice == '1':
                for name, details in film_pool.items():
                    print("Name : {film_name}, Director: {details['Director']}, Release Year: {details['Release Year']}, Genre: {details['Genre']}")

            elif choice == '2':
                director_filter = input("Enter director to filter by: ")
                for name, details in film_pool.items():

                    if details['Director'] == director_filter:
                        print(f"Name: {name}, Director: {details['Director']}, Release Year: {details['Release Year']}, Genre: {details['Genre']}")


            elif choice == '3':
                release_filter = input("Enter a year to filter by: ")
                for name, details in film_pool.items():

                    if details['Release Year'] == release_filter:
                        print(f"Name: {name}, Director: {details['Director']}, Release Year: {details['Release Year']}, Genre: {details['Genre']}")

            elif choice == '4':
                genre_filter = input("Enter a genre to filter by: ")
                for name, details in film_pool.items():

                    if details['Genre'] == genre_filter:
                        print(f"Name: {name}, Director: {details['Director']}, Release Year: {details['Release Year']}, Genre: {details['Genre']}")
            else:
                print("Invalid choice.")
'''


print("Customer Management System\n") 

customer_pool = {}

customer_id = 100

while True:
    
    print("1. Add Customer")
    print("2. Updating Customer Information")
    print("3. Delete Customer")
    print("4. List All Customers ")
    print("5. Check Out")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        customer_name = input("Please enter the customer name: ")
        customer_phone = input("Please enter the customer's phone number: ")
        customer_email = input("Please enter the customer's email: ")
        customer_id +=1
        customer_pool[customer_id] = {
            'Name' : customer_name,
            'Phone' : customer_phone,
            'Email' : customer_email,
        }
    print(f"{customer_name} is registered with the customer id: {customer_id}.")
    









   


    
    
    
    
    

   
    






