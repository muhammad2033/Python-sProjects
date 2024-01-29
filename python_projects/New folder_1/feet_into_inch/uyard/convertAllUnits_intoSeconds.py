# convert the all units into second 
year = int (input("input the the following years...\n"))*3600*24*365
month = int (input("input the the following months...\n"))*3600*24*31
week = int (input("input the the following weeks...\n"))*3600*24*7
day= int (input("input the the following days...\n"))*3600*24
hour= int (input("input the the following hours...\n"))*3600
minute = int (input("input the the following minutes...\n"))*60
second= int (input("input the the following seconds...\n"))

seconds = year+month+week+day+hour+minute+second

print("print all the units into second...\n",seconds)