students ={}

for i in range (0,3):

    student = {input("Name, Surname? "):[int(input("midterm ")),int(input("final ")), int(input("oral "))]}

    students.update(student)

    print(students)

for i in students:

    students[i].append(round(sum(students[i])/3))

print(students)

avg=[]

for i in students:

    avg.append((students[i])[-1])

print("Biggest average grade: ",i, max(avg))

Names=[]

print(students.keys())

for i in list(students.keys()):

    i.split(" ")[0]

    Names.append(i.split(" ")[0])

print(tuple(Names))

print("sorted names: ", sorted(Names))

Unseccesfull=[]

for i in students:

   if (students[i])[-1]<70:

    Unseccesfull.append(i)

print(set(Unseccesfull))

Unseccesfull=set(Unseccesfull)

for i in students:

   if (students[i])[-1]<70:

    Unseccesfull.add(i)

print("Unseccesfull students: ",Unseccesfull)