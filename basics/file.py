#python has a function for creating, reading , updating and deleting files
#the key function for working with files in python is the open() function
#open() function takes two parameters:
#1. the file we want to open
#2. the mode in which we want to open the file

#they are four different modes for opening a file
#r - read - default mode
#w - write
#a - append
#r+ - read and write

#you can aslo specify if the file should be handled as binary or text mode
#t - text - default mode
#b - binary for non text files

nasa = open("nasa.txt", "r")
#here we open the nasa.txt file in read mode
#the variable nasa is now pointing to the file
print(nasa.read())

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
 