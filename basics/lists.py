#list in python collection of items in a particular order 
#list are used to store multiple items in a single variable
#list are created using square brackets
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#example
fruits = ['apple', 'banana', 'cherry']
#list items are separated by commas
#example
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#list items are indexed starting from 0
#example
print(fruits[0])
    #this will print apple
print(bicycles[1])
#this will print cannondale

#list changes can be made
#example
names = ['john', 'peter', 'mary']
names[0] = 'james'
print(names)
#this will print ['james', 'peter', 'mary']


#you can also change a range of items in a list
#example
names[0:2] = ['james', 'peter']
print(names)
#this will print ['james', 'peter', 'mary']



#list allow duplicate values
#example
vegetables = ['carrot', 'tomato', 'potato', 'tomato']
print(vegetables[1])

#you can also check the length of a list using len()
#example
print(len(vegetables))
#this will print 4

#list can contain different data types
#example
mixed = ['apple', 'banana', 'cherry', 1, 2, 3]
print(mixed)
#this will print ['apple', 'banana', 'cherry', 1, 2, 3]

#example
bool = [True, False, True]
print(bool)
#this will print [True, False, True]

#you can also check the type of a list using type()
#example
print(type(bool))

#you can also use list() constructor to make a list
#example
new_list = list(('apple', 'banana', 'cherry'))
print(new_list)
#this will print ['apple', 'banana', 'cherry']

#you can check if an item is in a list using in keyword
#example
if 'apple' in new_list:
    print('yes, apple is in the list')

#append() method is used to add an item to the end of a list
#example
fruits.append('mango')
print(fruits)
#this will print ['apple', 'banana', 'cherry', 'mango']

#insert() method is used to add an item at a specified index
#example
fruits.insert(1, 'orange')  #this will add orange at index 1

#remove() method is used to remove an item from a list
#example
fruits.remove('cherry')
print(fruits)

#pop() method is used to remove an item at a specified index
#example
fruits.pop(1)
print(fruits)
#this will print ['apple', 'banana', 'mango']

#del keyword is used to delete an item at a specified index
#example
del fruits[0]
print(fruits)
#this will print ['banana', 'mango']
#del keyword can also be used to delete the entire list

#sort() method is used to sort the list
#sort() method sorts the list ascending by default
#example
fruits.sort()
print(fruits)
#this will print ['banana', 'mango', 'orange']

#reverse() method is used to reverse the list
#example
fruits.reverse()
print(fruits)
#this will print ['orange', 'mango', 'banana']

#copy() method is used to copy a list
#example
new_fruits = fruits.copy()
print(new_fruits)
#this will print ['orange', 'mango', 'banana']

#clear() method is used to clear a list
#example
new_fruits.clear()
print(new_fruits)
#this will print []
#clear() method can also be used to delete the entire list

#extend() method is used to add items from one list to another
#example
fruits.extend(new_fruits)
print(fruits)
#this will print ['orange', 'mango', 'banana']

#looping through a list
#example
mall = ['shoe', 'bag', 'cloth', 'shoe']
for item in mall:
    print(item)
#this will print shoe, bag, cloth, shoe

#Loop Through the Index Numbers
#example
for i in range(len(mall)):
    print(mall[i])
#this will print shoe, bag, cloth, shoe

#using a while loop
#example
i = 0
while i < len(mall):
    print(mall[i])
    i = i + 1
#this will print shoe, bag, cloth, shoe


#looping using list comprehension
#list comprehension is a way to create a new list with less syntax
#the syntax of list comprehension is [expression for item in iterable if condition == True]
#example
[print(item) for item in mall]
#this will print shoe, bag, cloth, shoe

#list comprehension can also be used to manipulate the list
#example
new_mall = [item for item in mall if item != 'shoe']
print(new_mall)
#this will print ['bag', 'cloth', 'shoe']

#list comprehension can also be used to create a new list  from an existing list using a conditional statement
#example
new_mall = []
for item in mall:
    if "s" in item:
        new_mall.append(item)
print(new_mall)
#this will print ['shoe', 'shoe']

#there are several ways to join two or more lists
#example
new_mall = mall + new_mall
print(new_mall)
#this will print ['shoe', 'bag', 'cloth', 'shoe', 'shoe', 'shoe']



#list comprehension can also be used to manipulate the list

# list are of different types tuple, set, dictionary
