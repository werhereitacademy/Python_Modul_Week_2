###  Question 1 

students = {
    'Ahmet Yılmaz': [85, 90, 78],  
    'Mehmet Demir': [92, 88, 76],  
    'Ayşe Kaya': [78, 89, 95],     
    'Zeynep Çelik': [65, 70, 80],  
    'Ali Kara': [50, 60, 55],      
    'Fatma Yıldız': [88, 85, 90],  
    'Murat Aydın': [72, 68, 74],   
    'Elif Aksoy': [95, 90, 88],    
    'Hakan Öztürk': [45, 50, 55],  
    'Canan Taş': [80, 75, 82]      
}

#1-Calculate each student's GPA and add it to the dictionary.

for student, item in students.items():
    average=sum(item)/len(item)
    students[student].append(average)
    print(f"Student:{student}, GPA:{average}")


#Find the student with the highest GPA and print it on the screen.
h_name=""
h_score=0
for student,item in students.items():
    if item[3]>h_score:
        h_score=item[3]
        h_name=student

print(f"Student:{h_name}, GPA:{h_score}")

#Separate each student's name from their surname and store them in a separate tuple and add them to a list.

lst=[]

for student in students.keys():
    temp_name=student.split()
    lst.append(tuple(temp_name))

print(lst)

#Sort the names in alphabetical order and print the sorted list on the screen.
lst_2=[student for student in students.keys()]
lst_2.sort()
print(lst_2)


#Keep students with a GPA below 70 in a cluster (set).

set_1=set([student for student,item in students.items() if item[3]<70])


#Question 2 

# 1 Kullanicinin gorecegi giris metnini yaz
# 2 Kullanicidan girdi al--> Film adi, Yonetmeni, Yayin yili, Film turu
# 3 Aldigin verileri array a ekle dict olarak sakla
# 4 Kullaniciya verileri duzenleme ve silme secenegi ver( buna uygun fonksiyon yaz)
# 5 Kullanicinin film koleksiyonunu goruntulemesine izin ver.Tum filmleri listele veya tur-yayin yili gibi kriterlere gore filtrele.
# 6 Film verilerini bir dosyaya kaydet ve program basladiginda bu verileri geri yukle.

import json

with open("movielist.json", "r", encoding="utf-8") as json_dosyasi:
    saved_movies  = json.load(json_dosyasi)



menu = [' -----------------------------------------------------',
        '|                                                     |',
        '|      Movie Collection uygulamasina hos geldiniz.    |',
        '|                                                     |',
        '|      Yeni film  eklemek için 1 e,                   |',
        '|                                                     |',
        '|      Film  silmek için 2 ye,                        |',
        '|                                                     |',
        '|      Film güncellemek için 3 e,                     |',
        '|                                                     |',
        '|      Tüm filmleri görmek için 4 e basiniz.          |',
        '|                                                     |',
        '|                                                     |',
        ' -----------------------------------------------------']

for i in menu:
    print('\t'.expandtabs(30), i)
user = input("Lutfen yapmak istediginiz islem icin bir secenege basiniz: ")

if user == "1":  # kullanici yeni bir film eklemek istiyorsa calisir

    movie_name = input("Film adini giriniz: ")
    movie_director_name = input("Filmin yonetmeni:  ")
    movie_year = input("Filmin yayin yilini giriniz: ")
    movie_type = input("Filmin turunu giriniz: ")

    movie_list=[]
    movie_dict = {}

    movie_dict["movie_name"] = movie_name
    movie_dict["movie_director_name"] = movie_director_name
    movie_dict["movie_year"] = movie_year
    movie_dict["movie_type"] = movie_type

    saved_movies.append(movie_dict)

    with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)
    print("Yeni film kaydedildi!")

if user == "2":
    
    deleted_movie = input("Lutfen silmek istediginiz filmin adini yaziniz: ")
    for movie in saved_movies:
        if movie["movie_name"] == deleted_movie:
            saved_movies.remove(movie)
            with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
                json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)
            movie_found = True
        if movie_found == False:
            print("Aradiginiz film bulunamistir")

if user == "3":
    movie_want_to_updated = input(
        "Guncellemek istediginiz filmin adini giriniz: ")
    movie_found = False
    for movie in saved_movies:  # for movie in saved_movies:
        if movie["movie_name"] == movie_want_to_updated:
            print("Filmin adini guncellemek icin 1'e, filmin yonetmenini guncellemek icin 2'ye, filmin yayin yilini guncellemek icin 3'e, filmin turunu guncellemek icin 4'e basiniz!")
            user_choice = input(
                "Lutfen yapmak istediginiz islem icin bir secenege basiniz: ")
            if user_choice == "1":
                new_movie_name = input("Lutfen Yeni Film Adi Giriniz: ")
                movie["movie_name"] = new_movie_name

                with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
                    json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)

                movie_found=True
            if user_choice=="2":
                new_director=input("Lutfen Yeni yonetmen adini gir: ")
                movie["movie_director_name"] =new_director
                with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
                    json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)
                movie_found=True
            if user_choice=="3":
                new_movie_year=input("Yeni Film yilini giriniz: ")
                movie["movie_year"]=new_movie_year
                with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
                    json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)
                movie_found=True
            if user_choice=="4":
                new_movie_type=input("Filmin yeni turunu giriniz: ")
                movie["movie_type"]=new_movie_type
                with open("movielist.json", "w", encoding="utf-8") as json_dosyasi:
                    json.dump(saved_movies, json_dosyasi, ensure_ascii=False, indent=4)
                movie_found=True

    print(saved_movies)
    if not movie_found:
        print("Aradiginiz Film Bulunamadi")

if user == "4":
    print("Uygulamanizda bulunan filmler: ")
    
    for movie in saved_movies:
        
        print(f"Film Adi:{movie['movie_name']}, Filmin Yonetmeni:{movie['movie_director_name']}, Filmin Turu:{movie['movie_type']}, Filmin yayin yili:{movie['movie_year']}")



#Question 3 

cust={
    1:{'name': 'Ford',
    'sirname': 'Mustang',
    'email': "for@mustang",
    'phone':123445},
    2:{'name': 'reno',
    'sirname': 'euorpe',
    'email': "reno@euora",
    'phone':3445454}
}
lst=["First name:","Sirname:","Email:","Phone number:"]
key_word=["name","sirname","email","phone"]
nex=2
while True:
    print("1-Add new customer")
    print("2-Update customer")
    print("3-Delete the customer")
    print("4-List all the customers")
    print("5-Logout\n")

    choose=int(input("which operation would like to do?:"))

    if 0<choose<6:
        match choose:
            case 1:
                
                request=[]

                

                for item in lst:
                    request.append(input(f"{item}"))
                
                nex+=nex
                cust[nex]={}
                for index, item in enumerate(key_word):
                    cust[nex][item]=request[index]
                print("\nNew customer added.\n\n\n")
                
            case 2:
                keep_going=True
                while keep_going:
                    cust_id=int(input("Enter the customer ID:"))
                    
                    if 0<cust_id<=len(cust):
                        request=[]

                        for item in lst:
                            request.append(input(f"{item}"))
                        
                        
                        for index, item in enumerate(key_word):
                            cust[cust_id][item]=request[index]
                        print(f"\nCustomerID {cust_id} updated\n\n")
                        break



                    else:
                        print("Invalid Customer id\n")
                        while True:
                            exit=input("Do you want to exit (Y/N):\n").lower()
                            if exit=="y":
                                keep_going=False
                                break
                                
                            elif exit=="n":
                                
                                break
                            else:
                                print("Wrong choice")
                            

            case 3:
                del_id=int(input("Please enter the id of Customer:"))

                
                get_id = cust.pop(del_id, "None")

                if get_id=="None":
                    print("\nWrong ID number\n")
                else:
                    print(f"\nCustomer ID number {del_id} deleted\n")
    
            case 4:
                if len(cust)>0:
                    for i in range(1,len(cust)+1):
                        
                        print("-"*30)
                        print(f"Cusmoter ID:{i}\nCustomer name:{cust[i]["name"]}\nCustomer Sirname:{cust[i]["sirname"]}\nEmail:{cust[i]["email"]}\nPhone:{cust[i]["phone"]}\n")
                    
                
                else:
                    print("Customer list is empty")
            case 5:
                break



    else:
        print("invalid choose")
