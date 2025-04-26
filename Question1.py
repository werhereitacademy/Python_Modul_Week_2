#We already have this in a dictionary called students
students = {                                    
    'Ahmet Yilmaz': [85, 90, 78],          #Each student has 3 grades: Midterm, Final, and Oral
    'Mehmet Demir': [92, 88, 76],
    'Ayse Kaya': [78, 89, 95],
    'Zeynep Celik': [65, 70, 80],
    'Ali Kara': [50, 60, 55],
    'Fatma Yildiz': [88, 85, 90],
    'Murat Aydin': [72, 68, 74],
    'Elif Aksoy': [95, 90, 88],
    'Hakan Ozturk': [45, 50, 55],
    'Canan Tas': [80, 75, 82]
}

# 1. Calculate GPA and add to dictionary
for name, grades, in students.items():          #We loop through the dictionary and add GPA to each student's info  ....
    midterm, final, oral = grades
    print(grades)
    print(type(grades))
    gpa = (midterm * 0.3) + (final * 0.5) + (oral * 0.2)
    students[name].append(round(gpa, 2))  #students[name]- gets the list of grades
print(students)                           #.append(...)- adds something to the end of the list.So it's the 4th value in position, but index 3 in code
                                          #round(gpa, 2)- rounds the GPA to 2 decimal places

# 2. Find student with highest GPA
highest_gpa = 0 #for now 0 , We'll update it later
top_student = "" #empty string, we dont know the best student yet
for name, grades in students.items():    #loop through the dictionary
    if grades[3] > highest_gpa:  #check if the student's GPA (grades[3]) higher than the current highest
        highest_gpa = grades[3]  #update highest_gpa to this student’s GPA
        top_student = name  #save the top_student name
print(f"Top student: {top_student} with GPA {highest_gpa}")

# 3. Separate names and surnames into a tuple list
name_tuples = []   #create an empty list
for full_name in students:      #loop through the dictionary  . students is a dictionary
    first, last = full_name.split()
    name_tuples.append((first, last))   #create a tuple first , last. add it to the list name_tuples
print(name_tuples)

# 4. Sort names alphabetically and print
sorted_names = sorted([first for first, last in name_tuples])   #sorted() function :sorts the lists in alphabetical order
print("Sorted first names:", sorted_names)  #prints the list of names in order

# 5. Students with GPA < 70 in a set                                                #{name for ... if ...} create a set
low_gpa_students = {name for name, grades in students.items() if grades[3] < 70}    #check their GPA, which is the 4th value in the list (index 3)
print("Students with GPA < 70:", low_gpa_students)                                  #if GPA is less than 70 , the student is added to the group
