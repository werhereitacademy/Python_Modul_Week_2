import json


# Question 4: Restore the movie data when the program starts
try:
    with open("movies.json", "r") as file:
        movie_library = json.load(file)
except FileNotFoundError:
    movie_library = []





# Question 2: Delete a field from a movie
def delete_movie(movie):
    key_to_delete = input("Which field do you want to delete? (e.g., genre): ")
    if key_to_delete in movie:
        del movie[key_to_delete]
        print(f"{key_to_delete} was deleted.")
    else:
        print("That field does not exist.")

# Question 3: View the movie collection (all, by genre, or year)
def view_movies():
    choice = input("View all movies (all), by genre (genre), or by year (year)?: ")
    if choice == "all":
        for m in movie_library:
            print(m)
    elif choice == "genre":
        g = input("Enter genre: ")
        for m in movie_library:
            if "genre" in m and m["genre"].lower() == g.lower():
                print(m)
    elif choice == "year":
        y = input("Enter release year: ")
        for m in movie_library:
            if "Release year" in m and m["Release year"] == y:
                print(m)
    else:
        print("Invalid option.")

# Question 4: Save the movie data in a file
def save_to_file():
    with open("movies.json", "w") as file:
        json.dump(movie_library, file, indent=4)

# Question 1: Create a movie dictionary with user input
movie = {
    "Movie name": input("Enter Movie: "),
    "Release year": input("Enter release year: "),
    "genre": input("Enter genre: "),
    "director": input("Enter director: ")
}
movie_library.append(movie)
save_to_file()
print("First movie saved!")


while True:
    print("\n Movie Library Menu:")
    print("1. Add another movie")
    print("2. View movies")
    print("3. Delete a field from last added movie")
    print("4. Exit")

    action = input("Choose an option: ")

    if action == "1":
        new_movie = {
            "Movie name": input("Enter Movie: "),
            "Release year": input("Enter release year: "),
            "genre": input("Enter genre: "),
            "director": input("Enter director: ")
        }


        movie_library.append(new_movie)
        print("Movie added!")
        save_to_file()

    elif action == "2":
        view_movies()

    elif action == "3":
        if movie_library:
            delete_movie(movie_library[-1])
            save_to_file()
        else:
            print("No movie to delete from.")

    elif action == "4":
        print("Goodbye!")
        save_to_file()
        break

    else:
        print("Invalid selection. Try again.")