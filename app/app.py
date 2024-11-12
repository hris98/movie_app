import os
import psycopg2
import json
import csv
import sys

POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_HOST = os.environ['POSTGRES_HOST']


class Movie:
    def __init__(self,name,year,director):
        self.name = name
        self.year = year
        self.director = director

def conn_to_db():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return conn

def getAllFromCsv():
    if os.path.exists("data.csv"):
        with open("data.csv","r") as filmsFile:
            reader = csv.DictReader(filmsFile,)
            l = list(reader)
            movies = {m["name"] : m for m in l }
            return movies

def getAll():
    conn = conn_to_db()
    cursor = conn.cursor()
    cursor.execute("select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films;")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()
       

def getByName(name):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where name ilike %s"
    cursor.execute(query,("%" + name +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()
              

def getByYear(year):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where year ilike %s"
    cursor.execute(query,("%" + year +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()

def getByDirector(director):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where director ilike %s"
    cursor.execute(query,("%" + director +"%",))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()

def updateMovies():
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "INSERT INTO films (name,director,year,genres) VALUES(%s,%s,%s,%s)"
    movies = getAllFromCsv()
    for movieID in movies:
      genres = { genre for genre in movies[movieID]['genres'].split('-')}
      cursor.execute(query,(movies[movieID]['name'],movies[movieID]['director'],movies[movieID]['year'],movies[movieID]['genres'].split('-')))
      conn.commit()
    cursor.close()
    conn.close()

def getByGenre(genre):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where %s = ANY(genres)"
    cursor.execute(query,(genre,))
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])
    cursor.close()
    conn.close()







print("\n 1: List all Movies\n","2: Search movie by name\n","3: Search movie by release date\n","4: Search movie by director\n","5: Update data file\n","6: Search by genre\n","7: Exit")
choice = int(sys.argv[1])

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
        updateMovies()

    case 6:
        genre = input("Search for movies by genre: ")
        getByGenre(genre)
    
    case 7:
         exit()
   