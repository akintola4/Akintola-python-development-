#function in python are defined using the def keyword
#function name is followed by parenthesis
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
#example
def  first():
    print("hello world")
    
#calling the function
    first()
#this will print hello world

#function can also take arguments
#arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#example
def hello(name):
    print("hello " + name)
hello("john")
#this will print hello john

#example
def my_function(fname):
  print(fname + " Refsnes")
  
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#this will print Emil Refsnes, Tobias Refsnes, Linus Refsnes


#function can also take multiple arguments
#multiple arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#example
def my_function(fname, lname):
  print(fname + " " + lname)
  my_function("Emil", "Refsnes")
#this will print Emil Refsnes

#function can also take arbitrary arguments
#arbitrary arguments are specified after * in the function definition.
#example
def my_function(*kids):
    print("The youngest child is " + kids[2])
    my_function("Emil", "Tobias", "Linus")
#this will print The youngest child is Linus

#keyword arguments
#keyword arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#example
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#this will print The youngest child is Linus


#function can also take arbitrary keyword arguments
#arbitrary keyword arguments are specified after ** in the function definition.

#example
def my_function(**kid):
  print("His last name is " + kid["lname"])
  my_function(fname = "Tobias", lname = "Refsnes")
#this will print His last name is Refsnes

#default parameter value
#If we call the function without argument, it uses the default value
#example
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
#this will print I am from Sweden, I am from India, I am from Norway

#passing a list as an argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#example    
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#this will print apple, banana, cherry

#return values
#To let a function return a value, use the return statement
#example
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#this will print 9, 25, 81
#you can also use return statement to exit a function

#pass statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
#example
def myfunction():
    pass
#this will not give an error

#recursion
#Python also accepts function recursion, which means a defined function can call itself.
#recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
#example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
#this will print 120
