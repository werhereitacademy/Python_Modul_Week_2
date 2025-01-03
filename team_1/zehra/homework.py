#Question1: Student Grades Processing
#1-Calculate each student's GPA and add it to the dictionary.
from ntpath import split

students={
    "Ahmet Yilmaz": [85,90,92],
    "Mehmet Demir": [92,88,60],
    "Ayse Kaya": [78,89,91],
    "Zeynep Celik": [65,70,81],
    "Ali Kara": [50,60,55],
    "Hakan Ozturk": [45,50,55]
}
#2-Find the student with the highest GPA and print it on the screen.

for student, grades in students.items():
    gpa=sum(grades)/len(grades)
    students[student].append(gpa)
max_student=[]
maxgpa=0
for student, grades in students.items():
    gpa=grades[-1]
    if gpa>maxgpa:
        maxgpa=gpa
        max_student=student
        print(max_student)

#3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

namelist=[]
for student in students.keys():
    a=student.split()
    b=(a[0],a[1])
    namelist.append(b)
print(namelist)

#4-Sort the names in alphabetical order and print the sorted list on the screen.

sorted_list=sorted(namelist)
print(sorted_list)

#5-Keep students with a GPA below 70 in a cluster (set).

low_scores=set()

for student, grades in students.items():
    gpa=sum(grades)/len(grades)
    if gpa<70:
        low_scores.add(student)
        print(low_scores)

######################################################################################

#Question 3: Customer Management System
musteriKoleksiyonu={}

musteriKoleksiyonu[1]={
    "musteriAdi":"ali",
    "musteriSoyadi":"ak",
    "musteriTelefonu":"0623162354",
    "musteriMail":"aliak@gmail.com"}


while True:
    print("Yeni musteri eklemek icin 1 yaziniz")
    print("Musteri bilgilerini guncellemek icin 2 yaziniz")
    print("musteri silmek icin 3 yaziniz")
    print("Tum musterileri listelemek icin 4 yaziniz")
    print("cikis yapmak icin 5 yaziniz")

    secenek=input("bir rakam giriniz")
    if secenek == "1":
        musteri_adi=input("Musteri adi:")
        musteri_soyadi=input("Musteri Soyadi:")
        musteri_tel=input("Musteri Telefonu:")
        musteri_mail=input("musteri mail:")

        musteri_id=len(musteriKoleksiyonu)+1
        musteriKoleksiyonu[musteri_id]={
            "musteriAdi": musteri_adi,
            "musteriSoyadi": musteri_soyadi,
            "musteriTelefonu": musteri_tel,
            "musteriMail": musteri_mail
            }
        print("yeni musteri basari ile eklendi")

    elif secenek == "2":
        musteri_id=int(input("guncellemek istediginiz bilginin numarasini giriniz:"))
        if musteri_id in musteriKoleksiyonu:
            print("Adi guncellemek icin 1")
            print("Soyadi guncelemek icin 2")
            print("Telefon numarasini guncellemek icin 3")
            print("maili guncellemek icin 4")

            secimguncelleme=input("guncellemek istedigini verinin numarasini giriniz:")
            if secimguncelleme == "1":
                yeni_ad=input("yeni adi giriniz:")
                musteriKoleksiyonu[musteri_id]["musteriAdi"]=yeni_ad
            elif secimguncelleme == "2":
                yeni_soyad=input("yeni soyadi giriniz:")
                musteriKoleksiyonu[musteri_id]["musteriSoyadi"]=yeni_soyad
            elif secimguncelleme=="3":
                yeni_tel=input("yeni tel no giriniz:")
                musteriKoleksiyonu[musteri_id]["musteriTelefonu"]=yeni_tel
            elif secimguncelleme=="4":
                yeni_mail=input("yeni mail adresini giriniz")
                musteriKoleksiyonu[musteri_id]["musteriMail"]=yeni_mail
            else:
                print("yanlis giris yaptiniz")
    elif secenek == "3":
        musteri_id = int(input("Silmek istediğiniz müşterinin ID'sini giriniz: "))
        if musteri_id in musteriKoleksiyonu:
            del musteriKoleksiyonu[musteri_id]
            print("Müşteri ID",musteri_id,"başarıyla silindi.")

    elif secenek == "4":
        if musteriKoleksiyonu:
            print("\nTüm Müşteri Listesi:")
            for id, musteri in musteriKoleksiyonu.items():
                print(
                    f"ID: {id}, Ad: {musteri['musteriAdi']}, Soyad: {musteri['musteriSoyadi']}, Tel: {musteri['musteriTelefonu']}, Mail: {musteri['musteriMail']}")
            print("------------------------")
        else:
            print("Hiç müşteri kaydı bulunmamaktadır.")

    elif secenek == "5":
        print("cikis yapiliyor")
        break

    else:
        print("gecersiz rakam yazdiniz lutfen 1 ile 5 arasi bir numara seciniz.")

##############################################################################################


