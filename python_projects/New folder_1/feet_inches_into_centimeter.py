# converting the feet and inches into centimeters 

print("input the height..\n")
h_ft = int (input("feet\n"))
h_inch = int (input("inches\n"))
h_ft += h_inch * 12
h_cm = round(h_inch *2.54 , 1)
print("print the height  %d cm. \n " % h_cm)