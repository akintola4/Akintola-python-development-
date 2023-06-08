##variable in python is case sensitive
##variable name must start with a letter or the underscore character
##variable name cannot start with a number
##variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
##variable names are case-sensitive (age, Age and AGE are three different variables)
##variable names should not be reused

##  Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

## Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

##mutiple variable
x, y, z = "Orange", "Banana", "Cherry"

##print variable
print(x)    #Orange


##Multi Words Variable Names
##Variable names with more than one word can be difficult to read.
##There are several techniques you can use to make them more readable:
##Camel Case
##Each word, except the first, starts with a capital letter:
myVariableName = "John"
##Pascal Case
##Each word starts with a capital letter:
MyVariableName = "John" 
##Snake Case
##Each word is separated by an underscore character:
my_variable_name = "John"

##global variable
##create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
##output: Python is awesome

##create a variable inside a function, with the same name as the global variable
x = "awesome" 
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
##output: Python is fantastic


##The global Keyword
##Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
##To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x = "amazing"
myfunc()
print("Python is " + x)
##output: Python is amazing

