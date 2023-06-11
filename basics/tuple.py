#Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 

#Create tuple
fruits = ('apple', 'banana', 'cherry')
#tuple items are separated by commas
#example
bicycles = ('trek', 'cannondale', 'redline', 'specialized')
#tuple items are enclosed in parentheses
#example
print(fruits[0])
numbers = (1, 2, 3, 4, 5)
#example
print(bicycles[0])
#example
print(bicycles[-1])

#tuple are unchangeable
#example
# fruits[0] = 'orange'
#this will give an error
#example
# fruits.append('orange')
#this will give an error

#tuple allows duplicate values
#example
vegetables = ('carrot', 'tomato', 'potato', 'tomato')
print(vegetables[1])
#you can also check the length of a tuple using len()
#example
print(len(vegetables))

#you can also create a tuple with only one item
#example
one = ('item',)
print(type(one))
#this will print <class 'tuple'>
#note the comma after the item
#otherwise Python will not recognize it as a tuple.

#tuple can be of any data type and can contain different data types
#example
mixed = ('apple', 'banana', 'cherry', 1, 2, 3)
print(mixed)
#this will print ('apple', 'banana', 'cherry', 1, 2, 3)
#example
dd = ("abc", 34, True, 40, "male")
print(dd)
#this will print ('abc', 34, True, 40, 'male')

#type of tuple
#example
print(type(mixed))
#this will print <class 'tuple'>
#why is it <class 'tuple'> and not <class 'list'>?

#beacuse From Python's perspective, tuples are defined as objects with the data type 'tuple'

#it also possible to make a tuple from the tuple() constructor
#example
fruits = tuple(('apple', 'banana', 'cherry'))
print(fruits)
#this will print ('apple', 'banana', 'cherry')
#note the double round-brackets
#this is beacause the tuple() constructor is also a function

#you can also change a tuple to a list and vice versa
#example
fruits = ('apple', 'banana', 'cherry')
fruits = list(fruits)
print(fruits)
#this will print ['apple', 'banana', 'cherry']

#you can also change the value of a tuple by changing it to a list
#example
fruits = ('apple', 'banana', 'cherry')
fruits = list(fruits)
fruits[0] = 'orange'
fruits = tuple(fruits)
print(fruits)
#this will print ('orange', 'banana', 'cherry')

#you can also append a tuple
#example
fruits = ('apple', 'banana', 'cherry')
fruits = list(fruits)
fruits.append('orange')
fruits = tuple(fruits)
print(fruits)
#this will print ('apple', 'banana', 'cherry', 'orange')

#you can also delete a tuple
#example
fruits = ('apple', 'banana', 'cherry')
del fruits
#this will delete the tuple

#you can also remove a value from a tuple
#example
fruits = ('apple', 'banana', 'cherry')
fruits = list(fruits)
fruits.remove('apple')
fruits = tuple(fruits)
print(fruits)
#this will print ('banana', 'cherry')

#you can also add a tuple to a tuple
#example
fruits = ('apple', 'banana', 'cherry')
fruits2 = ('orange', 'mango', 'grapes')
fruits += fruits2
print(fruits)
#this will print ('apple', 'banana', 'cherry', 'orange', 'mango', 'grapes')

#you can also unpack a tuple
#example
fruits = ('apple', 'banana', 'cherry')
a, b, c = fruits
print(a)
print(b)
print(c)
#this will print apple
#this will print banana
#this will print cherry

#example
fruits = ('apple', 'banana', 'cherry', 'orange', 'mango', 'grapes')
a, b, *c = fruits
print(a)
print(b)
print(c)
#this will print apple
#this will print banana
#this will print ['cherry', 'orange', 'mango', 'grapes']
#note the * in front of c
#this means that c will take the rest of the values in the tuple

#you can also loop through a tuple
#example
fruits = ('apple', 'banana', 'cherry')
for x in fruits:
    print(x)
#this will print apple
#this will print banana
#this will print cherry
#note that the loop will stop at the last value



#tuple methods
#example
print(fruits.count('apple'))
#this will print 1
#this is because there is only one apple in the tuple
print(fruits.index('banana'))
#this will print 1
#this is because banana is the second value in the tuple