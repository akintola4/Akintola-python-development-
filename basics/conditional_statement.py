#coniditonal statement in python are used to make decisions in the program.
#conditional statement are also known as if-else statement
#if-else statement are used to perform different actions based on different conditions.
#if statement
#example
a=10
10
b=20
if a>b:
    print("a is greater than b")
    
#this will not print anything because the condition is not true

#else statement
#example
a=10
b=20
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")
#this will print a is not greater than b because the condition is not true

#elif statement
#elif is short for else if.
#elif statement are used to test more than two conditions
#example
a=10
b=20
c=30
if a>b:
    print("a is greater than b")
elif a>c:
    print("a is greater than c")
else:
    print("a is not greater than b or c")
#this will print a is not greater than b or c because the condition is not true

#short hand if statement
#short hand if statement is used to make a single line if statement.
#example
a=10
b=20
if a>b: print("a is greater than b")
#this will print a is greater than b because the condition is true

#short hand if-else statement
#short hand if-else statement is used to make a single line if-else statement.
#example
a=10
b=20
if a>b: print("a is greater than b")
else: print("a is not greater than b")
#this will print a is not greater than b because the condition is not true


#you can also have multiple else statement on the same line
#example
a=10
b=20
if a>b: print("a is greater than b")
else: print("a is not greater than b")
#this will print a is not greater than b because the condition is not true

#and statement
#and statement is used to combine multiple conditions.
#example
a=10
b=20
c=30
if a>b and a>c:
    print("a is greater than b and c")
else:
    print("a is not greater than b and c")
#this will print a is not greater than b and c because the condition is not true

#or statement
#or statement is used to combine multiple conditions.
#example
a=10
b=20
c=30
if a>b or a>c:
    print("a is greater than b or c")
else:
    print("a is not greater than b or c")
#this will print a is not greater than b or c because the condition is not true

#not statement
#not statement is used to invert the result of a condition.
#example
a=10
b=20
if not a>b:
    print("a is not greater than b")
else:
    print("a is greater than b")
#this will print a is greater than b because the condition is true

#pass statement
#pass statement is used to avoid getting an error.
#example
a=10
b=20
if a>b:
    pass
#this will not print anything because the condition is not true
#but it will not give an error
#this is useful when you are writing a function and you want to write a function body but don't want to write anything in it.

#nested if statement
#nested if statement is an if statement inside an if statement.
#example
a=10
b=20
c=30
if a>b:
    if a>c:
        print("a is greater than b and c")
    else:
        print("a is not greater than b and c")
else:
    print("a is not greater than b")
#this will print a is not greater than b because the condition is not true


#membership operator
#membership operator are used to test if a sequence is presented in an object
#example  
p = 3
n= 13
numbers = [
    1,2,3,4,5
]
#not 


#in
if p in numbers:
    print(p in numbers)
    #this will print true 
#not in 
if n not in numbers:
    print(n in numbers)
    #this will print false
    
#identity operator (is , is not) compare the object, not if they are equal, but if they are actually the same 
#object, with the same memory location:
g=3
k=4
#is
if g is k:
    print(g is k)
    #wont print anything since g is not k
#is not 
if g is not k:
    print(g is not k)
    #this will print true