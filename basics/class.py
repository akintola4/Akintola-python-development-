#class in python is a blueprint for creating objects
#object is an instance of a class
#example
#this is a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
#this is an object
p1 = Person("John", 36)
#we can access the object's properties
print(p1.name)
print(p1.age)
#we can access the object's methods
p1.myfunc()
#this will print
#John
#36
#Hello my name is John
