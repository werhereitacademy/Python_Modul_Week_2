"""
You need to write a Python program to process a student's grades. The program needs to perform the following functions:
Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades 
(Midterm, Final and Oral grades). For example:

1-Calculate each student's GPA and add it to the dictionary.

2-Find the student with the highest GPA and print it on the screen.

3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

4-Sort the names in alphabetical order and print the sorted list on the screen.

5-Keep students with a GPA below 70 in a cluster (set).
"""

student={}   # 10 Student information list.

i=0
while i < 2:   #Let each student have their name, surname and grades (Midterm, Final and Oral grades).
    
    i+=1
    
    name = str(input("Enter your  |Full name : "))
    midterm = int(input("Enter your midterm : "))
    final = int(input("Enter your final: "))
    oral = int(input("Enter your oral : "))
    
#1-Calculate each student's GPA and add it to the dictionary.
    student[i] = { 
                  "name" : name ,
                  "grades":[midterm,final, oral],
                  "gpa" : ((midterm + final + oral)//3)          # "i" is een uniek number.
                  } 
 
else :
    print(student)

#2-Find the student with the highest GPA and print it on the screen.
gpa_list = []
names_list = []

for i in range(1,3):  

    gpa_list.append(student[i]["gpa"])
    #It is for test , this mirror de data of k
    #k =student[i]["gpa"]
    #print(k)  
    na_me = student[i]["name"]
    names_list.append(na_me)


print(gpa_list)
print(max(gpa_list))

#4-Sort the names in alphabetical order and print the sorted list on the screen.
names_list.sort(key = str.lower) 
print(names_list)

#3- Separate each student's name from their surname and store them in 
# a separate tuple and add them to a list.
name_sepr= "-".join(names_list)
print(name_sepr)

#5-Keep students with a GPA below 70 in a cluster (set).
s = set()
for grad in gpa_list :
    if grad <= 70 :
        s.add(grad)
print(s)
