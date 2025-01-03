#Project Description: This project aims to create an application that will help the user manage their movie collection.
#  Users can add, edit, delete movies and view their collection.

#Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

# 1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

def create_movie_list():
    movie ={}

    for i in range(10):
        movie_name = input(f"{i+1}, Enter a nameof Movie :")
        movie_year = int(input("Enter Year of Release :"))
        director = input("Enter a director of Movie :")
        movie_genre = input("Enter a Genre of Movie :")

        movie_data ={
            "Movie Name" : movie_name,
            "Movie Year" : movie_year,
            "Director" : director,
            "Movie Genre" : movie_genre  

        }

        movie.append(movie_data)  
    return movie

movie_list = create_movie_list()
print(movie_list)

#[
# {'Movie Name': 'The Lord of The Rings - The Fellowship of the Rings', 'Movie Year': 2001, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'},
# {'Movie Name': 'The Lord of The Rings - The Two Towers', 'Movie Year': 2002, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'},
# {'Movie Name': 'The Lord of The Rings - The Return of the King', 'Movie Year': 2003, 'Director': 'Adventure', 'Movie Genre': 'Adventure'},
# {'Movie Name': 'Hobbit', 'Movie Year': 2012, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'},
# {'Movie Name': 'Kingdom of Heaven', 'Movie Year': 2005, 'Director': 'Ridley Schott', 'Movie Genre': 'Action-History-War'},
# {'Movie Name': 'The Green Mile', 'Movie Year': 1999, 'Director': 'Frank Darabont', 'Movie Genre': 'Dram-Fantastic'},
# {'Movie Name': 'Saving Private Ryan', 'Movie Year': 1998, 'Director': 'Steven Spielberg', 'Movie Genre': 'History-War'},
# {'Movie Name': 'Harry Potter and the Prisoner of Azkaban', 'Movie Year': 2004, 'Director': 'Alfonso Cuaron', 'Movie Genre': 'Fantastic-Adventure'},
# {'Movie Name': 'The Curious Case of Benjamin Button', 'Movie Year': 2008, 'Director': 'David Fincher', 'Movie Genre': 'Dram'},
# {'Movie Name': 'Pearl Harbor', 'Movie Year': 2001, 'Director': 'Michael Bay', 'Movie Genre': 'War-Drama'}
#]
film_sozlugu ={}
def film_ekle(film_adı, yil, tur, puan):
    film_sozlugu[film_adı] = {"yil": yil, "tur": tur, "puan": puan}

film_ekle("Kabadayi", 2015, "gerilim", 7.1)
print(film_sozlugu)

#******************************************************************
#2- Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)
movie_list = {
    "Inception": {
        "Movie Name": "Inception",
        "Movie Year": 2010,
        "Director": "Christopher Nolan",
        "Movie Genre": "Sci-Fi"
    },
    "Avatar": {
        "Movie Name": "Avatar",
        "Movie Year": 2009,
        "Director": "James Cameron",
        "Movie Genre": "Adventure"
    }
}



def del_movie(movie_name):
    if movie_name in movie_list:
        del movie_list[movie_name]

def edit_movie(movie_name, new_movie_name= None, new_year=None, new_director=None, new_genre=None):
    if movie_name in movie_list:
        if new_movie_name:
            movie_list[movie_name]["Movie Name" ] = new_movie_name
        
        if new_year:
             movie_list[movie_name]["Movie Year" ] = new_year

        if new_director:
             movie_list[movie_name]["Director" ] = new_director

        if new_year:
             movie_list[movie_name]["Movie Genre" ] = new_genre

edit_movie("Avatar", new_movie_name="Avatar: Special Edition") # fonk calistimak icin
edit_movie("Inception", new_year=2012, new_genre="Thriller")     # fonk calistimak icin

#************************************************************************************************
#3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

movie_liste = {
    'The Lord of The Rings - The Fellowship of the Rings': {
        'Movie Year': 2001,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Two Towers': {
        'Movie Year': 2002,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Return of the King': {
        'Movie Year': 2003,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'Kingdom of Heaven': {
        'Movie Year': 2005,
        'Director': 'Ridley Scott',
        'Movie Genre': 'Action-History-War'
    },
    'The Green Mile': {
        'Movie Year': 1999,
        'Director': 'Frank Darabont',
        'Movie Genre': 'Drama-Fantasy'
    },
    'Saving Private Ryan': {
        'Movie Year': 1998,
        'Director': 'Steven Spielberg',
        'Movie Genre': 'History-War'
    },
    'Harry Potter and the Prisoner of Azkaban': {
        'Movie Year': 2004,
        'Director': 'Alfonso Cuaron',
        'Movie Genre': 'Fantasy-Adventure'
    },
    'The Curious Case of Benjamin Button': {
        'Movie Year': 2008,
        'Director': 'David Fincher',
        'Movie Genre': 'Drama'
    },
    'Pearl Harbor': {
        'Movie Year': 2001,
        'Director': 'Michael Bay',
        'Movie Genre': 'War-Drama'
    }
}

def filter_movie(movie_liste, criteria, value):
    result =[]
    for movie, values in movie_liste.items():
        if criteria == "Movie Year" and values["Movie Year"] == value:          # İlk döngüde: film = "Inception", detaylar = {"yil": 2010, "tur": "Bilim Kurgu", "puan": 8.8}
            result.append(movie)
        if criteria == "Movie Year" and values["Movie Year"] == value:
            result.append((movie, values))
        if criteria == "Movie Genre" and values["Movie Genre"] == value:
            result.append((movie, values))

    return result

                 #filter_movie(movie_liste,   criteria,      value)  
filtered_movies = filter_movie(movie_liste, "Movie Genre", "Adventure") 
print(filtered_movies)

#[('The Lord of The Rings - The Fellowship of the Rings', {'Movie Year': 2001, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'}),
# ('The Lord of The Rings - The Two Towers', {'Movie Year': 2002, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'}),
# ('The Lord of The Rings - The Return of the King', {'Movie Year': 2003, 'Director': 'Peter Jackson', 'Movie Genre': 'Adventure'})]

#4-Save the movie data in a file and restore this data when you start the program.
import json
movie_liste = {
    'The Lord of The Rings - The Fellowship of the Rings': {
        'Movie Year': 2001,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Two Towers': {
        'Movie Year': 2002,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'The Lord of The Rings - The Return of the King': {
        'Movie Year': 2003,
        'Director': 'Peter Jackson',
        'Movie Genre': 'Adventure'
    },
    'Kingdom of Heaven': {
        'Movie Year': 2005,
        'Director': 'Ridley Scott',
        'Movie Genre': 'Action-History-War'
    },
    'The Green Mile': {
        'Movie Year': 1999,
        'Director': 'Frank Darabont',
        'Movie Genre': 'Drama-Fantasy'
    },
    'Saving Private Ryan': {
        'Movie Year': 1998,
        'Director': 'Steven Spielberg',
        'Movie Genre': 'History-War'
    },
    'Harry Potter and the Prisoner of Azkaban': {
        'Movie Year': 2004,
        'Director': 'Alfonso Cuaron',
        'Movie Genre': 'Fantasy-Adventure'
    },
    'The Curious Case of Benjamin Button': {
        'Movie Year': 2008,
        'Director': 'David Fincher',
        'Movie Genre': 'Drama'
    },
    'Pearl Harbor': {
        'Movie Year': 2001,
        'Director': 'Michael Bay',
        'Movie Genre': 'War-Drama'
    }
}
with open("c:/Users/harri/Desktop/Python_Modul_Week_2/team_1/yasin/my_dictionary.json", "w") as file:
    json.dump(movie_liste, file, indent=4)
