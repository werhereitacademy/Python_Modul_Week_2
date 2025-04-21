# students = {
# 'Ahmet Yilmaz':	[85,90,	78],
# 'Mehmet emir':	[92,88,	76],
# 'Ayse Kaya':	[78,89,	95],
# 'Zeynep Celik':	[65,70,	80],
# 'Ali Kara':	    [50,60,	55],
# 'Fatma Yildiz':	[88,85,	90],
# 'Murat Aydin':	[72,68,74],
# 'Elif Aksoy':	[95,90,88],
# 'Hakan Oztiirk':[45,50,55],
# 'Canan Tas':	[80,75,82]
# }
# grades_list  = list(students.values()) 
# # print(grades_list)
# list = []
# for list in grades_list :  
#     avarage = sum(list) / len(list)
#     avarage_int = int(avarage)
#     list.append(avarage_int)
# print(students)

Students = {
    'Student_1': {'name': 'Ahmet Yilmaz', 'grades': [80,90,78]},
    'Student_2': {'name': 'Mehmet Demir', 'grades': [82,88,76]},
    'Student_3': {'name': 'Ayse Kaya', 'grades': [78,89,95]},
    'Student_4': {'name': 'Zeynep Celik', 'grades': [65, 70, 80]},
    'Student_5': {'name': 'Ali Kara', 'grades': [50, 60, 55]},
    'Student_6': {'name': 'Fatma Yildiz', 'grades': [88, 85, 90]},
    'Student_7': {'name': 'Mutrat Aydin', 'grades': [72, 68, 74]},
    'Student_8': {'name': 'Elif Aksoy', 'grades': [95, 90, 88]},
    'Student_9': {'name': 'Hakan Ozturk', 'grades': [45, 50, 55]},
    'Student_10': {'name': 'Canan Tas', 'grades': [80, 75, 82]}
}
#1-Calculate each student's GPA and add it to the dictionary.
i=1
for i in range(1,len(Students)+1) :
    student="Student_" + str(i)
    list= Students[student]['grades']
    avarage = sum(list) / len(list)
    avarage_int = int(avarage)
    Students[student].update([('GPA', avarage_int)])
    i+=1

print(Students)
# 2-Find the student with the highest GPA and print it on the screen.
i = 1
max = 0
student_max = " "
for i in range(1,len(Students)+1) :
    student="Student_" + str(i)
    gpa = int(Students[student]['GPA'])
    if gpa > max :
        max = gpa 
        student_max = student
print('Student',Students[student]['name'],'is with hights GPA of ', max)

# 3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.
Students_names = []
i = 1
for i in range(1,len(Students)+1) :
    student="Student_" + str(i)
    Full_name = Students[student]['name']
    # print (Full_name)
    Students_names.append((Full_name.split()[0],Full_name.split()[1]))
print(Students_names)

# 4-Sort the names in alphabetical order and print the sorted list on the screen.
Students_names = []
i = 1
for i in range(1,len(Students)+1) :
    student="Student_" + str(i)
    Full_name = Students[student]['name']
    # print (Full_name)
    Students_names.append(Full_name)
Students_names.sort()
print(Students_names)
    
# 5-Keep students with a GPA below 70 in a cluster (set).
cluster_set = []
i = 1
gba = 0
for i in range(1,len(Students)+1) :
    student="Student_" + str(i)
    gba = Students[student]['GPA']
    if gba < 70 :
        cluster_set.append(Students[student])
print("students with a GPA below 70 are : ",cluster_set)

