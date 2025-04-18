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


