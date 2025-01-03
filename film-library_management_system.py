# ENG // Question 2: Film Library Management System Project
# Project Description: This project aims to create an application that will help the user manage their movie collection. Users can add, edit, delete movies and view their collection.
# Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)
# Basic Functions:
# 1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.
# 2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)
# 3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.
# 4-Save the movie data in a file and restore this data when you start the program.


#TR//Soru 2: Film Kütüphanesi Yönetim Sistemi Projesi
# Proje Açıklaması: Bu proje, kullanıcının film koleksiyonunu yönetmesine yardımcı olacak bir uygulama oluşturmayı amaçlamaktadır. Kullanıcılar film ekleyebilir, düzenleyebilir, silebilir ve koleksiyonlarını görüntüleyebilir.
# Kullanılan Veri Yapıları: Sözlükler (filmleri ve ilgili bilgileri depolamak için), listeler (film koleksiyonunu görüntülemek için)
# Temel Fonksiyonlar:
# 1-Kullanıcıdan film adı, yönetmeni, yayın yılı, türü gibi bilgileri alarak bir film verisi oluşturun ve bir sözlükte saklayın.
# 2-Kullanıcıya filmi düzenleme veya silme seçeneği verin. (Bunun için, film hakkında değiştirmek istedikleri veriler ne olursa olsun, buna uygun bir fonksiyon yazılmalıdır.)
# 3-Kullanıcının koleksiyonunu görüntülemesine izin verin. Tüm filmleri listeleyin veya tür veya yayın yılı gibi kriterlere göre filtreleyin.
# 4-Film verilerini bir dosyaya kaydedin ve programı başlattığınızda bu verileri geri yükleyin.


#bos bir list olusturdum.
#dictionary = { "key": value}

films = [
    {"name": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "genre": "Drama"},
    {"name": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "genre": "Crime, Drama"},
    {"name": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action, Crime, Drama"},
    {"name": "Forrest Gump", "director": "Robert Zemeckis", "year": 1994, "genre": "Drama, Romance"},
    {"name": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson", "year": 2003, "genre": "Action, Adventure, Fantasy"},
    {"name": "Schindler's List", "director": "Steven Spielberg", "year": 1993, "genre": "Biography, Drama, History"},
    {"name": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994, "genre": "Crime, Drama"},
    {"name": "The Good, the Bad and the Ugly", "director": "Sergio Leone", "year": 1966, "genre": "Western"},
    {"name": "Fight Club", "director": "David Fincher", "year": 1999, "genre": "Drama"},
    {"name": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "year": 1999, "genre": "Action, Sci-Fi"},
    {"name": "Inception", "director": "Christopher Nolan", "year": 2010, "genre": "Action, Adventure, Sci-Fi"},
    {"name": "Star Wars: Episode V - The Empire Strikes Back", "director": "Irvin Kershner", "year": 1980, "genre": "Action, Adventure, Fantasy"},
    {"name": "Titanic", "director": "James Cameron", "year": 1997, "genre": "Drama, Romance"},
    {"name": "The Silence of the Lambs", "director": "Jonathan Demme", "year": 1991, "genre": "Crime, Drama, Thriller"},
    {"name": "Avengers: Infinity War", "director": "Anthony Russo, Joe Russo", "year": 2018, "genre": "Action, Adventure, Sci-Fi"}
]



def add_film():
    name_ofthe_film = input("Enter the name of the film")
    director_ofthe_film = input("Enter the director of the film")
    year_ofthe_film = input("Enter the year of the film")
    genre_ofthe_film = input("Enter the genre of the film")
    films.append({
        "name": name_ofthe_film,
        "director": director_ofthe_film,
        "year": year_ofthe_film,
        "genre": genre_ofthe_film
        })


def get_films():
    for index, film in enumerate(films, 1):
        print(f"{index}, Name: {film['name']}, Director: {film['director']}, Year: {film['year']}, Genre: {film['genre']}")
#enumerate
# Python'da enumerate, bir iterable (örneğin bir liste veya tuple) üzerinde döngü yaparken, her elemanla birlikte o elemanın indeksini (sırasını) de elde etmenizi sağlar. Bu, özellikle bir döngüde hem elemanlara hem de indekslere ihtiyaç duyduğunuz durumlarda oldukça kullanışlıdır.

# Sözdizimi
# enumerate(iterable, start=0)
# iterable: Üzerinde döngü yapılacak veri (örneğin liste, tuple, string).
# start: İndeksin başlayacağı sayı (varsayılan 0’dır).

#2//enumerate Olmadan Nasıl Yapılırdı?

# Eğer enumerate kullanmazsanız, bir döngü içinde indeksleri ayrı bir şekilde elde etmeniz gerekirdi:
        # def get_films():
            # for i in range(len(films)):  # range(len(films)) ile indeksleri alıyoruz
                # film = films[i]  # İlgili indeksin film sözlüğünü alıyoruz
                # print(f"{i + 1}. Name: {film['name']}, Director: {film['director']}, Year: {film['year']}, Genre: {film['genre']}")
# Bu da aynı sonucu üretir, ancak enumerate kullanmak daha okunabilir ve Pythonic bir çözümdür.

def find_film():
    wanted_film = input("Enter the movie name you want to search: ").lower()
    found_films = [film for film in films if wanted_film.lower() in film ['name'].lower()]

    if found_films:
        for film in found_films:
           print(f"Name: {film['name']}, Director: {film['director']}, Year: {film['year']}, Genre: {film['genre']}")
    else:
        print("The film you are looking for could not be found.")

def delete_film():
    name_to_delete = input("Enter the name of the film you want to delete: ").lower()
    found = False
    for film in films:
        if film["name"].lower() == name_to_delete:
            films.remove(film)
            print(f"The film '{film['name']}' has been deleted.")
            found = True
            break  # İlk bulduğu filmi silip döngüyü sonlandırır
    if not found:
        print("The film you want to delete was not found.")


#menu    
while True:
    print("\nFilm library menu\n")
    print("1 - Add film")
    print("2 - List films")
    print("3 - Search for a film")
    print("4 - Delete a film")
    print("5 - Exit\n")

    selected = input("select the operation you want to perform(1/2/3/4/5): ")
    if selected == "1":
        add_film()
    elif selected == "2":
        get_films()
    elif selected == "3":
        find_film()
    elif selected == "4":
        delete_film()
    elif selected == "5":
        print("leaving the library...")
        break
    else:
        print("you made an invalid choice ")
