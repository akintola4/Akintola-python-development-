#json is commonly used with data APIS 
#we can parse json into a python dictionary
#we need to import the json module
import json

#we can create a custom json
UserJson = '{"first_name": "Fola", "last_name": "akintola"}'

#we then parse it into a dict
user = json.loads(UserJson)
print(user) 
#this will print out all the data in user

#let say we want to print a specfic part of the data
print(user["last_name"])

#lets convert a dictionary to a json 
#lets create a custom dict
cars = {
    "car_1": "ford",
    "car_2": "benz",
    "car_3": "tesla"
}

#we use .dumps to create a json  
carJson = json.dumps(cars)
#we can then print out the new json we created 
print(carJson)
#note json is in double quotes and dict is in single quotes 