import os
import csv

class Movie:
    def __init__(self,name,year,director):
        self.name = name
        self.year = year
        self.director = director

def getAll():
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            for movieId in movies:
               print(movies[movieId])
                

def getByName(name):
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            if name in movies:
             print(movies[name])
            else: print("No results")

def getByYear():
    print("By year")

def getByDirector():
    print("By director")

def updateMovies(movies):
    fields = ['name','year','director']
    with open ("data.csv","w", newline='') as movieFile:
        writer = csv.writer(movieFile)
        writer.writerow(fields)
        for movieID in movies:
            movie = movies[movieID]
            writer.writerow([movie.name, movie.year , movie.director])


movies = {
   "The Exorcist": Movie("The Exorcist","1973","William Friedkin"),
   "Hereditary": Movie("Hereditary","2018","Ari Aster"),
   "A Nightmare on Elm Street": Movie("A Nightmare on Elm Street","1984","Wes Craven"), 
}

print(" 1: List all Movies\n","2: Search movie by name\n","3: Search movie by release date\n","4: Search movie by director\n","5: To exit")
choice = int(input())

match choice:
    case 1:
        getAll()

    case 2:
        name = input("please type a movie name: ")
        getByName(name)

    case 3:
        getByYear()

    case 4:
        getByDirector()

    case 5:
        exit
   