import os
import csv
import re

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
               print(movies[movieId]['name'], "Director: " + movies[movieId]['director'], "Release Date: " + movies[movieId]['year'],sep=" - ")
                

def getByName(name):
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            for movie in movies:
              if re.search(name, movie, re.IGNORECASE):
                print(movies[movie]['name'], "Director: " + movies[movie]['director'], "Release Date: " + movies[movie]['year'],sep=" - " )
              

def getByYear(year):
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            for movie in movies:
              if year in movies[movie]['year']:
                 print(movies[movie]['name'], "Director: " + movies[movie]['director'], "Release Date: " + movies[movie]['year'],sep=" - " )

def getByDirector(director):
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            for movie in movies:
              if re.search(director, movies[movie]['director'], re.IGNORECASE):
                print(movies[movie]['name'], "Director: " + movies[movie]['director'], "Release Date: " + movies[movie]['year'],sep=" - " )

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
   "Home Alone ": Movie("Home Alone","1990","Chris Columbus"),
   "Home Alone 2": Movie("Home Alone 2","1992","Chris Columbus"),
   "The Exorcist 3": Movie("The Exorcist 3","1990", "William Peter Blatty")
}

choice = 0

while choice != 6:

 print("\n 1: List all Movies\n","2: Search movie by name\n","3: Search movie by release date\n","4: Search movie by director\n","5: Update data file\n","6: To exit")
 choice = int(input())

 match choice:
    case 1:
        getAll()

    case 2:
        name = input("please type a movie name: ")
        getByName(name)

    case 3:
        year = input("Please type a year ")
        getByYear(year)

    case 4:
        director = input("Search for movies by director: ")
        getByDirector(director)

    case 5:
        updateMovies(movies)

    case 6:
        exit
   