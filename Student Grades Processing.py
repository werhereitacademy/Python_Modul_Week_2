students = {
    'Ahmet Yılmaz': [85, 90, 78],
    'Mehmet Demir': [92, 88, 76],
    'Ayşe Kaya': [78, 89, 95],
    'Zeynep Çelik': [65, 70, 80],
    'Ali Kara': [50, 60, 55],
    'Fatma Yıldız': [88, 85, 90],
    'Murat Aydın': [72, 68, 74],
    'Elif Aksoy': [95, 90, 88],
    'Hakan Öztürk': [45, 50, 55],
    'Canan Taş': [80, 75, 82]
}

# ----------------------------
# Question 1: Calculate the GPA of each student
# ----------------------------
top_student = None
top_gpa = 0
low_gpa_students = set()  # For Q5

print("GPAs:\n")
low_gpa_students = set()
for name, grades in students.items():
    gpa=sum(grades)/3


    # For Question 2
    if gpa > top_gpa:
        top_gpa=gpa
        top_student=name

    # For Question 5: Add to set if GPA is below 70
    if gpa < 70:
        low_gpa_students.add(name)
    print(f"{name}: {gpa:.2f}")

# ----------------------------
# Question 2: Print the student with the highest GPA
# ----------------------------
print("\nTop student is:", top_student)
print("With GPA:", f"{top_gpa:.2f}")


# ----------------------------
# Question 3: Separate names into (first_name, last_name) tuples
# ----------------------------
name_tuples = []

for student in students:
    first_name, last_name = student.split()
    name_tuples.append((first_name, last_name))


print("\nList of name tuples:")
print(name_tuples)


# ----------------------------
# Question 4: Sort the name tuples alphabetically
# ----------------------------

name_tuples.sort()
print("Sorted names:")
print(name_tuples)

# ----------------------------
# Question 5: Print students with GPA below 70 (stored in a set)
# ----------------------------
print("low gpa studnets")
print(low_gpa_students)
