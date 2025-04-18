#Question 2
import json

# Function to create a movie entry
def create_movie():
    movie_name = input("Enter movie name: ")
    director = input("Enter director: ")
    release_year = input("Enter release year: ")
    genre = input("Enter genre: ")
    movie = {
        "name": movie_name,
        "director": director,
        "release_year": release_year,
        "genre": genre
    }
    return movie

# Function to edit a movie
def edit_movie(collection):
    name_to_edit = input("Enter the name of the movie to edit: ")
    for movie in collection:
        if movie["name"] == name_to_edit:
            print("Current details:", movie)
            movie["name"] = input("Enter new movie name (or press Enter to keep current): ") 
            movie["director"] = input("Enter new director (or press Enter to keep current): ") 
            movie["release_year"] = input("Enter new release year (or press Enter to keep current): ") 
            movie["genre"] = input("Enter new genre (or press Enter to keep current): ")
            print("Movie updated!")
        print("Movie not found.")

# Function to delete a movie
def delete_movie(collection):
    name_to_delete = input("Enter the name of the movie to delete: ")
    for movie in collection:
        if movie["name"] == name_to_delete:
            collection.remove(movie)
            print(f"Movie '{name_to_delete}' deleted!")
            
        print("Movie not found.")

# Function to view movies
def view_collection(collection):
    choice = input("View all movies or filter by genre/year? (all/genre/year): ").lower()
    if choice == "all":
        for movie in collection:
            print(movie)
    elif choice == "genre":
        genre = input("Enter genre to filter: ")
        filtered_movies = [movie for movie in collection if movie["genre"].lower() == genre.lower()]
        for movie in filtered_movies:
            print(movie)
    elif choice == "year":
        year = input("Enter year to filter: ")
        filtered_movies = [movie for movie in collection if movie["release_year"] == year]
        for movie in filtered_movies:
            print(movie)
    else:
        print("Invalid choice.")

# Function to save data to a file
def save_data(collection):
    with open("movies.json", "w") as file:
        json.dump(collection, file)
    print("Data saved successfully!")

# Function to load data from a file
def load_data():
    try:
        with open("movies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main program loop
def main():
    movie_collection = load_data()
    while True:
        print("\nFilm Library Management System")
        print("1. Add a movie")
        print("2. Edit a movie")
        print("3. Delete a movie")
        print("4. View collection")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            movie_collection.append(create_movie())
        elif choice == "2":
            edit_movie(movie_collection)
        elif choice == "3":
            delete_movie(movie_collection)
        elif choice == "4":
            view_collection(movie_collection)
        elif choice == "5":
            save_data(movie_collection)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
