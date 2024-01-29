# accepting an any integer for commuting n+nn+nnn
 
a = input("input any integer....")

no1 = int("%s" %a)
no2 = int("%s%s" %(a,a))
no3 = int("%s%s%s" %(a,a,a))
print(no1+no2+no3)