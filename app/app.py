import os
import psycopg2
from flask import Flask
from flask import request

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


def getAll():
    res = {}
    conn = conn_to_db()
    cursor = conn.cursor()
    cursor.execute("select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films;")
    l = cursor.fetchall()
    movies = [m[0] for m in l]
    cursor.close()
    conn.close()
    return movies

def getByName(name):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where name ilike %s"
    cursor.execute(query,("%" + name +"%",))
    l = cursor.fetchall()
    movies = [m[0] for m in l]
    cursor.close()
    conn.close()
    return movies

def getByYear(year):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where year ilike %s"
    cursor.execute(query,("%" + year +"%",))
    l = cursor.fetchall()
    movies = [m[0] for m in l]
    cursor.close()
    conn.close()
    return movies

def getByDirector(director):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where director ilike %s"
    cursor.execute(query,("%" + director +"%",))
    l = cursor.fetchall()
    movies = [m[0] for m in l]
    cursor.close()
    conn.close()
    return movies

def updateMovies(data):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "INSERT INTO films (name,director,year,genres) VALUES(%s,%s,%s,%s)"
    cursor.execute(query,(data['Name'],data['Director'],data['Year'],data['Genres']))
    conn.commit()
    cursor.close()
    conn.close()

def getByGenre(genre):
    conn = conn_to_db()
    cursor = conn.cursor()
    query= "select to_json(json_build_object('Name',name,'Director',director,'Year',year,'Generes',genres)) as data from films where %s = ANY(genres)"
    cursor.execute(query,(genre,))
    l = cursor.fetchall()
    movies = [m[0] for m in l]
    cursor.close()
    conn.close()
    return movies


def validate(data):  #validate all of the fields in the  request data
    if ('Name' not in data)  or (data['Name'] == ''):
      return False
    if ('Director' not in data)  or (data['Director'] == ''):
       return False
    if ('Year' not in data)  or (data['Year'] == ''):
       return False
    if ('Genres' not in data)  or (data['Genres'] == ''):
       return False
    else: return True




app = Flask(__name__)

@app.route("/")
def get_AllMovies():
    movies = getAll()
    if movies == []:
        return  {"data": "No movies found"},400
    else:
        return movies,200
    
@app.route('/film/<string:name>',methods=['GET'])
def get_MovieByName(name):
    movies = getByName(name)
    print(name)
    if movies == []:
        return  {"data": "No movies found"},400
    else:
        return movies,200
    

@app.route('/director/<string:name>',methods=['GET'])
def get_MovieByDirector(name):
    movies = getByDirector(name)
    if movies == None:
      return  {"data": "No movies found"},400
    else:
        return movies,200
    
@app.route('/year/<string:year>',methods=['GET'])
def get_MovieByYear(year):
    movies = getByYear(year)
    if movies == None:
        return {"data": "No movies found"},400
    else:
        return movies,200
    
@app.route('/genre/<string:genre>',methods=['GET'])
def get_MovieByGenre(genre):
    movies = getByGenre(genre)
    if movies == None:
       return {"data": "No movies found"},400
    else:
        return movies,200
    
@app.route('/post/',methods=['POST'])
def add_Movie():
    data = request.json
    if validate(data):
      updateMovies(data)
      return data,200
    else:
      return  {"data": "Incorrect data provided"},400
    


@app.route('/hostname',methods=['GET'])
def hostname():
       return os.environ['HOSTNAME'],200