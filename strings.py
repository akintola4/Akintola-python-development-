#strings
#strings are a sequence of characters, they can be enclosed in single quotes or double quotes
#strings are immutable, this means that once defined, they cannot be changed
#strings can be indexed, the first character in the string has the index 0
print('hello'[0])

#multiline strings
#multiline strings are enclosed in triple quotes
#multiline strings can span multiple lines
x = '''hello
world, i am tope akintola, 
i am a software developer,
i am a student at the state university of ondo state.'''
print(x)
#strings can be indexed with negative numbers
print('hello'[-1])

#strings can be concatenated with the + operator
print('hello' + 'world')

#strings can be repeated with the * operator
#repeated strings are concatenated

print('hello' * 3)
#strings can be sliced with the [start:stop:step] operator
#slice operator returns a string
print('hello'[0:3])
#this prints from the first character to the third character

print('hello'[:3])
#since the start is not specified, it prints from the first character to the third character

print('hello'[3:])
#since the stop is not specified, it prints from the third character to the last character

#negative indexes can be used to slice strings
print('hello'[-3:-1])
#this prints from the third character from the end to the second character from the end

#strings can be split with the split() method
#split() method returns a list
#split() method takes a separator as an argument
#split() method splits the string at the specified separator
#split() method splits the string into substrings
#split() method splits the string into a list
#split() method splits the string into a list of strings
#split() method splits the string into a list of substrings
print('hello world'.split(' '))
#this uses the space as the separator
print('hello world'.split())
#this uses the default separator


#strings can be joined with the join() method
#join() method returns a string
#join() method takes a list as an argument
#join() method joins the list elements with the specified separator
print(' '.join(['hello', 'world']))

#strings can be formatted with the format() method
#format() method returns a string   
#format() method takes positional arguments
#format() method takes keyword arguments
#format() method takes both positional and keyword arguments
#format() method takes an object as an argument
print('hello {} {}'.format('temitope', 'akintola'))
#the positional arguments are inserted into the curly braces in the order they are passed

#format method to insert numbers
print('the number is {}'.format(1))
#the number is 1

#format method to insert multiple numbers
print('the numbers are {}, {}, {}'.format(1, 2, 3))

#format method can take multiple arguments
print('the first name is {} and the last name is {}'.format('temitope', 'akintola'))

#format method can be used with indexes
print('brought a car called {1} and a house called {0} to the market'.format( 'duplex', 'superx'))
#the curly braces are used to insert the positional arguments
#the positional arguments are inserted in the order they are passed

#format method can be used with keywords
#strings can be formatted with f-strings
#strings can be formatted with the % operator
#strings can be formatted with the Template class
#strings can be formatted with the string modulo operator
#strings can be formatted with the format() method

#strings can be concatenated with the + operator
first_name = 'temitope'
last_name = 'akintola'

print(first_name + last_name)
print('hello,' + first_name + ' ' + last_name)

#strings are iterable
#strings can be looped over with the for loop
for i in 'hello':
    print(i)
    #this prints each character in the string on a new line
    
#strings length can be found with the len() function
#len() function returns an integer
#len() function takes a string as an argument
#len() function returns the number of characters in the string
print(len('hello'))
#this prints the length of the string

#checking if a string contains a substring
#the in operator returns a boolean
#the in operator returns True if the substring is in the string
#the in operator returns False if the substring is not in the string
print('hello' in 'hello world')

txt = 'the best things in life are free'
if 'free' in txt:
    print('yes, free is present')
else:
    print('no, free is not present')

#checking if a string contains a substring
#the not in operator returns a boolean
#the not in operator returns True if the substring is not in the string
#the not in operator returns False if the substring is in the string
print('hello' not in 'hello world')

#strings can be compared with the == operator
#the == operator returns a boolean
#the == operator returns True if the strings are equal
#the == operator returns False if the strings are not equal
print('hello' == 'hello')
#this prints True because the strings are equal
print('hello' == 'hello world')
#this prints False because the strings are not equal
print('hello' != 'hello world')
#this prints True because the strings are not equal
print('hello' != 'hello')
#this prints False because the strings are equal


#strings can be modified
#upper() method converts the string to uppercase
print('hello'.upper())
#lower() method converts the string to lowercase
print('HELLO'.lower())
#capitalize() method capitalizes the first character of the string
print('hello'.capitalize())
#title() method capitalizes the first character of each word in the string
print('hello'.title())
#swapcase() method swaps the case of the string
print('Hello'.swapcase())
#casefold() method converts the string to lowercase
print('HELLO'.casefold())
#center() method centers the string
print('hello'.center(20))
#ljust() method left-justifies the string
print('hello'.ljust(20))
#rjust() method right-justifies the string
print('hello'.rjust(20))
#zfill() method fills the string with zeros
print('hello'.zfill(20))
#lstrip() method removes leading whitespace
print(' hello'.lstrip())
#rstrip() method removes trailing whitespace
print('hello '.rstrip())
#strip() method removes leading and trailing whitespace
print(' hello '.strip())
#replace() method replaces a substring with another substring
print('hello'.replace('h', 'H'))

#escape characters
#escape characters are used to insert characters that are illegal in a string
#escape characters are preceded by a backslash
#escape characters are not interpreted by the interpreter
print('hello \'world\'')
#this prints hello 'world'
print('hello \"world\"')
#this prints hello "world"
print('hello \\world\\')
#this prints hello \world\
print('hello \nworld')
#this prints hello on a new line and world on a new line
print('hello \tworld')
#this prints hello and world separated by a tab
