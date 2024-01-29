# sum of three digits if there is any two are equal then the sum will be zero

def three_sum(x,y,z):
    if x==y or y==z or x==z:
        sum = 0
    else:
         sum = x + y + z 
    return sum         

print(three_sum(4,3,4))    
print(three_sum(2,3,2))    
print(three_sum(2,3,4))    
print(three_sum(4,9,10))    
print(three_sum(2,3,6))    
print(three_sum(2,3,7))    