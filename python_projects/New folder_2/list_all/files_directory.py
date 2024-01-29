# finding all file directory in python 
from os import listdir
from os.path import isfile, join
file_list = [f for f in listdir('/home/students'  ) if isfile(join('/home/ students',f))]
print(file_list)