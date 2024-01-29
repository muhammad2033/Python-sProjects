# printing the value or star 


def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '\tALLAH'
          times = times - 1
        print(output)

histogram([1,2,3,4,5])
histogram([5,4,3,2,1])
histogram([2,3,4,5,1,7])