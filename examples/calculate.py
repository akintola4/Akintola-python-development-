# Code in python to generate a calculator that includes the following operators
# Addition of two numbers
# Subtraction of two numbers
# Division of two numbers
# Multiplication of two numbers
# Modulus of two numbers

one = int(input("enter your first number: "))
print("enter your operator")
print("for minus"+" "+ "-" )
print("for addition" +" "+"+" )
print("for division"+" "+ "/" )
print("for multiplication" +" "+"+" )
print("for modulus"+" "+ "%" )
opt = input()
two = int(input("enter your second number: "))
if(opt=="+"):
    result=one+two
elif(opt=="-"):
    result=one-two
elif(opt=="X"):
    result=one*two
elif(opt=="/"):
    result=one/two
elif(opt=="%"):
    result=one%two
print("the result is:", result)
print(result)
