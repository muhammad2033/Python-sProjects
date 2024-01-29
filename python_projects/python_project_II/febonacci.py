# print a program of febonacci series 

a = int(input("input the numbers for febonacci serires..."))
f = 0
s = 1
if a<=0:
    print("the request series is in \n ..",f)
else:
    print(s,f,end=" ")
    for n in range(2,a):
        next = f + s
        print(next,end = " ")
        f = s
        s = next

        # it s febonacci series

        
