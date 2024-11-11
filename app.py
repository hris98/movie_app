import os
import csv
import re
import psycopg2
import json

class Movie:
    def __init__(self,name,year,director):
        self.name = name
        self.year = year
        self.director = director

def conn_to_db():
    conn = psycopg2.connect(
        dbname="movies",
        user="hris",
        password="superpassword",
        host="movie-db",
        port="5432"
    )
    return conn

def getAll():
    conn = conn_to_db()
    cursor = conn.cursor()
    cursor.execute("select to_json(json_build_object('Name',name,'Director',director,'Year',year)) as data from films;")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()
       

def getByName(name):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year)) as data from films where name ilike %s"
    cursor.execute(query,("%" + name +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()
              

def getByYear(year):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year)) as data from films where year ilike %s"
    cursor.execute(query,("%" + year +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()

def getByDirector(director):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year)) as data from films where director ilike %s"
    cursor.execute(query,("%" + director +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()

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



"""def conn_to_db():
    conn = psycopg2.connect(
        dbname="movies",
        user="hris",
        password="superpassword",
        host="movie-db",
        port="5432"
    )
    cursor = conn.cursor()
    movies = getAll()
    for movieId in movies:
      cursor.execute(""" 
                  # INSERT INTO films (name,director,year)
                 #  VALUES (%s, %s, %s);
                  # """, (movies[movieId]['name'] ,movies[movieId]['director'], movies[movieId]['year']))
      #conn.commit()


    #cursor.close()
    #conn.close()"""

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
   