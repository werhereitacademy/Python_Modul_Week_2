# huiswerk
# Question1: Student Grades Processing
'''
Question1: Student Grades Processing
You need to write a Python program to process a student's grades. The program needs to perform the following functions:

Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Oral grades). For example:


1-Calculate each student's GPA and add it to the dictionary.

2-Find the student with the highest GPA and print it on the screen.

3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

4-Sort the names in alphabetical order and print the sorted list on the screen.

5-Keep students with a GPA below 70 in a cluster (set).

'''

# version 1
'''
# Bos bir sozlukk olusturuyoruz
students = {}

# 10 ogrencinin bilgilerini aliyoruz
for i in range(10):  
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    midterm = int(input("Please enter your midterm grade: "))
    final = int(input("Please enter your final grade: "))
    oral_grades = int(input("Please enter your oral grade: "))

    gpa = midterm * 0.4 + final * 0.5 + oral_grades * 0.1
    gpa = round(gpa, 2)

    # ogrencinin bilgilerini sozluge ekliyoruz
    full_name = first_name + " " + last_name
    students[full_name] = {
        "midterm": midterm,
        "final": final,
        "oral": oral_grades,
        "GPA": gpa,
    }

# 1. Tum ogrenci bilgilerini yazdir
print("\nStudent Information:")
for name, info in students.items():
    print("Name:", name)
    print("Midterm:", info["midterm"])
    print("Final:", info["final"])
    print("Oral:", info["oral"])
    print("GPA:", info["GPA"])
    print()

# 2. En yuksek GPA'ya sahip ogrenciyi bulma
max_gpa = 0
max_gpa_student = ""
for name, info in students.items():
    if info["GPA"] > max_gpa:
        max_gpa = info["GPA"]
        max_gpa_student = name

print("Student with the highest GPA:")
print("Name:", max_gpa_student)
print("GPA:", max_gpa)
print()

# 3. Her ogrencinin adini soyadindan ayirip tuple olarak bir listeye ekleme
name_tuple_list = []
for name in students.keys():
    split_name = name.split()
    name_tuple_list.append((split_name[0], split_name[1]))

print("List of first and last names as tuples:")
print(name_tuple_list)
print()

# 4. Adlari alfabetik siraya gore siralama
sorted_names = sorted(name_tuple_list)
sorted_names_list = []
for first, last in sorted_names:
    sorted_names_list.append(first + " " + last)

print("Sorted list of names:")
print(sorted_names_list)
print()

# 5. GPA'si 70'in altinda olan ogrencileri bir kumede toplama
low_gpa_students = set()
for name, info in students.items():
    if info["GPA"] < 70:
        low_gpa_students.add(name)

print("Students with GPA below 70:")
print(low_gpa_students)

'''
# version 2

'''
students={
    1:{"name":"ali", "surname":"er", "grades":{"midterm":90,"final":80, "oral":70}},
    2:{"name":"ahmet", "surname":"ak", "grades":{"midterm":80,"final":90, "oral":60}},
    3:{"name":"ayse", "surname":"cam", "grades":{"midterm":60,"final":75, "oral":95}},
    4:{"name":"kemal", "surname":"yilmaz", "grades":{"midterm":85,"final":65, "oral":75}},
    5:{"name":"murat", "surname":"yavuz", "grades":{"midterm":60,"final":50, "oral":40}},
    6:{"name":"fatma", "surname":"yalcin", "grades":{"midterm":90,"final":68, "oral":75}},
    7:{"name":"betul", "surname":"atay", "grades":{"midterm":50,"final":80, "oral":90}},
    8:{"name":"elif", "surname":"dogan", "grades":{"midterm":65,"final":95, "oral":100}},
    9:{"name":"mustafa", "surname":"aslan", "grades":{"midterm":60,"final":95, "oral":95}},
    10:{"name":"zeynep", "surname":"koc", "grades":{"midterm":30,"final":40, "oral":50}}
}
def averages(grades):
    return(grades["midterm"]*0.30)+(grades["final"]*0.60)+(grades["oral"]*0.10)

average_grades={
    student_id:{
        "name":data["name"],
        "surname":data["surname"],
        "gpa":averages(data["grades"])
}
    for student_id, data in students.items()
}
average_grades

print("\nAll students:")

counter=1
for student_id, data in average_grades.items():
    print(f"{counter}:{data["name"]} {data["surname"]}, GPA:{data["gpa"]:.2f}")
    counter+=1

max_gpa=-1
max_student=list(average_grades.values())[0]
for data in average_grades.values():
    if data["gpa"]>max_gpa:
        max_gpa=data["gpa"]
        max_student=data
print(f"\nHigest GPA:{max_student["name"]} {max_student["surname"]}, GPA:{max_student["gpa"]:.2f}")

name_list= []
print("\ntuple list:")
for data in students.values():
    name_list.append((data['name'], data['surname']))
print(name_list)

def sort_key(item):
    return item[0], item[1]

name_list_sorted=sorted(name_list, key=sort_key)
print("\nAlphabetical sorting:\n")
for name, surname in name_list_sorted:

    print(f"{name} {surname}")



low_gpa_cluster={
    f"{data['name']} {data['surname']}"
    for data in students.values()
    if averages(data["grades"])<70
}

print("\ncluster of students with GPA below 70:")
print(low_gpa_cluster)

'''
# version 3

'''
students={
    'Ahmet yılmaz'  :[85,90,78],
    'Mehmet demir'  :[92,88,76],
    'Ayşe kaya'     :[78,89,95],
    'Zeynep çelik'  :[65,70,80],
    'Ali kara'      :[50,60,55],
    'Fatma yildiz'  :[88,85,90],
    'Murat aydın'   :[72,68,64],
    'Elif Aksoy'    :[95,90,88],
    'Hakan Öztürk'  :[45,50,55],
    'Canan taş'     :[80,75,82]
    }
# 1- Her öğrencinin GPA'sini hesaplayıp sözlüğe ekleyelim
# Her öğrencinin notlarının ortalamasını hesaplama
average_scores = {name: (lambda scores: sum(scores) / len(scores))(scores) for name, scores in students.items()}

# Sonuçları yazdır
print('ISIMLER VE NOT ORTALAMALARI: ',average_scores)

# 2.En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.
top_student =max(average_scores, key=average_scores.get)

top_average =average_scores[top_student]

print(f"En yüksek not ortalamasına sahip öğrenci: {top_student} ({top_average:.2f})")

# 3.Her öğrencinin adını soyadından ayırın, bunları ayrı bir tuple içinde saklayın ve bir listeye ekleyin.
#  keys(): Dictionary içindeki tüm anahtarları bir liste olarak döndürür.
nameSurnameList=[(name.split()[0], name.split()[1]) for name in students.keys()]
print(nameSurnameList)

# 4.Adları alfabetik sıraya göre sıralayın ve sıralı listeyi ekrana yazdırın.
siraliListe=sorted(students.keys())
print(siraliListe)

# 5.Not ortalaması 70'in altında olan öğrencileri bir kümede (set) tutun.
# . items(): Dictionary içindeki tüm anahtar-değer çiftlerini bir liste olarak döndürür.
below_70_set = {name for name, scores in students.items() if sum(scores) / len(scores) < 70
}

# Print the set of students
print('70in altindakiler',below_70_set)

'''

# Question 2: Film Library Management System Project
'''
Question 2: Film Library Management System Project
Project Description: This project aims to create an application that will help the user manage their movie collection. 
Users can add, edit, delete movies and view their collection.

Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

Basic Functions:

1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

4-Save the movie data in a file and restore this data when you start the program.

'''
# version 1
'''
movies=[]
while True:
    movie={}
    movie["name"]=input("write the name of the movie:")
    movie["director"]=input("write the director of the movie:")
    movie["release year"]=input("write the release year of the movie:")
    movie["genre"]=input("write the genre of movie:")

    movies.append(movie)
    another=input("do you want to add another movie?(Y/N)").strip().lower()
    if another!="y":
        break
print("\nAll Movies:")

counter=1
for movie in movies:
    print(f"movie{counter}:{movie}")
    counter+=1

while True:
    change=input("Do you want to change the movie list?(edit/delete/exit):").strip().lower()

    if change=="edit":
        movie_number=int(input("Enter the movie number to edit:"))-1
        if 0<=movie_number<len(movies):
            movie=movies[movie_number]
            movie["name"]=input(f"name ({movie["name"]}):") or movie["name"]
            movie["director"]=input(f"director({movie["director"]}):") or movie["director"]
            movie["release year"]=input(f"release year({movie["release year"]}):") or movie["release year"]
            movie["genre"]=input(f"genre({movie["genre"]}):") or movie["genre"]
            print("movie updated successfully")
        else:
            print("invalid number")
    elif change=="delete":
        movie_number=int(input("Enter the movie number to delete:"))-1
        if 0 <= movie_number < len(movies):
            deleted_movie=movies.pop(movie_number)
            print(f"movie {deleted_movie["name"]} deleted successfully")
        else:
            print("invalid number")
    elif change=="exit":
        print("exiting the program")
        break
    else:
        print("invalid entry(edit/delete/exit)")

'''
# version 2
'''
# 1- Kullanıcıdan film adı, yönetmen, çıkış yılı ve tür gibi bilgileri alarak bir film verisi oluşturun ve bunu bir sözlükte saklayın.
def film_listesi_olustur():
    film={}
    film['ad']=input('film adi:')
    film['yonetmen']=input('yonetmen adi:')
    film['cikis_yili']=int(input('cikis yili:'))
    film['tur']=input('tur: (ornek: bilim kurgu, dram vs.)')
    return film
# Birden fazla film için örnek kullanım:
print(film_listesi_olustur())

# 2- Kullanıcıya bir filmi düzenleme veya silme seçeneği sunun.
# (Bunun için, kullanıcı hangi veriyi değiştirmek istiyorsa ona uygun bir fonksiyon yazılmalıdır.)
def film_duzenle(filmler, film_adi):
    for film in filmler:
        if film ['ad']==film_adi:
            print('bulunan film')
            print(film)
            film['ad']=input('yeni film adi:')
            film['yonetmen']=input('yeni yonetmen:')
            print('film basariyla guncellendi')
            return
        print('boyle bir film bulunamadi')

def film_sil(filmler, film_adi):
    for i , film in enumerate(filmler):
        if film ['ad']==film_adi:
            del filmler[i]
            print('film basariyla silindi')
            return
        print('boyle bir film bulunamadi')

filmer=[]
while True:
    print("\n1-film ekle\n2-film duzenle\n3-film sil\n4-cikis")
    secim=input('seciminizi yapin')

    if secim=='1':
        yeni_film=film_olustur()
        filmler.append(yeni_film)
    elif secim=='2':
        film_adi=input('duzenlemek istediginiz film adini girin:')
        film_duzenle(filmler, film_adi)
    elif secim=='3':
        film_adi==input('silmek istediginiz filmin adini girin')
        film_sil(filmler, film_adi)
    elif secim=='4':
        break
    else:
        print('gecersiz secim')

print('\nTum filmler:')
for film in filmler:
    print(film)

'''
# version 3
'''
film_bilgisi = {}

def film_ekleme():
    """Kullanıcıdan film bilgilerini alır ve koleksiyona ekler."""
    film_adi = input("Film adı: ").lower()
    yonetmen = input("Yönetmen: ").lower()
    yayin_yili = input("Yayın yılı: ").lower()
    tur = input("Tür: ").lower()
    film_bilgisi[film_adi] = {
        "yönetmen": yonetmen,
        "yayın yılı": yayin_yili,
        "tür": tur,
    }
    print(f"'{film_adi}' başarıyla eklendi.")

def film_koleksiyon_goruntuleme():
    """Film koleksiyonunu ekrana yazdırır."""
    if not film_bilgisi:
        print("Koleksiyon boş.")
        return
    print("\nTüm Filmler:")
    for film, detaylar in film_bilgisi.items():
        print(f"\nFilm Adı: {film}")
        for anahtar, deger in detaylar.items():
            print(f"{anahtar.capitalize()}: {deger}")

def film_duzenleme():
    """Kullanıcının belirttiği filmi düzenler."""
    film_adi = input("Düzenlemek istediğiniz filmin adını giriniz: ").lower()
    if film_adi in film_bilgisi:
        print(f"'{film_adi}' için mevcut bilgiler:")
        for anahtar, deger in film_bilgisi[film_adi].items():
            print(f"{anahtar.capitalize()}: {deger}")
        print("\nAşağıdaki seçeneklerden birini girin:")
        print("a: Yönetmen\nb: Yayın Yılı\nc: Tür")
        secim = input("Hangi bilgiyi güncellemek istiyorsunuz? (a/b/c): ").lower()
        alanlar = {"a": "yönetmen", "b": "yayın yılı", "c": "tür"}
        if secim in alanlar:
            yeni_deger = input(f"Yeni {alanlar[secim]}: ").lower()
            film_bilgisi[film_adi][alanlar[secim]] = yeni_deger
            print(f"'{film_adi}' başarıyla güncellendi.")
        else:
            print("Geçersiz seçim.")
    else:
        print("Film bulunamadı.")

def film_silme():
    """Kullanıcının belirttiği filmi koleksiyondan siler."""
    film_adi = input("Silmek istediğiniz filmin adını giriniz: ").lower()
    if film_adi in film_bilgisi:
        del film_bilgisi[film_adi]
        print(f"'{film_adi}' koleksiyondan silindi.")
    else:
        print("Film bulunamadı.")

# Menü Döngüsü
while True:
    print("\n1. Film Ekle\n2. Koleksiyon Görüntüle\n3. Film Düzenle\n4. Film Sil\nq. Çıkış")
    secim = input("Lütfen bir seçenek girin: ").lower()
    if secim == "1":
        film_ekleme()
    elif secim == "2":
        film_koleksiyon_goruntuleme()
    elif secim == "3":
        film_duzenleme()
    elif secim == "4":
        film_silme()
    elif secim == "q":
        print("Çıkış yapılıyor.")
        break
    else:
        print("Geçersiz seçenek, tekrar deneyin.")

'''
# Question 3: Customer Management System
'''
Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.

2-Provide a menu where the user can choose the following actions:

Add new customers
Updating customer information
Delete customer
List all customers
Check out
3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.

4-When updating customer information, view the current information using the customer ID and save the updated information.

5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.

6-In the process of listing all customers, view the list of existing customers.

7-Repeat the process until the user logs out.
'''
# version 1
'''
def main():
    customers = {}
    customers_no = 1

    while True:
        print("\n--- Customers List ---")
        print("1. Add Customers")
        print("2. Update Customers")
        print("3. Delete Customers")
        print("4. View Customers")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":  # Müşteri ekleme
            name = input("Enter the customer's name: ")
            surname = input("Enter the customer's surname: ")
            email = input("Enter the customer's email: ")

            # Telefon numarası doğrulama
            while True:
                try:
                    tel = int(input("Enter the customer's telephone: "))
                    break
                except ValueError:
                    print("Please enter a valid number for the telephone.")

            customers[customers_no] = {"Ad": name, "Soyad": surname, "E-mail": email, "Telefon": tel}
            print(f"Customer {customers_no} added successfully!")
            customers_no += 1

        elif choice == "2":  # Müşteri güncelleme
            if not customers:
                print("No customers to update.")
            else:
                print("\nYour customers:")
                for id, info in customers.items():
                    print(f"ID: {id}, Customers Infos: {info}")

                try:
                    update_customer = int(input("Enter the ID of the customer to update: "))
                    if update_customer in customers:
                        updated_name = input("Enter the new name of the customer: ")
                        updated_surname = input("Enter the new surname of the customer: ")
                        updated_email = input("Enter the new email of the customer: ")

                        # Telefon numarası doğrulama
                        while True:
                            try:
                                updated_tel = int(input("Enter the new telephone of the customer: "))
                                break
                            except ValueError:
                                print("Please enter a valid number for the telephone.")

                        # Doğru anahtar isimleri
                        customers[update_customer] = {
                            "Ad": updated_name,
                            "Soyad": updated_surname,
                            "E-mail": updated_email,
                            "Telefon": updated_tel
                        }
                        print(f"Customer {update_customer} has been updated.")
                    else:
                        print("Customer ID does not exist.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":  # Müşteri silme
            if not customers:
                print("No customers to delete.")
            else:
                print("\nYour customers:")
                for id, info in customers.items():
                    print(f"ID: {id}, Customers Infos: {info}")

                try:
                    delete_customer = int(input("Enter the ID of the customer to delete: "))
                    if delete_customer in customers:
                        delete_customer = customers.pop(delete_customer)
                        print(f"Customer {delete_customer} has been deleted.")
                    else:
                        print("Customer ID does not exist.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":  # Müşteri görüntüleme
            if customers:
                for id, info in customers.items():
                    print(f"ID: {id}, Customers Infos: {info}")
            else:
                print("No customers found!")

        elif choice == "5":  # Programdan çıkış
            print("Goodbye!")
            break

        else:  # Geçersiz giriş
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

'''
# version 2
'''
customers=[]
while True:
    customer={}
    customer["name"]=input("write the name of the customer:")
    customer["surname"]=input("write the surname of the customer:")
    customer["e-mail"]=input("write the e-mail of the customer:")
    customer["phone number"]=input("write the phone number of customer:")

#add new customer
    customers.append(customer)
    another=input("do you want to add another customer?(Y/N)").strip().lower()
    if another!="y":
        break
print("\nAll Customer:")

counter=1
for customer in customers:
    print(f"customer{counter}:{customer}")
    counter+=1
#transaction on the customer list
while True:
    another=input("do you want to make a transaction on the customer list?(Y/N)").strip().lower()
    if another!="y":
        break
    change=input("please enter the number of the transaction you want to make:\n"
                 "1-update customer information\n"
                 "2-delete customer\n"
                 "3-list all customers\n"
                 "4-exit\n").strip().lower()

    if change=="1":
        customer_number=int(input("Enter the customer number to update:"))-1
        if 0<=customer_number<len(customers):
            customer=customers[customer_number]
            customer["name"]=input(f"name ({customer["name"]}):") or customer["name"]
            customer["surname"]=input(f"surname({customer["surname"]}):") or customer["surname"]
            customer["e-mail"]=input(f"e-mail({customer["e-mail"]}):") or customer["e-mail"]
            customer["phone number"]=input(f"phone number({customer["phone number"]}):") or customer["genre"]
            print("customer information updated successfully")
        else:
            print("invalid number")
    elif change=="2":
        customer_number=int(input("Enter the customer number to delete:"))-1
        if 0 <= customer_number < len(customers):
            deleted_customer=customers.pop(customer_number)
            print(f"customer {deleted_customer["name"]} {deleted_customer["surname"]} deleted successfully")
        else:
            print("invalid number")
    elif change=="3":
        print("\nAll customers:")
        for customer in customers:
            print(customer)

    elif change=="4":
        print("exiting the program")
        break
    else:
        print("invalid entry")
'''
