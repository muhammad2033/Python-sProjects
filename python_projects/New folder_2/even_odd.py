# finding the even or odd number with printing a statement
no = int(input("input the number for finding the even or odd...\n"))

mod = no % 2
if mod > 0:
    print("this is an odd number")
else:
    print("this is an even  number")