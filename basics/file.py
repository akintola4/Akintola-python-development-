#python has a function for creating, reading , updating and deleting files

#open a file
#example
myFile = open("myfile.txt", "w")
#w means the mode for writing

#get some info on the file
print("name of the file is: ", myFile.name)
print("is the file closed:", myFile.closed)
print("what is the mode of the file: ", myFile.mode)

#we can also write to the file
myFile.write("i love python and am testing if i can write to a file using python")
#we can close the file
myFile.close()

#if we want to append new content to the file 
myFile = open("myfile", "a")
#a means append
myFile.write("now i am testing if i can append to the file ")
#then i can close it 
myFile.close()

#if we want to read from a file
myFile = open("myfile", "r+")
#r+ means read 
#we need to save the data we get from the file into a variable 
text = myFile.read(100)
print("the data from the file : ", text)
 