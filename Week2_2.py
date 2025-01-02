"""
Question 2: Film Library Management System Project
Project Description: This project aims to create an application that will help the user manage their movie collection. Users can add, edit, delete movies and view their collection.

Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

Basic Functions:

1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

4-Save the movie data in a file and restore this data when you start the program.
"""
import os
import json

def save_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # print(f"Data was successfully written to file: {file_path}")
    except Exception as e:
        print(f"Error: Data could not be written to file. Details: {e}")

def load_file(file_path):
    """
    Reads a list from a file in JSON format.
    """
    if not os.path.exists(file_path):
        save_file(file_path, [])
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON format is invalid.")
        return []
    except Exception as e:
        print(f"Error: File could not be read. Details: {e}")
        return []    

# Main program
if __name__ == "__main__":
    movies_file = "movies.txt"
    movie_keys_file = "movie_keys.txt"
    # if not os.path.exists(movies_file):
    #     save_file(movies_file, [])
    # if not os.path.exists(movie_keys_file):
    #     save_file(movie_keys_file, [])
    movies= load_file(movies_file)
    movie_keys = load_file(movie_keys_file)
    incorrectly_entered = False
    exit_confirmation = True
    while exit_confirmation:
        os.system("clear" if os.name == "posix" else "cls")
        main_menu = main_menu = [
                "_____________________________________________________",
                "              Film Library Management                ",
                "_____________________________________________________\n",
                "     (1) Movie Adding Procedures.\n",
                "     (2) Movie List.\n\n",
                "     (q) You can exit the program by pressing.\n\n"
        ]

        for i in main_menu:
            print(i)

        if incorrectly_entered:
            print('\t'.expandtabs(5), "You have entered incorrectly. Please check the menu and make your selection again!")
            incorrectly_entered = False

        print('\t'.expandtabs(5), "Please select the action you wish to perform:", end=" ")
        select_menu = input()

        if select_menu in ["q", "Q"]:
            exit_confirmation = False
        elif select_menu == "1":
            exit_submenu1 = True
            while exit_submenu1:
                os.system("clear" if os.name == "posix" else "cls")
                movie_id = 1
                for movie in movies:
                    print(movie_id,"\t".expandtabs(3), end="")
                    print(movie)
                    movie_id += 1
                main_menu = [
                        "_____________________________________________________",
                        "              Movie Adding Procedures.               ",
                        "_____________________________________________________\n",
                        "   (1) Adding a Movie.",
                        "   (2) Movie Correction.",
                        "   (3) Movie Deletion.",
                        "   (4) Edit movie info fields.\n",
                        "   (q) To return to the main menu.\n"
                ]
                for i in main_menu:
                    print(i)

                if incorrectly_entered:
                    print('\t'.expandtabs(5), "You have entered incorrectly. Please check the menu and make your selection again!")
                    incorrectly_entered = False

                print('\t'.expandtabs(5), "Please select the action you wish to perform:", end=" ")
                select_menu = input()
                if select_menu in ["q", "Q"]:
                    exit_submenu1 = False
                elif select_menu == "1":
                    movie = {}
                    for key in movie_keys:
                        movie[key] = input(f"Please enter the movie {key}: ")
                    if movie not in movies:
                        movies.append(movie)
                        save_file(movies_file, movies)
                        print("Movie added successfully.")
                        input("Press enter to continue...")
                    else:
                        print("This movie already exists.")
                        input("Press enter to continue...")
                elif select_menu == "2":
                    edit_movie_id = input("Please enter the movie ID you want to edit: ")
                    if edit_movie_id.isdigit():
                        edit_movie_id = int(edit_movie_id)
                    else:
                        edit_movie_id = -1
                    if edit_movie_id in range(1, len(movies)+1):
                        movie = movies[edit_movie_id-1]
                        for key in movie_keys:
                            movie[key] = input(f"Please enter the movie {key}: ")
                        movies[edit_movie_id-1] = movie
                        save_file(movies_file, movies)
                elif select_menu == "3":
                    delete_movie_id = input("Please enter the movie ID you want to delete: ")
                    if delete_movie_id.isdigit():
                        delete_movie_id = int(delete_movie_id)
                    else:
                        delete_movie_id = -1
                    if delete_movie_id in range(1, len(movies)+1):
                        if True if input("Are you sure you want to delete the movie? (Y/N): ") in ["y","Y"] else False:
                            del movies[delete_movie_id-1]
                            save_file(movies_file, movies)
                            print("Movie deleted successfully.")
                        else:
                            print("Movie deletion canceled.")
                            input("Press enter to continue...")
                elif select_menu == "4":
                    exit_submenu2 = True
                    while exit_submenu2:
                        os.system("clear" if os.name == "posix" else "cls")
                        index_key = 1
                        print('\t'.expandtabs(5),"ID-",'\t'.expandtabs(1), "Key")
                        for key in movie_keys:
                            print("\t".expandtabs(5),index_key,"- ","\t".expandtabs(1),key)
                            index_key += 1
                        main_menu = [
                        "_____________________________________________________",
                        "            Student Adding Procedures.               ",
                        "_____________________________________________________\n",
                        "   (1) Adding a Key.\n",
                        "   (2) Key Correction.\n",
                        "   (3) Key Deletion.\n",
                        "   (q) To return to the upper menu.\n\n"
                        ]
                        for i in main_menu:
                            print(i)
                        
                        if incorrectly_entered:
                            print('\t'.expandtabs(5), "You have entered incorrectly. Please check the menu and make your selection again!")
                            incorrectly_entered = False

                        print('\t'.expandtabs(5), "Please select the action you wish to perform:", end=" ")
                        select_menu = input()
                        if select_menu in ["q", "Q"]:
                            exit_submenu2 = False
                        elif select_menu == "1":
                            new_key = input("Please enter the new key: ")
                            if new_key not in movie_keys:
                                movie_keys.append(new_key)
                                save_file(movie_keys_file, movie_keys)
                                print("Key added successfully.")
                                input("Press enter to continue...")
                            else:
                                print("This key already exists.")
                                input("Press enter to continue...")
                        elif select_menu == "2":
                            select_key = input("Please enter the key ID you want to edit: ")
                            if select_key.isdigit():
                                select_key = int(select_key)
                            else:
                                select_key = -1
                            if select_key in range(1, len(movie_keys)+1):
                                new_key = input("Please enter the new key: ")
                                if new_key not in movie_keys:
                                    movie_keys[select_key-1] = new_key
                                    save_file(movie_keys_file, movie_keys)
                                    print("Key edited successfully.")
                                    input("Press enter to continue...")
                                else:
                                    print("This key already exists.")
                                    input("Press enter to continue...")
                            else:
                                print("Invalid key ID.")
                                input("Press enter to continue...")
                        elif select_menu == "3":
                            select_key = input("Please enter the key ID you want to delete: ")
                            if select_key.isdigit():
                                select_key = int(select_key)
                            else:
                                select_key = -1
                            if select_key in range(1, len(movie_keys)+1):
                                if True if input("Are you sure you want to delete the key? (Y/N): ") in ["y","Y"] else False:
                                    del_keys = movie_keys[select_key-1]
                                    del movie_keys[select_key-1]
                                    save_file(movie_keys_file, movie_keys)
                                    for movie in movies:
                                        del movie[del_keys]
                                    save_file(movies_file, movies)
                                    print("Key deleted successfully.")
                                    input("Press enter to continue...")
                                else:
                                    print("Key deletion canceled.")
                                    input("Press enter to continue...")
                            else:
                                print("Invalid key ID.")
                                input("Press enter to continue...")
                        else:
                            incorrectly_entered = True
                else:
                    incorrectly_entered = True
        elif select_menu == "2":
            print("Movie ID".center(16, " "), end="")
            for key in movie_keys:
               print(key.center(35, " "), end="")
            print()
            print("----------".center((len(movie_keys)*35+16), "-"))
            movie_id = 1
            for movie in movies:
                print(str(movie_id).center(16, " "), end="")
                for key in movie_keys:
                    print(movie[key].center(35, " "), end="")
                print()
                movie_id += 1
            input("\n\n\nPress enter to continue...") 
        else:
            incorrectly_entered = True
