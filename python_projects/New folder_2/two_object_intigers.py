# two objects both are intigers......

def add(x,y):
    if not((isinstance(x,int)) and (isinstance(y,int))):
        return "input must be an integer"
    else:
        return x + y
print(add(2,2))            
print(add(2,3.))            
print(add('2',2))            
print(add('2','2'))            