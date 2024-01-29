# printing the color list from the other list which are not presented fromeach other

lis_1 = set(['white','black','blue','green','gray'])
lis_2 = set(['brown','black','green'])
print("print original set,,\n")
print(lis_1)
print(lis_2)
print("\n difference of color 1 and color 2...")
print(lis_1.difference(lis_2))
print("\n difference of color 2 and color 1...")
print(lis_2.difference(lis_1))

# got it
