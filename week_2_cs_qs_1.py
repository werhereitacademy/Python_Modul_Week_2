#week-2 ws 1 Students
# Week 2 - Ödev 1
# 1-Calculate each student's GPA and add it to the dictionary.
# 2-Find the student with the highest GPA and print it on the screen.
# 3-Separate each student's name from their surname and store them in a separate tuple and add them to a list.
# 4-Sort the names in alphabetical order and print the sorted list on the screen.
# 5-Keep students with a GPA below 70 in a cluster (set)....

students= []

while True:
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    not1 = int(input("1. notu girin: "))
    not2 = int(input("2. notu girin: "))
    not3 = int(input("3. notu girin: "))
    ogrenci = {
    "ad": ad,
    "soyad": soyad,
    "notlar": [not1, not2, not3]
    }

    ortalama = sum(ogrenci["notlar"])// len(ogrenci["notlar"])
    ogrenci["ortalama"] = ortalama
    students.append(ogrenci)
    devam = input("Devam mı etmek istiyorsun Cıkmakmı istiyorsun: D_Q   :   ").upper()
    if devam !="D":
        break

# 1-Calculate each student's GPA and add it to the dictionary. 
isimler = [ogrenci["ad"] for ogrenci in students]
isimler.sort()
print(f" Sorted names: {isimler}")

# 2-Find the student with the highest GPA and print it on the screen.
highest = max(students, key=lambda x: x["ortalama"])
print(f" Highest student: {highest['ad']}")
print(f" Firs student: {isimler[-1]}")

# 3-Separate each student's name from their surname and store them in a separate tuple and add them to a list.
isimleri = [i["ad"] for i in students]
print(isimleri)

# 4-Sort the names in alphabetical order and print the sorted list on the screen.
isimleri.sort()
print(isimleri) 

# 5-Keep students with a GPA below 70 in a cluster (set).
under70 = [{"ad": ogrenci["ad"], "ortalama" : ogrenci["ortalama"]} for ogrenci in students if ogrenci["ortalama"]<70]

print(f" Under 70 student are : {under70}")
print(f" All students are : {students}")
        

