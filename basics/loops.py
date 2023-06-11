#loops in python
people = ['tope', 'tosin','tayo','fola']

#for loop in python is used for iterating over a sequence (that is either a list, tuple, set, dictionary, a string )
#you can use for loop

for name in people:
    print(f"names {name}") 

#break 
#it can be used to break a loop
for name in people:
    if name == 'tayo':
        break
    print(f"the names will break at 'tayo' Current person:  {name}")
    #note tayo wont show
#continue 
#it can be used to break a loop
for name in people:
    if name == 'tayo':
        continue
    print(f"the names will continue after 'tayo' Current person: {name}")
    #note tayo wont show

#range
# 
#example
for i in range(len(name)):
    print(people[i])
# this will basically print the whole items in a list
 
 #we can also create a custom loop 
 #example
for i in range(0,11):
     print(f'Numbers: {i}')
 
#you can also use while loop
#while loops execute a set of statement as long as the condition is true
#example
index = 0
while index < len(people):
    print(people[index])
    index = index + 1
#example 
count = 0
while count <= 10:
    print(f'count: {count}')
    #we have to increaement it 
    count+=1

#it all depends on what you wanna use