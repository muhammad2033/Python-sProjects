string ="my name is maaz ,live in peshawar"
word_list = string.split()
word_freq = [word_list.count(n) for n in word_list]

print("string:\n{} \n ".format(string))
print("list:\n {} \n ".format(str((word_list))))
print("pairs(word and frequencies .. \n {} \n".format(str(list(zip(word_list, word_freq)))))
