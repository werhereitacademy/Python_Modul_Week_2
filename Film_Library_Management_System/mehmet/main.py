# edit_delete_movie.py

def edit_movie(movies):
    name = input("Duzenlemek istediginiz filmin adini girin: ")

    if name in movies:
        print("Ne degistirmek istersiniz?")
        print("1. Film adi")
        print("2. Yonetmen")
        print("3. Yayin yili")
        print("4. Tur")
        choice = input("Seciminiz (1-4): ")

        if choice == "1":
            new_name = input("Yeni film adini girin: ")
            movies[new_name] = movies[name]  # eski bilgiyi yeni adla kopyala
            del movies[name]  # eski filmi sil
            print("Film adi guncellendi.")
        elif choice == "2":
            new_director = input("Yeni yonetmeni girin: ")
            movies[name]["director"] = new_director
            print("Yonetmen guncellendi.")
        elif choice == "3":
            new_year = input("Yeni yili girin: ")
            movies[name]["year"] = new_year
            print("Yil guncellendi.")
        elif choice == "4":
            new_genre = input("Yeni turu girin: ")
            movies[name]["genre"] = new_genre
            print("Tur guncellendi.")
        else:
            print("Gecersiz secim!")
    else:
        print("Film bulunamadi!")


def delete_movie(movies):
    name = input("Silmek istediginiz filmin adini girin: ")

    if name in movies:
        confirm = input(f"{name} filmini silmek istiyor musunuz? (e/h): ")
        if confirm.lower() == "e":
            del movies[name]
            print("Film silindi.")
        else:
            print("Silme iptal edildi.")
    else:
        print("Film bulunamadi!")
