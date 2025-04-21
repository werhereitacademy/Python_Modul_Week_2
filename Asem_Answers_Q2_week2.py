
# 1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.
movies = {}
i = 1 
while True:
    movie_name= input('Enter the name of the movie:')
    director = input('Enter the director name:')
    release_year =input('Enter the release year:')
    genre = input('Enter the genre of the movie:')
    exit = input('Do you want to enter an other movie?(Y/N)').strip().lower()
    movie = 'movie'+" "+ str(i)
    movies.update( {movie: {'Name':(movie_name), 'Director':(director),'Release year' : release_year,'Genre': genre}})
    i +=1
    if exit != "y" :
        break  
# for key , value  in movies.items() :
#     print(key, value)
# 2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

change_info = input('Do you want to delete a movie? or do you want to edite an information about a movie?(Press D foor delete /Press E foor edit )'). strip().lower()
if change_info == "d" : 
    del_movie_num = int(input ("Enter The movie number which you want to delete for exampel  (1) "))
    # print(len(movies))
    if del_movie_num > 0 and del_movie_num <= len(movies): 
        # print("In the if deleted")
        movie_to_del = "movie"+ ' ' +str(del_movie_num)
        # print(movie_to_del)
        movies.pop(movie_to_del)
        print("Movie number: ", del_movie_num, " is deleted !")
    else:
        print("Movie number: ", del_movie_num, " is not found !" )
elif change_info == "e" : 
    # Edit function
    edit_movie_num = int(input ("Enter The movie number which you want to edit for exampel  (1) "))
    if edit_movie_num > 0 and edit_movie_num <= len(movies): 
        # print("In the if deleted")
        movie_to_edit = "movie"+ ' ' +str(edit_movie_num)
        # print(movie_to_del)
        m_to_edit = movies.get(movie_to_edit)
        value_to_change = input("Which part of the movie do you want to change ? Enter: \n N for name \n D for director \n R for relese year \n G for genre \n").strip().lower()
        if value_to_change == "n" :
            new_name = input("Enter new movie name")
            movies[movie_to_edit]["Name"] = new_name
            print("Movie number: ", edit_movie_num, " is edited !")
        elif value_to_change == "d":
           new_dir = input("Enter new movie director")
           movies[movie_to_edit]['Director'] = new_dir
        elif value_to_change == "r": 
           new_relese = input ('Enter new movie relese year')
           movies[movie_to_edit]['Release year'] = new_relese
        elif value_to_change == "g":
            new_gemer = input("Enter new Gemer")
            movies[movie_to_edit]['Genre'] = new_gemer
        else:
            print("Sorry you did not enterd a correct letter")
    else:
        print("Movie number: ", edit_movie_num, " is not found !")
        
else:
    print("You have not entered D or E!")
print(movies)
    
# 3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

criterea_to_list = input("Enter the criteria to filter your dictionary?  Enter:\n D for director \n R for release year \n G for genre \n").strip().lower()

if criterea_to_list == "d" : 
    director_name = input ("Enter the name of the director: \n").strip().lower()
    i=1
    dir_list = []
    for i in range(1,len(movies)+1):
        movie = "movie " + str(i)
        if movies[movie]["Director"].lower() == director_name:
            dir_list.append(movies[movie])
    print("The list of movies: ", dir_list)
elif criterea_to_list == 'r' : 
    release_year = input("Enter the release year: \n").strip().lower()
    i = 1 
    release_list = []
    for i in range (1,len(movies)+1) : 
        movie = 'movie ' + str(i)
        if movies[movie]['Release year'].lower() == release_year :
            release_year.append(movies[movie])
    print ('The list of movies : ', release_list)
elif criterea_to_list == 'g' : 
    genre_name = input("Enter the Genre: \n").strip().lower()
    i = 1 
    genre_list = []
    for i in range (1,len(movies)+1) : 
        movie = 'movie ' + str(i)
        if movies[movie]['Genre'].lower() == genre_name :
            genre_list.append(movies[movie])
    print ('The list of movies : ', genre_list)
else:
    print(" You interd a rong filter criteria ")


# 4-Save the movie data in a file and restore this data when you start the program.
import json

print (movies)

print("Started writing dictionary to a file")
with open("movies.txt", "w") as fp:
    json.dump(movies, fp)  # encode dict into JSON
print("Done writing dict into .txt file")