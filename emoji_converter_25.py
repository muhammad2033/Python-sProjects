
message = input(">")
words = message.split(' ') 
emoji_converter = {

            "sad" : "sad",
            "  " : " delighted"
 

} 

output = ""
for word in words : 
    output += emoji_converter.get(word,word) + " "
print(output)     