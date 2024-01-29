from typing import Concatenate


def concentrate(element):
    result = ''    
    for n in element:
        
        result += str(n)
    return result

print(concentrate([1,2,33,44]))       

# all value will be Concatenated fromthe list into string 