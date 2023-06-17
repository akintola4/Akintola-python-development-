#inheritance in python
#it means that a class can inherit attributes and methods from another class
#the class that inherits is called the child class
#the class that is being inherited from is called the parent class
#example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
class Student(Person):
    pass
p1 = Person("John", 36)
p1.myfunc()
s1 = Student("Mike", 24)
s1.myfunc()
#here the student class inherits the person class
#the person class is the parent class

#the child class inherits all the attributes and methods from the parent class

#the child class can override the parent class methods
#example
