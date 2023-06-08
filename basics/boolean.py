#boolean experssion is a value that is either true or false
print(True)
print(False)
print(type(True))
print(type(False))

#boolean experssion can be used to compare values
print(1 > 2)
#this prints out false because 1 is not greater than 2
print(1 < 2)
#this prints out true because 1 is less than 2
print(1 == 1)
#this prints out true because 1 is equal to 1
print(1 != 1)
#this prints out false because 1 is not equal to 1
print(1 >= 1)
#this prints out true because 1 is greater than or equal to 1
print(1 <= 1)
#this prints out true because 1 is less than or equal to 1

#evaluate values
#boolean experssion can be used to evaluate values
print(bool('hello'))
#this prints out true because the string is not empty
print(bool(15))
#this prints out true because the number is not zero

#evaluate variables
#boolean experssion can be used to evaluate variables
x = 'hello'
y = 15
print(bool(x))
#this prints out true because the string is not empty
print(bool(y))
#this prints out true because the number is not zero
#if you want to check if a variable is empty, you can use the len function
z = ''
print(bool(z))
#this prints out false because the string is empty
print(len(z))
#this prints out 0 because the string is empty

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#The following will return True:
bool(1)
bool("abc")
bool([1,2,3])
bool({"a":1})
bool({"name": "John"})


#isinstamce() function
#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
print(isinstance("fola", str))
#this prints out true because the variable x is a string
print(isinstance(10, int))

#this prints out true because the variable y is an integer
print(isinstance(10, str))
#this prints out false because the variable z is not a string


#when working with  boolean experssion 
#i check to see if the requirement for honour roll are met
gpa = float(input('what is your garde point average? '))
lowest_grade = float(input('what is your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

#later in your code if you want to check if the student is
#on honour rool, all i need to do is use the variable to check the boolean variable
#i set earlier in my code
if honour_roll:
    print('you made honour roll')