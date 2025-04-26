#1-Create a movie data by taking information such as movie name, 
# director, release year and genre from the user and store it in a dictionary.
#2-Give the user the option to edit or delete a movie. 
# (For this, a suitable function must be written 
# for whatever data they want to change about the movie.)
#3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.
#4-Save the movie data in a file and restore this data when you start the program.
import json
import os

if os.path.exists("movied.json"):
    with open("movies.json", "r", encoding="utf-8") as dosya:
        movies = json.load(dosya)
else:
    movies = []

while True:

    choise = str(input("Chooise a menu:  ------------------\nDelete a movie:(D)\nChange a movie:(C) \nNew movie:(N) \nList :(L) ").upper())
    if choise == "N":

        while True:

            name = input("Give movie name:   ")
            year = int(input("Give the year of the movie:  ") if input("Give the year of the movie:  ").isdigit() else "2023")
            if year < 1900 or year > 2023:
                print("Please enter a valid year between 1900 and 2023.")
                continue
            #year = int(input("Give the year of the movie:  ") if input("Give the year of the movie:  ").isdigit() else "2023")
            director = input("Give director name:   ")
            genre = input("Give genre:   ")
            xname = {
            "name": name,
            "year": year,
            "director" : director,
            "genre" : genre
                    }
            
            movies.append(xname)
            print(movies)
            break

    elif choise == "C":
                
        xc = input("Give an info over the movie:    ")
        yc = input("Give new info:    ")
        for z in movies:
            if z["name"] == xc:
                z["name"] = yc
                print(movies)
            elif z["director"] == xc:
                z["director"] = yc
                print(movies)
            elif z["genre"] == xc:
                z["genre"] = yc
                print(movies)
            else:
                z["year"] = yc
                print(movies)
    
    elif choise == "L":
        choise = str(input("Chooise a sort:  \nName:(N)\nYear:(Y) \nGenre:(G) \nDırector :(D) ").upper())
        while True:
            if choise == "N":
                #for movie in movies if len(movies) > 0, print(movie for movie in movies if movie["name"]), print("list is empty")
                #print("".join(str(movie["name"]) for movie in movies) if len(movies) > 0 else "list is empty")
                print("".join(str(movie["name"]) for movie in movies) if len(movies) > 0 else "list is empty")
                break
            elif choise == "Y":
                print("".join(str(movie["year"]) for movie in movies) if len(movies) > 0 else "list is empty")
                #for movie in movies if len(movies) > 0, print(movie for movie in movies if movie["year"]), print("list is empty") 
                break
            elif choise == "G":
                #print("".join(str(movie["genre"]) for movie in movies) if len(movies) > 0 else "list is empty")
                #for movie in movies if len(movies) > 0, print(movie for movie in movies if movie["genre"]), print("list is empty")
                print("".join(str(movie["genre"]) for movie in movies) if len(movies) > 0 else "list is empty")
                break
            elif choise == "D":
                print("".join(str(movie["director"]) for movie in movies) if len(movies) > 0 else "list is empty")
                #for movie in movies if len(movies) > 0, print(movie for movie in movies if movie["director"]), print("list is empty")
                break
            elif choise == "Q":
                break
            else:
                print(f"{choise} is not defined.")
                break

    elif choise == "D":
        xm = input("Give an info over the movie:    ")
        for xm in movies:
            movies.remove(xm)
            print(movies)
        #movies = [movies for movies in movies if movies['name'] != 'Ayşe']

    else:
        print(movies)

with open("movies.json", "w", encoding="utf-8") as dosya:
    json.dump(movies, dosya, ensure_ascii=False, indent=2) 
     

