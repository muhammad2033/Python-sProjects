# finding the list and tuple from user with commas

l1 = input("input the commas for seperating...")
list = l1.split(",")
tuple = tuple(list)
print('list ,,,' , list)
print('tuple,,,,' , tuple)