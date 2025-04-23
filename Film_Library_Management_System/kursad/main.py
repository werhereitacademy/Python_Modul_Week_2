import json
import os
import keyboard

clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Dosya yolu: bu sayede 'main.py' ile aynı klasördeki 'movies.json' dosyasına erişilir
file_path = os.path.join(os.path.dirname(__file__), "movies.json")

# JSON verisini oku
with open(file_path, 'r', encoding="utf-8") as file:
    movies = json.load(file)

# JSON verisini güncelleme fonksiyonu
def update_movies_json(movies_dict, filename=file_path):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(movies_dict, file, indent=4, ensure_ascii=False)

def get_input(range, message="Lütfen bir işlem numarası giriniz:"):
    while True:
        try:
            sel = int(input(message))
            if sel in range:
                return sel
        except ValueError:
            print("lütfen gecerli bir deger giriniz")

def menu_header(menu_name):
    clear_screen()
    global menu_width
    menu_width = 30
    print(menu_width*'-')
    print(f"\033[1;33m"+ menu_name.center(menu_width)+f"\033[0m")
    print(menu_width*'-')

def show_main_menu():
    menu_name = "Movie Library"
    menu_header(menu_name)

    print("1 - Add movie")
    print("2 - Delete movie")
    print("3 - Edit movie")
    print("4 - View all movies")
    print("5 - Exit")
    print(menu_width*'-')

    selection = get_input(range(1,6))
    clear_screen()
    return selection

def select_movie(message):
    movie_list = []

    for index, movie in enumerate(movies):
        movie_list.append(movie)
        print(f"{index+1}. {movie}")

    print(menu_width*'-')
    selection = get_input(range(len(movies)+1), message )

    clear_screen()
    if selection != 0:
        return movie_list[selection-1]    
    else:
        return None


def show_movie_details(movie):
    menu_name = movie + " - Movie Details"
    menu_header(menu_name)

    print(f"Title\t\t: {movie}")
    print(f"Director\t: {movies[movie]['director']}")
    print(f"Release Year\t: {movies[movie]['release_year']}")
    print(f"Genre\t\t: {movies[movie]['genre']}")
    print(f"Lead Actor\t: {movies[movie]['lead_actor']}")

    print(menu_width*'-')

def change_details(movie):
    print(f"\n\nEditing movie: {movie}")
    info = movies[movie]
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print()
    
    director = input("Enter new value for director (press Enter to keep current value): ")
    if director: 
        info["director"] = director
    
    release_year = input("Enter new value for voor release year (press Enter to keep current value): ")
    if release_year:
        info["release_year"] = release_year
    genre = input("Enter the new value for the genre of the movie: ")
    if genre:
        info["genre"] = genre
    lead_actor = input("Enter the new value for the lead actor of the movie: ")
    if lead_actor:
        info["lead_actor"] = lead_actor
    update_movies_json(movies)
    print("Movie edited successfully!")
    input("Press Enter to continue...")


    
def delete_movie():
    menu_name = "Delete Movie"
    menu_header(menu_name)
    message = "Silmek istediğiniz filmin numarasını giriniz, vazgeçmek için 0'a basınsınız :"
    movie = select_movie(message)

    if movie != None:
        if input(f"\nAre you sure you want to delete ? (Y/N) : ").lower() == "y":
            del movies[movie]
            update_movies_json(movies)
            print("Movie deleted successfully!")
            input("Press Enter to continue...")

def edit_movie():
    menu_name = "Edit Movie"
    menu_header(menu_name)
    message = "Düzenlemek istediğiniz filmin numarasını giriniz, vazgeçmek için 0'a basınsınız :"
    movie = select_movie(message)
        
    if movie != None:
        show_movie_details(movie)
        change_details(movie)

def view_movies():
    menu_name = "View Movies"
    menu_header(menu_name)

    for movie in movies:
        show_movie_details(movie)
        input("Press Enter to continue...")

def get_new_movie():
    info = {}
    title = input("Movie name :  ")
    info["director"] = input("Director:  ")
    info["release_year"] = int(get_input(range(1900,2100),"Release Year:  "))
    info["genre"] = input("Genre:  ")
    info["lead_actor"] = input("Lead Actor:  ")

    return title, info

def add_movie():
    menu_name = "Add Movie"
    menu_header(menu_name)

    title, info = get_new_movie()
    movies[title] = info
    update_movies_json(movies)
    print("\nMovie added successfully!")
    input("Press Enter to continue...")

while True:
    selection = show_main_menu()
    if selection == 1:
        add_movie()
    elif selection == 2:
        delete_movie()
    elif selection == 3:
        edit_movie()
    elif selection == 4:
        view_movies()
    elif selection == 5:
        break






