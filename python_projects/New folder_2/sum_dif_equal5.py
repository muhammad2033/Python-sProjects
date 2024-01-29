# return true is sum is equal ,sum and difference is 5

def test_number(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5 :
        return True
    else:
        return False
print(test_number(11,3))            
print(test_number(3,3))            
print(test_number(2,3))            
print(test_number(8,3))            
print(test_number(11,3))            