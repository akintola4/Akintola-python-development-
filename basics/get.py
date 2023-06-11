#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


#example of a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
#this will print {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#example
x = thisdict["model"]
print(x)
#this will print Mustang

#Dictionaries cannot have two items with the same key
#example
movies = {
    "movie1": "The Godfather",
    "movie2": "The Shawshank Redemption",
    "movie3": "Schindler's List",
    "movie4": "Raging Bull",
    "movie4": "Raging Bull",
    "movie5": "Casablanca",
    "movie6": "Citizen Kane",
}
print(movies)
#this will print {'movie1': 'The Godfather', 'movie2': 'The Shawshank Redemption', 'movie3': 'Schindler\'s List', 'movie4': 'Raging Bull', 'movie5': 'Casablanca', 'movie6': 'Citizen Kane
#notice that the movie4 is repeated twice, but Python will only print one of them

#Dictionaries are mutable, meaning that we can change the value of a specific item after the dictionary has been created.
#dictionary can be of any data type

#the dist() constructor
#It is also possible to use the dict() constructor to make a dictionary
#example
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
#this will print {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.
#Method	Description
#clear()	Removes all the elements from the dictionary
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
animals.clear()
print(animals)
#this will print {}
#beacuse we cleared the dictionary

#copy()	Returns a copy of the dictionary
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
x = animals.copy()
print(x)
#this will print {'animal1': 'dog', 'animal2': 'cat', 'animal3': 'rabbit', 'animal4': 'hamster', 'animal5': 'goldfish'}

#fromkeys()	Returns a dictionary with the specified keys and value
#example
x = ('key1', 'key2', 'key3')
y = 0
new = dict.fromkeys(x, y)
print(new)
#this will print {'key1': 0, 'key2': 0, 'key3': 0}
#notice that the value is 0 for all the keys


#get()	Returns the value of the specified key
# example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}   
x = animals.get("animal3")
print(x)
#this will print rabbit
#notice that we didn't need to use the print() function


#items()	Returns a list containing a tuple for each key value pair
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
x = animals.items()
print(x)
#this will print dict_items([('animal1', 'dog'), ('animal2', 'cat'), ('animal3', 'rabbit'), ('animal4', 'hamster'), ('animal5', 'goldfish')])
#notice that the items are inside a tuple
#thats because the items() method returns a list containing a tuple for each key value pair

#keys()	Returns a list containing the dictionary's keys
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
x = animals.keys()
print(x)
#this will print dict_keys(['animal1', 'animal2', 'animal3', 'animal4', 'animal5'])
#notice that the keys are inside a list
#thats because the keys() method returns a list containing the dictionary's keys

#pop()	Removes the element with the specified key
#example    
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
animals.pop("animal3")
print(animals)
#this will print {'animal1': 'dog', 'animal2': 'cat', 'animal4': 'hamster', 'animal5': 'goldfish'}
#notice that the animal3 is removed

#popitem()	Removes the last inserted key-value pair
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
animals.popitem()   
print(animals)
#this will print {'animal1': 'dog', 'animal2': 'cat', 'animal3': 'rabbit', 'animal4': 'hamster'}
#notice that the last inserted key-value pair is removed
#notice that the popitem() method removes the last inserted key-value pair


#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#   example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
x = animals.setdefault("animal2", "hamster")
print(x)
#this will print cat
#notice that the value of the key is returned
#notice that the key already exists



#update()	Updates the dictionary with the specified key-value pairs
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
animals.update({"animal6": "tiger"})
print(animals)
#this will print {'animal1': 'dog', 'animal2': 'cat', 'animal3': 'rabbit', 'animal4': 'hamster', 'animal5': 'goldfish', 'animal6': 'tiger'}
#notice that the dictionary is updated with the specified key-value pair


#values()	Returns a list of all the values in the dictionary
#example
animals = {
    "animal1": "dog",
    "animal2": "cat",
    "animal3": "rabbit",
    "animal4": "hamster",
    "animal5": "goldfish",
}
x = animals.values()
print(x)
#this will print dict_values(['dog', 'cat', 'rabbit', 'hamster', 'goldfish'])
#notice that the values are inside a list
#thats because the values() method returns a list containing the dictionary's values
