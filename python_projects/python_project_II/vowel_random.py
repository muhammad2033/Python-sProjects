# make a program to select random letter of vowel

import random
vowel_list = ['a','e','i','o','u' ]
random.shuffle(vowel_list)
print(''.join(vowel_list))