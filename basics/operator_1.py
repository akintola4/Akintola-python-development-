#operator
#operator in python is a symbol that performs an operation on one or more operands. 
#An operand is a variable or a value on which we perform the operation.

#types of operator

#Example:
#Arithmetic operator
#they are used to perform mathematical operations like addition, subtraction, multiplication etc.
# +, -, *, /, %, //, **

# + is used for addition
print(2+3)
#this prints 5 because 2+3 = 5

# - is used for subtraction
print(2-3)
#this prints -1 because 2-3 = -1

# * is used for multiplication
print(2*3)
#this prints 6 because 2*3 = 6
# / is used for division
print(2/3)
#this prints 0.6666666666666666 because 2/3 = 0.6666666666666666

# % is used for modulus
print(2%3)
#this prints 2 because 2%3 = 2

# // is used for floor division
print(2//3)
#this prints 0 because 2//3 = 0

# ** is used for exponent
print(2**3)
#this prints 8 because 2*2*2 = 8

#Assignment operator
#they are used to assign values to variables.
# =, +=, -=, *=, /=, %=, //=, **=
# = is used for assigning values
x = 2
a = 2
print(a)
#this prints 2
# += is used for adding values
x += 2
print(x)
#this prints 4 because x = x + 2

# -= is used for subtracting values
x -= 2
print(x)
#this prints 2 because x = x - 2

# *= is used for multiplying values
x *= 2
print(x)
#this prints 4 because x = x * 2

# /= is used for dividing values
x /= 2
print(x)
#this prints 2 because x = x / 2

# %= is used for modulus
x %= 2
print(x)
#this prints 0 because x = x % 2

# //= is used for floor division
x //= 2
print(x)
#this prints 0 because x = x // 2

# **= is used for exponent
x **= 2
print(x)
#this prints 0 because x = x ** 2

#Comparison operator
#they are used to compare values.
# ==, !=, >, <, >=, <=
# == is used for equality
print(2 == 3)
#this prints False because 2 is not equal to 3
# != is used for not equal
# != is used for inequality
print(2 != 3)
#this prints True because 2 is not equal to 3
# > is used for greater than
print(2 > 3)
#this prints False because 2 is not greater than 3
# < is used for less than
print(2 < 3)
#this prints True because 2 is less than 3
# >= is used for greater than or equal to
print(2 >= 3)
#this prints False because 2 is not greater than or equal to 3
# <= is used for less than or equal to
print(2 <= 3)
#this prints True because 2 is less than or equal to 3


#Logical operator
#they are used to combine conditional statements.
# and, or, not
# and is used for logical and
# and is used for logical and
print(2 == 3 and 2 != 3)
#this prints False because 2 is not equal to 3 and 2 is not equal to 3
# or is used for logical or
print(2 == 3 or 2 != 3)
#this prints True because 2 is equal to 3 or 2 is not equal to 3
# not is used for logical not
print(not(2 == 3 and 2 != 3))
#this prints True because 2 is not equal to 3 and 2 is not equal to 3
# not is used for logical not
print(not(2 == 3 or 2 != 3))
#this prints False because 2 is equal to 3 or 2 is not equal to 3

#Identity operator
#they are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# is, is not
# is is used for identity
print(2 is 3)
#this prints False because 2 is not equal to 3
# is not is used for non-identity
print(2 is not 3)
#this prints True because 2 is not equal to 3

#Membership operator
#they are used to test if a sequence is presented in an object.
# in, not in
# in is used for membership
print(2 in [1,2,3])
#this prints False because 2 is not in [1,2,3]
# not in is used for non-membership
print(2 not in [1,2,3])
#this prints True because 2 is not in [1,2,3]

#Bitwise operator
#they are used to perform bitwise operations.
# &, |, ^, ~, <<, >>
# & is used for bitwise and
# | is used for bitwise or
# ^ is used for bitwise xor 
# ~ is used for bitwise not
# << is used for bitwise left shift
# >> is used for bitwise right shift
# & is used for bitwise and
print(2 & 3)
#this prints 2 because 2 & 3 = 2
# | is used for bitwise or
print(2 | 3)
#this prints 3 because 2 | 3 = 3
# ^ is used for bitwise xor
print(2 ^ 3)
#this prints 1 because 2 ^ 3 = 1
# ~ is used for bitwise not
print(~2)
#this prints -3 because ~2 = -3
# << is used for bitwise left shift
print(2 << 3)
#this prints 16 because 2 << 3 = 16
# >> is used for bitwise right shift
print(2 >> 3)
#this prints 0 because 2 >> 3 = 0

#operator precedence
#operator precedence is a way to specify the order in which the operations are performed.
#just like using BODMAS in mathematics
#where B stands for bracket, O stands for order, D stands for division, M stands for multiplication, A stands for addition and S stands for subtraction
#it follows the order of operations from left to right.
#Example:
# () is used for parenthesis
# ** is used for exponent
# * is used for multiplication
# / is used for division
# % is used for modulus
# + is used for addition
# - is used for subtraction
print(2 + 3 * 4)
#this prints 14 because 3 * 4 = 12 and 2 + 12 = 14
print((2 + 3) * 4)
#this prints 20 because 2 + 3 = 5 and 5 * 4 = 20
print(2 ** 3 / 4)
#this prints 2 because 2 ** 3 = 8 and 8 / 4 = 2
print(2 ** (3 / 4))
#this prints 2.0 because 2 ** (3 / 4) = 2.0
print(2 * 3 % 4)
#this prints 2 because 2 * 3 = 6 and 6 % 4 = 2
print(2 * 3 // 4)
#this prints 2 because 2 * 3 = 6 and 6 // 4 = 2
print(2 * 3 + 4)
#this prints 10 because 2 * 3 = 6 and 6 + 4 = 10
print(2 + 3 * 4 % 5)
#this prints 10 because 2 + 3 * 4 % 5 = 10
print(2 + 3 * 4 % (5 + 6))
#this prints 10 because 2 + 3 * 4 % (5 + 6) = 10
print(2 + 3 * 4 ** 2)
#this prints 50 because 2 + 3 * 4 ** 2 = 50
print(2 + 3 * 4 ** 2 / 5)
#this prints 10.4 because 2 + 3 * 4 ** 2 / 5 = 10.4
print(2 + 3 * 4 ** (2 / 5))
#this prints 7.2 because 2 + 3 * 4 ** (2 / 5) = 7.2
print(2 + 3 * 4 ** (2 / 5) + 6)
#this prints 13.2 because 2 + 3 * 4 ** (2 / 5) + 6 = 13.2
print(2 + 3 * 4 ** (2 / 5) + 6 // 7)
#this prints 13.2 because 2 + 3 * 4 ** (2 / 5) + 6 // 7 = 13.2
