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
class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def myfunc(self):
        print("Hello my name is " + self.name)
class car1(car):
    def myfunc(self):
        print("Hello my name is " + self.name + " and my color is " + self.color)
c1 = car("Ford", "red")
c1.myfunc()
c2 = car1("Ferrari", "red")
c2.myfunc()

#the child class can also inherit from multiple parent classes
#example
class animal:
    def __init__(self, name,color,kingdom):
        self.name = name
        self.color = color
        self.kingdom = kingdom
    def myTest(self):
        print("Hello my name is " + self.name + " and my color is " + self.color + " and my kingdom is " + self.kingdom)
    
class dog(animal):
    def __init__(self, name, color, kingdom, breed):
        super().__init__(name, color, kingdom)
        self.breed = breed #here we add the breed attribute to the child class
        
        #here we use the super() function to inherit the parent class attributes
        #the super() function returns a proxy object that allows us to access the parent class attributes and methods
        #the proxy object is called the superclass object
        
    def myTest(self):
        print("Hello my name is " + self.name + " and my color is " + self.color + " and my kingdom is " + self.kingdom + " and my breed is " + self.breed)
        
