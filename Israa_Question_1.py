#Question 1
students={
    'Ahmet Yilmaz':[85,90,78],
    'Mehmet Demir':[92,88,78],
    'Ayse Kaya':[78,89,95],
    'Zenep Celik':[65,70,80],
    'Ali Kara':[50,60,55],
    'Fatma Yildiz':[88,85,90],
    'Murat ydin':[72,68,74],
    'Elif Aksoy':[95,90,88],
    'Hakan Ozturk':[45,50,55],
    'Çanan Tas':[80,75,82]
}

# create new dictionary for averages and names:
averages={name:round(sum(grade)/len(grade),2) for name, grade in students.items()}
print('Averages : ', averages )
print('')

#find the student with the highest GPA:
heighest_GPA_student=max(averages)
heighest_GPA=averages[heighest_GPA_student]
print('Heighest GPA : ',heighest_GPA_student , ' ' , heighest_GPA)

print('')
#Separate each student's name from their surname and store them in a separate tuple and add them to a list
full_names=[( name.split()[0] ,name.split()[1] )for name in students.keys()]
print("Separate each student's name from their surname:")
print(full_names)

print('')
#Sort the names in alphabetical order and print the sorted list on the screen
names=[name[0] for name in full_names]
names.sort()
print('Sort the names in alphabetical order: ')
print(names)

print('')
#Keep students with a GPA below 70 in a cluster (set)
GPA_below_70={average for average in averages.values() if average<70}  
print('students with a GPA below 70: ',GPA_below_70)