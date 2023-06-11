#set is a collection of unique elements
#set are used to store multiple items in a single variable

#set are created using curly brackets
#example
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
#this will print {'apple', 'banana', 'cherry'}

#set items are separated by commas
#set items are unordered
#set items are unchangeable
#set items are indexed
#set can contain different data types
#example
toast = {'apple', 'banana', 'cherry',1, True}
print(toast)
#this will print {'apple', 'banana', 'cherry',1, True}`
#note that the data types are not the same


#set cannot contain duplicate values
# #example
turnite = {'apple', 'banana', 'cherry','cherry'}
print(turnite)
#this will print {'apple', 'banana', 'cherry'}
#note that the duplicate value was removed
#true and 1 are the same in set

# #example
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
# #this will print {'apple', 'banana', 'cherry'}


#you can use thr set() constructor to make a set
#example
test = set(('apple', 'banana', 'cherry'))
print(test)
#this will print {'apple', 'banana', 'cherry'}

#methods in set
#add() - adds an element to the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)
#this will print {'apple', 'banana', 'cherry', 'orange'}
#note that the element was added to the end of the set
#you can add multiple elements to the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.update(['orange', 'mango', 'grapes'])
print(fruits)
#this will print {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}
#note that the elements were added to the end of the set

#remove() - removes an element from the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)
#this will print {'apple', 'cherry'}
#note that the element was removed from the set
#you can also use discard() method to remove an element from the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)
#this will print {'apple', 'cherry'}
#note that the element was removed from the set
#note that if the element does not exist, discard() will not raise an error
#you can also use pop() method to remove an element from the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.pop()
print(fruits)
#this will print {'banana', 'cherry'}
#note that the element was removed from the set 
#note that pop() method will remove the last element from the set
#note that pop() method will return the removed element
#you can also use clear() method to remove all elements from the set
#example
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)
#this will print set()
#note that the set is now empty
#note that clear() method will not return any value
#note that clear() method will not return anything

#copy() - returns a copy of the set
#example
fruits = {'apple', 'banana', 'cherry'}
copy = fruits.copy()
print(copy)
#this will print {'apple', 'banana', 'cherry'}
#note that the copy of the set was returned

#union() - returns a set containing the union of sets
#example
fruits = {'apple', 'banana', 'cherry'}
vegetables = {'carrot', 'cabbage', 'onion'}
fruits_and_vegetables = fruits.union(vegetables)
print(fruits_and_vegetables)
#this will print {'apple', 'banana', 'cherry', 'carrot', 'cabbage', 'onion'}
#note that the union of the sets was returned
#note that the union of sets does not contain duplicate elements


#update() - updates the set with the union of this set and others
#example
fruits = {'apple', 'banana', 'cherry'}
vegetables = {'carrot', 'cabbage', 'onion'}
fruits.update(vegetables)
print(fruits)
#this will print {'apple', 'banana', 'cherry', 'carrot', 'cabbage', 'onion'}
#note that the update of the sets was returned
#note that the update of sets does not contain duplicate elements
