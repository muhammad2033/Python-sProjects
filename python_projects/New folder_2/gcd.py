# greatest common division

def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2),0,-1):
        if x % k == 0  and y % k == 0:
            gcd = k
            break
    return gcd
    
print("gcd of 12 and 17",gcd(12,17))
print("gcd of 12 and 17",gcd(4,6))
print("gcd of 12 and 17",gcd(322,362))
print("gcd of 12 and 17",gcd(35,55))
