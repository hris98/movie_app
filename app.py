
class Movie:
    def __init__(self,name,year,director):
        self.name = name
        self.year = year
        self.director = director

def getAll():
    print("All movies")

def getByName():
    print("Movie by name")

def getByYear():
    print("By year")

def getByDirector():
    print("By director")



print(" 1: List all Movies\n","2: Search movie by name\n","3: Search movie by release date\n","4: Search movie by director")
choice = int(input())
print(choice)