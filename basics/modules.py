#a module is bascially a file containing a set of function to include in your application
#there a core python module, modules you can install using the pip package manager (including Django) as well as custom modules

#example
import datetime

from datetime import date

import time
from time import time
today = date.today()
#to get the current time
timestamp = time()
print(today)
print(timestamp)


#we can also import custom modules
#we can also create our own modules
#create a file with the .py extension
#created one called mymodule.py
#import the module
import mymodule
from mymodule import add
from mymodule import sub
#use the module
#here i am using the add function from the mymodule.py file
print(add(1,2))
#this will print 3

#here i am using the sub function from the mymodule.py file
print(sub(2,1))
#this will print 1

#module can contain functions, classes and variables
#we can also create a module that only contains variables
#example
#this is the personal_data.py file
import perosnal_data 
#then we import details from the file 
from perosnal_data import details
#we check if we imported the right data by printing the details
print(details)

#here i am using the name variable from the details.py file
#to print the firstname and lastname
#we had to use the details["firstname"] and details["lastname"] because we are using a dictionary
#and we are accessing the values using the keys

print(details["firstname"] + " " + details["lastname"])
#here we are printing the firstname and lastname

#we can also print out an list of items in a dictionary
#here we are printing the first 2 items in the list
#we had to use the details["achievements"] because we are using a dictionary
#and we are accessing the values using the keys
#we also had to use the [0:2] because we want to print the first 2 items in the list

print(details["achievements"])
#this will print ['Being a NASA astronaut', 'Won the Nobel prize']

#pip moduels
import camelcase

from camelcase import CamelCase
c = CamelCase()

#Hump is a method that takes an inputted string and turns it into camel case format.
print(c.hump("hello i am tope akintola"))


#we can also use a custom module 
#we are going to import a module called validator
import validator
#then we import the function we want in validator.py
from validator import validate_email

# we create a custom user input to collect the email
email = input("Please enter your email: ")

if validate_email(email):
    print("email is vaild")
else:
    print("email is not vaild")
