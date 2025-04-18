
# Question 2: Film Library Management System Project
print("Question 2")
import json

# File to store the movie data
MOVIE_FILE = 'movies.json'

# Load movie data from file
def load_movies():
    name = input("Enter movie name: ")
    director = input("Enter director: ")
    year = input("Enter release year: ")
    genre = input("Enter genre: ")
    movie = {
        "name": name,
        "director": director,
        "release_year": year,
        "genre": genre
    }
    return movie

# Save movie data to file
def save_movies(movies):
    with open(MOVIE_FILE, 'w') as f:
        json.dump(movies, f, indent=4)

# Add a new movie
def add_movie(movies):
    name = input("Enter movie name: ").strip()
    if not name:
        print("Movie name cannot be empty.")
        return
    if name in movies:
        print("Movie already exists.")
        return
    director = input("Enter director: ").strip()
    year = input("Enter release year: ").strip()
    while not year.isdigit():
        year = input("Invalid year. Enter a valid release year: ").strip()
    genre = input("Enter genre: ").strip()

    movies[name] = {
        'director': director,
        'year': year,
        'genre': genre
    }
    print("Movie added.")

# Edit movie details
def edit_movie(movies):
    name = input("Enter movie name to edit: ").strip()
    if name not in movies:
        print("Movie not found.")
        return
    print("What do you want to edit?")
    print("1. Director")
    print("2. Release Year")
    print("3. Genre")
    choice = input("Choose (1-3): ").strip()
    if choice == '1':
        movies[name]['director'] = input("Enter new director: ").strip()
    elif choice == '2':
        year = input("Enter new release year: ").strip()
        while not year.isdigit():
            year = input("Invalid year. Enter a valid release year: ").strip()
        movies[name]['year'] = year
    elif choice == '3':
        movies[name]['genre'] = input("Enter new genre: ").strip()
    else:
        print("Invalid choice.")
        return
    print("Movie updated.")

# Delete a movie
def delete_movie(movies):
    name = input("Enter movie name to delete: ").strip()
    if name in movies:
        del movies[name]
        print("Movie deleted.")
    else:
        print("Movie not found.")

# View the movie collection
def view_movies(movies):
    print("1. View all movies")
    print("2. Filter by genre")
    print("3. Filter by release year")
    choice = input("Choose an option: ").strip()
    if choice == '1':
        if not movies:
            print("No movies in the library.")
        else:
            for name, details in movies.items():
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
    elif choice == '2':
        genre = input("Enter genre to filter: ").strip().lower()
        found = False
        for name, details in movies.items():
            if details['genre'].lower() == genre:
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
                found = True
        if not found:
            print("No movies found for that genre.")
    elif choice == '3':
        year = input("Enter release year to filter: ").strip()
        found = False
        for name, details in movies.items():
            if details['year'] == year:
                print(f"\nTitle: {name}")
                print(f"  Director: {details['director']}")
                print(f"  Year: {details['year']}")
                print(f"  Genre: {details['genre']}")
                found = True
        if not found:
            print("No movies found for that year.")
    else:
        print("Invalid choice.")

# Main menu
def main():
    movies = load_movies()
    while True:
        print("\n--- Movie Library Menu ---")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View Movies")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_movie(load_movies)
        elif choice == '2':
            edit_movie(movies)
        elif choice == '3':
            delete_movie(movies)
        elif choice == '4':
            view_movies(movies)
        elif choice == '5':
            save_movies(movies)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
main()