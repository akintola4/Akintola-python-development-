# Develop a standard grading system using python else if statements

# matricNumber = int(input("enter your matric number"))

score = int(input("enter your score:"))

if (score > 70 and score < 101 ):
    print("You got A")
elif (score > 69 and score <70):
    print("You got B")
elif (score > 59 and score <69):
    print("You got C")
elif (score > 49 and score <59):
    print("You got D")
elif (score > 40 and score <49):
    print("You got E")
elif (score > 0 and score <40):
    print("You got F")
