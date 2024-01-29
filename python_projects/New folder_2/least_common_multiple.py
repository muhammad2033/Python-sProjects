# least common factor (lcm)
def lcm(x,y):
    if x>y :
        z=x
    else:
        z = y
    while(True):
        if((z % x ==0) and (z % y ==0)) :
            icm = z
        z +=1
    return lcm

print(lcm(4,3))        

