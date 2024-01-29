# determinning the proflie through pstats module

import cProfile
def sum():
    print("sum..\n",1+2)
def mul():
    print('multiply..\n', 1*3)    
cProfile.run('sum()')    
cProfile.run('mul()')    