# finding vowels whether the given letter is vowel or consonant


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('e'))    #true   
print(is_vowel('i'))    #true
print(is_vowel('x'))    #false