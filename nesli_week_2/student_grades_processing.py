# ### Question1: Student Grades Processing

# You need to write a Python program to process a student's grades. The program needs to perform the following functions:
# Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Oral grades). For example:
# ![image](https://github.com/user-attachments/assets/0e3f85a4-bf24-4b22-b0ea-f9b3dbda4fc8)

# 1-Calculate each student's GPA and add it to the dictionary.
# 2-Find the student with the highest GPA and print it on the screen.
# 3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.
# 4-Sort the names in alphabetical order and print the sorted list on the screen.
# 5-Keep students with a GPA below 70 in a cluster (set).


#TR
# Bir öğrencinin notlarını işlemek için bir Python programı yazmanız gerekiyor. Programın aşağıdaki işlevleri gerçekleştirmesi gerekiyor:
# Bir sözlük kullanarak 10 öğrenci için bilgi ve notları depolayın. Her öğrencinin adını, soyadını ve notlarını 
# (Vize, Final ve Sözlü notları) almasını sağlayın. Örneğin:

# 1-Her öğrencinin not ortalamasını hesaplayıp sözlüğe ekleyin.
# 2-En yüksek not ortalamasına sahip öğrenciyi bulup ekrana yazdırın.
# 3- Her öğrencinin adını soyadından ayırıp ayrı bir tuple'da saklayıp bir listeye ekleyin.
# 4-İsimleri alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
# 5-GNO'su 70'in altında olan öğrencileri bir kümede (kümede) tutun.


students = {

'Ahmet yilmaz': {'grades':  [85, 90, 78]},
'Mehmet Demir': {'grades': [92, 88,76]},
'Ayse Kaya': {'grades': [78, 89, 95]},
'Zeynep Celik': {'grades': [65, 70, 80]},
'Ali Kara': {'grades': [50, 60, 55]},
'Fatma Yildiz': {'grades': [88, 85, 90]},
'Murat Aydin': {'grades': [72, 68, 74]},
'Elif Aksoy': {'grades': [95, 90, 88]},
'Hakan Ozturk': {'grades':  [45, 50, 55]},
'Canan Tas': {'grades': [80, 75, 82]}
}


#1/averages

for student_name, info in students.items():
    grades = info['grades']
    average = sum(grades) / len(grades) #average
    info['average'] = average #ortalama bilgisi ekledik
    

#2/enyuksekortalamayasahipogrenci

highest_avg = 0
top_student = None

for student_name, info in students.items():
    if info['average'] > highest_avg:
        highest_avg = info['average']
        top_student = student_name
print(f"student with the highest grade point average: {top_student}, average: {highest_avg:.2f}")

#3/ad soyadi ayri ayri tuple olustur

name_surname_list = []
for student_name in students.keys():
    first_name, last_name = student_name.split() #ad ve soyadini ayir
    name_surname_list.append((first_name, last_name))#tuple olarak ekle


#4 Soru 4: İsimleri alfabetik sıraya göre sıralayın
#  ve sıralanmış listeyi ekrana yazdırın
#1)
sorted_names = sorted(name_surname_list, key= lambda x:x[0])
print("sorted list of names" , sorted_names)

#2)
# def get_first_name(name_tuple):
#     return name_tuple[0]#tuple'in ilk elemanini doner.
# sorted_names = sorted(name_surname_list, key=get_first_name)
# print("siralanmis _isim_listesi:", sorted_names)
#Sıralama, veri üzerinde düzenli çalışmayı sağlar ve okunabilirliği artırır.
# Nasıl sıralıyoruz?

# Python’un sorted() fonksiyonunu kullanıyoruz.
# Sıralama kriterini belirlemek için key=lambda x: x[0] kullanıyoruz; bu, x[0] ile isimlere göre sıralama yapar.
# Adımlar:

# Listeyi sırala: sorted() ile isimlere göre sırala.


#Soru 5: GNO'su 70'in altında olan öğrencileri bir kümede tutun
low_avg_students =set()

for student_name, info in students.items():
    if info['average'] < 70: #GNo su 70 in altinda mi kontrol et
        low_avg_students.add(student_name)
print("students with a GPA below 70 :", low_avg_students)