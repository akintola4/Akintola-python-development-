##data type in python
#text type: str
#numeric type: int, float, complex
#sequence type: list, tuple, range
#mapping type: dict
#set type: set
#boolean type: bool
#int
#   An integer is a whole number that can be positive or negative. It is a derived data type.
int = 1
#float
#A float is a number that has a decimal point. It is a derived data type.
float = 1.0
#string
#A string in Python is a sequence of characters. It is a derived data type. Strings are immutable. This means that once defined, they cannot be changed.
string = "hello"
#boolean
#A boolean is a data type that can only be true or false.
boolean = True
#complex
#A complex number is a number that can be expressed as a combination of real and imaginary parts.
complex = 1j

#list
#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
list = ["apple", "banana", "cherry"]
#tuple
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple = ("apple", "banana", "cherry")
#set
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
set = {"apple", "banana", "cherry"}
#dictionary
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dictionary = {"name":"john", "age":30}
#dictionary can be written as dict
dict = {"name":"john", "age":30}

#range
#A range is a collection which is ordered and immutable. In Python ranges are written with round brackets.
range = range(6)
#frozenset
#A frozenset is a collection which is unordered and unchangeable. In Python frozensets are written with curly brackets.
frozenset = frozenset({"apple", "banana", "cherry"})
#bytes
#A bytes is a sequence of bytes. In Python bytes are written with the b prefix.
bytes = b"hello"
#bytearray
#A bytearray is a mutable sequence of bytes. In Python bytearrays are written with the b prefix.
bytearray = bytearray(5)
#memoryview
#A memory view is a view of memory. In Python memory views are written with the memoryview() function.
memoryview = memoryview(bytes(5))
#None
#The None keyword is used to define a null value, or no value at all.
none = None
#type() 
#The type() function returns the data type of the specified object.
print(type(int))
print(type(float))
print(type(string))
print(type(boolean))
print(type(complex))
print(type(list))
print(type(tuple))
print(type(set))
print(type(dictionary))
print(type(dict))
print(type(range))
print(type(frozenset))
print(type(bytes))
print(type(bytearray))
print(type(memoryview))
print(type(none))
#output
#<class 'int'>
#<class 'float'>
#<class 'str'>
#<class 'bool'>
#<class 'complex'>
#<class 'list'>
#<class 'tuple'>
#<class 'set'>
#<class 'dict'>
#<class 'dict'>
#<class 'range'>
#<class 'frozenset'>
#<class 'bytes'>
#<class 'bytearray'>
#<class 'memoryview'>
#<class 'NoneType'>
#type() can also be used to create new data types
#example
#Create a class named MyClass, with a property named x:
class MyClass:
    x = 5
#Create an object of type MyClass:
p1 = MyClass()
print(p1.x)
#output
#5
#example
#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Create an object of type Person, and print the value of name and age:
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#output
#John
#36

