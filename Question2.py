#1)Create a movie
def create_movie():
    name = input("Enter movie name: ")
    director = input("Enter director: ")
    year = input("Enter release year: ")
    genre = input("Enter genre: ")

    movie = {              #create a dictionary
        "name": name,      #"name" is the key, and the movie name is its value
        "director": director, 
        "year": year,
        "genre": genre
    }
    return movie

#2)Edit or delete a movie
def edit_movie(movie):
    print("Editing movie:", movie["name"])
    fields = {"1":"name", "2":"director", "3": "year", "4": "genre"} #fields is a dictionary that maps user choices (like "1") to the keys in the movie dictionary (like "name")

    print("1. Name\n2. Director\n3. Year\n4. Genre")     #print("1. Name")
                                                         #print("2. Director")
                                                         #print("3. Year")
                                                         #print("4. Genre")
    choice = input("What do you want to edit? (1-4): ")

    if choice in fields:
        new_value = input(f"Enter new {fields[choice]}: ")
        movie[fields[choice]] = new_value
    else:
        print("Invalid choice.")

    return movie

def delete_movie(collection, name):
    for movie in collection:         #goes through the list of movies
        if movie ["name"].lower() == name.lower():     #if the name matches, it removes the movie from the list 
            collection.remove(movie)                   #use .lower() to make sure it matches even if the user uses different capital letters
            print("Movie deleted.")
            return
    print("Movie not found")

#3)Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.
def view_movies(collection):
    print("1. View all\n2. Filter by genre\n3. Filter by year" )
    choice = input("Choose an option: ")

    if choice == '1':
        for movie in collection:
            print(movie)
    elif choice == '2':
        genre = input("Enter genre: ")
        for movie in collection:
            if movie["genre"].lower() == genre.lower():
                print(movie)
    elif choice == '3':
        year = input("Enter year: ")
        for movie in collection:
            if movie["year"] == year:
                print(movie)
    else:
        print("Invalid option.")

#4-Save the movie data in a file and restore this data when you start the program.
import json

def save_to_file(collection, filename="movies.json"):
    with open(filename, "w") as f:
        json.dump(collection, f)

def load_from_file(filename="movies.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def main():
    movies = load_from_file()

    while True:
        print("\n1. Add movie\n2. Edit movie\n3. Delete movie\n4. View collection\n5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            movie = create_movie()
            movies.append(movie)
        elif choice == '2':
            name = input("Enter the movie name to edit: ")
            for m in movies:
                if m["name"].lower() == name.lower():
                    edit_movie(m)
                    break
            else:
                print("Movie not found.")
        elif choice == '3':
            name = input("Enter the movie name to delete: ")
            delete_movie(movies, name)
        elif choice == '4':
            view_movies(movies)
        elif choice == '5':
            save_to_file(movies)
            print("Collection saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
