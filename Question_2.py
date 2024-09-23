
""" Question 2: Film Library Management System Project

Project Description: This project aims to create an application that will help the user manage their movie collection. Users can add, edit, delete movies and view their collection.

Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

Basic Functions:

1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

4-Save the movie data in a file and restore this data when you start the program.
    
# """


import os.path     # importing os module 
import json        # importing json module 

film={}
# film = {
#     "1":{'name': 'John', "Derector": "Tomas","Year":1980,"Genre" : "Trillend" },
#     "2":{'name': 'John', "Derector": "Tomas","Year":1981 ,"Genre" : "Animasyon" },
#     "3":{'name': 'John', "Derector": "Tomas","Year":1982 ,"Genre" : "Family" },
#     "4":{'name': 'John', "Derector": "Tomas","Year":1983 ,"Genre" : "Trillend" }
# }


file_name = "Film.json"  # It can also be ".txt"

fNumber = 0

#There is a nested dictionary structure here, each film is recorded under a number(from 1 to infinity), 
#That is, the first key number value is again the dictionary.

def addFilm(fName :str,fDerector: str ,fYear : int, fGenre :str) -> None:
   
   film[fNumber] = {
                    "Name" :fName,
                    "Derector":fDerector,
                    "Year" :fYear, 
                    "Genre" : fGenre 
                }
    
  
   print(F" Your film {fName} input has been made successfully.")
   uploodDictJsonFile()
   
   
   
   

def updateFilm(choise :int,fName :None,fDerector: None ,fYear : None, fGenre :None)-> None:
    
    if choise in film:

        if fName is not None:
            film[choise].update({"Name" : fName})
            #film[choise][fName] = fName
        if fDerector is not None :
            film[choise].update({"Derector" :fDerector})
        if fYear is not None :
            film[choise].update({"Year" :fYear})
        if fGenre is not None :
            film[choise].update({"Genre" :fGenre})

        print("An update has been made.")

        uploodDictJsonFile()  

def searchFilm(chose):
    if chose in film:
        print (F"{chose} was found {film[chose]}")
    else:
        print("Item not found.")


def displayFilm():
    for i in film:
        print (film[i])
    

def removeFilm(chose):
    if chose in film:
        del  film["chose"]
    else :
        print("Item not found.")

#This function converts the data in dictionary format to json file format.
def uploodDictJsonFile():          

    with open(file_name,"w") as f_json :
        json.dump(film,f_json,indent=4)



def checkJsonFile():
    
    if os.path.isfile(file_name):

        print("dosya mevcut.\n")

        with open(file_name,"r") as f_json:
            mydict = json.load(f_json)
        print(mydict)

    else:
        print("False, dosya mevcut değil.")
        with open("Film.json", "w",encoding = 'utf-8') as f_json:
            print("Dosya olusturuldu.\n")
            print("Filim ler sozlugumdeki veriler json dosyasina ekleniyor...\n")
            json.dump(film,f_json,indent=4)
            

    
"""When the program runs automatically, the first function that will open is our main menu."""

def mainFilmMenu():

    checkJsonFile()


    while True :


        print(
        """
    ---- Film Library Management System Project----
            
                1. Add    film 
                2. Update film
                3. Delete film
                4. Search film  
                5. list   film
                0. exit
            
        """
        )

        select = int(input("Please select the option you want to make between 1-5 :"))
        
        
        match select :
            
            case 1:
                print("Your choice is : (1) Film add \n")
                print("Please fill in the required information to add a movie.")
                
               
                global fNumber  # If we do not specify this variable as "global" we get an error.
                fNumber+=1  # Automatically generates film number

                #These are all film library input data.
                fName =input("Enter name of the film :")
                fDerector = input("Enter name of the filmdrector  :")
                fYear = input("Enter release year of the film  :")
                fGenre = input("Enter genre  of the film  :")
            
                addFilm(fName,fDerector,fYear,fGenre) #We call the add film function.


            case 2 :
                print("Your choice is : (2) Film update , Please enter your current information..")
                
                #If there is no movie in the entered number, the selection continues until the correct choice is made.
                while True:
                    
                    choise = int(input("Enter number of film you want to change :"))
                    
                    if choise in film:
                        print (F"{choise} number of film wil be update ")
                        fName =input("Enter name of the film :") or None
                        fDerector = input("Enter name of the filmdrector  :") or None
                        fYear = input("Enter release year of the film  :") or None
                        fGenre = input("Enter genre  of the film  :") or None

                        updateFilm(choise,fName,fDerector,fYear,fGenre)
                        
                        break    
                    
                    else :
                        filmList = film.keys()
                        print(filmList , "Enter one of the film numbers among them.")
                        
            case 3:
                choise = input("Enter jour film code (1 - 5)")
                removeFilm(choise)
            
            case 4 :
                choise = input("Enter jour film code :")
                searchFilm(choise)
            
            case 5 :
                displayFilm()

            case 0 :
               
               print(json.dumps(film, indent=4))
               break

            case _:

                print("Number not between 1 and 5 ") 



# It is required to run the specified function automatically when the program is run.
if __name__ == "__main__":
    mainFilmMenu()
