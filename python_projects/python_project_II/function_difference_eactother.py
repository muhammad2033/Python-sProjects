# printing a program's function which exist integer but difference from each other

def test_distinct(data):
    if len(data)== len(set(data)):
        return True
    else:
        return False

print(test_distinct([1,2,3,4,5,6,7,8,9,11]))            
print(test_distinct([1,2,3,4,5,6,6,7,8,9,11]))            