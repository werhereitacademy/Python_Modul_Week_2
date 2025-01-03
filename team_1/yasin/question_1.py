# Question1: Student Grades Processing
students = {
    "Ahmet Yilmaz" : [85, 90, 78],      
    "Mehmet Demir" : [92, 88, 76],
    "Ayse Kaya" : [78, 89, 95],
    "Zeynep Celik" : [65, 70, 80],
    "Ali Kara" : [50, 60, 55],
    "Fatma Yildiz" : [88, 85, 90],
    "Mutrat Aydin" : [72, 68, 74],
    "Elif Aksoy" : [95, 90, 88],
    "Hakan Ozturk" : [45, 50, 55],
    "Canan Tas" : [80, 75, 82],
}

# 1-Calculate each student's GPA and add it to the dictionary.

average_notes = {}

for student, notes in students.items():
    average = sum(notes) // len(notes)
    average_notes[student] = average
print(average_notes)
# average_notes ={
# 'Ahmet Yilmaz': 84,
# 'Mehmet Demir': 85,
#  'Ayse Kaya': 87,
#  'Zeynep Celik': 71,
#  'Ali Kara': 55,
#  'Fatma Yildiz': 87,
#  'Mutrat Aydin': 71,
#  'Elif Aksoy': 91,
#  'Hakan Ozturk': 50,
#  'Canan Tas': 79}

#2-Find the student with the highest GPA and print it on the screen.

student_max_note = max(average_notes, key =average_notes.get)   # average_notes.get("Ali") → 90, average_notes.get("Ayşe") → 94, average_notes.get("Mehmet") → 82
print(student_max_note, average_notes[student_max_note])

# max() max() fonksiyonu sözlükteki anahtarları alır: "Ali", "Ayşe", "Mehmet".
# Her anahtar için average_notes.get() fonksiyonu çalıştırılır:
# "Ali" için average_notes.get("Ali") → 90
# "Ayşe" için average_notes.get("Ayşe") → 94
# "Mehmet" için average_notes.get("Mehmet") → 82
# max() fonksiyonu bu değerleri karşılaştırarak en büyük değeri bulur: 94.
# max() fonksiyonu, en büyük değeri veren anahtarın adını döndürür: "Ayşe".
# student_max_note = Elif Aksoy

# 3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

new_students ={}

for student, notes in students.items():
    first_name = student.split()[0]     # Her bir ogrencinin adini soyadindan split metodu ile ayirdik ve sadece adini aldik.
    new_students[first_name] = notes

print(new_students) 
# {'Ahmet': [85, 90, 78],
#  'Mehmet': [92, 88, 76],
#  'Ayse': [78, 89, 95],
#  'Zeynep': [65, 70, 80],
#  'Ali': [50, 60, 55],
#  'Fatma': [88, 85, 90],
#  'Mutrat': [72, 68, 74],
#  'Elif': [95, 90, 88],
#  'Hakan': [45, 50, 55],
#  'Canan': [80, 75, 82]}

#4-Sort the names in alphabetical order and print the sorted list on the screen.
alphabetical_dictionary ={}
sorted_students = sorted(new_students.items()) # ogrenciler aslari siralandi notlariyla birlikte.

for student, note in sorted_students:              # for ile yeni sozluge atildilar.
        alphabetical_dictionary[student] = note

print(alphabetical_dictionary)

#{'Ahmet': [85, 90, 78],
#  'Ali': [50, 60, 55],
#  'Ayse': [78, 89, 95],
#  'Canan': [80, 75, 82],
#  'Elif': [95, 90, 88],
#  'Fatma': [88, 85, 90],
#  'Hakan': [45, 50, 55],
#  'Mehmet': [92, 88, 76],
#  'Mutrat': [72, 68, 74],
#  'Zeynep': [65, 70, 80]}

# 5-Keep students with a GPA below 70 in a cluster (set). 

below_70 = {}

for student, note in average_notes.items():
     if note <= 70:
          below_70[student] = note

print(below_70) 

#{'Ali Kara': 55,
#  'Hakan Ozturk': 50}