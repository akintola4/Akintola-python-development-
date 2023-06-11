#a module is bascially a file containing a set of function to include in your application
#there a core python module, modules you can install using the pip package manager (including Django) as well as custom modules

#example
import datetime

from datetime import date

import time
from time import time
today = date.today()
#to get the current t
timestamp = time()
print(today)
print(timestamp)