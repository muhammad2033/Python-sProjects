n = int(input("enter the number for factorial..."))

product = 1
for i in range(n):
    product = product *(i +1)
print(product)

words = str(input("enter the word:\n "))
text_digit = {
        "one"  : "i wanna make a project \n",
        "two"  : "in which we can print a dozen of functions \n",
        "three": "firstly, i'd like to make a program of factorial \n",
        "four" : "secondly, for dictionary\n"
}
output = " "
for number in words:
    output += text_digit.get(number,"wrong!!!") +" "
print(output)



project = input("  project name \n")
if project == product:
    print(product)
    with open("project_1.txt","w") as f:
        data = f.write(str(product))
    print(data)
else  :  
    print(output)
     
    with open("project_1.txt","w") as f:
        data = f.write(output)
        print(data)
    



