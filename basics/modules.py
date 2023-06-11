#a module is bascially a file containing a set of function to include in your application
#there a core python module, modules you can install using the pip package manager (including Django) as well as custom modules

#example
import datetime

from datetime import date

import time
from time import time
today = date.today()
#to get the current time
timestamp = time()
print(today)
print(timestamp)


#we can also import custom modules
#we can also create our own modules
#create a file with the .py extension
#created one called mymodule.py
#import the module
import mymodule
from mymodule import add
from mymodule import sub
#use the module
#here i am using the add function from the mymodule.py file
print(add(1,2))
#this will print 3

#here i am using the sub function from the mymodule.py file
print(sub(2,1))
#this will print 1



