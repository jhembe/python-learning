personal_message = input("> ")
# we need to separate the input string stream
#here we use the split method split()

words = personal_message.split(" ")
# print(words)

## here we have to define a dictionary in order to be mapping 
#creating an emoji dictionary
emoji = {
    ":)":"😄",
    ":(":"😥",
    "sunshine":"🌞",
    "graduate":"👨‍🎓",
    "copy right":"©",
    "registered":"®",
    "family":"👨‍👩‍👧",
    "love":"👩‍❤️‍💋‍👩",
    "trademark":"™",
    "lovee":"👨‍❤‍👨", 
    "time":"⌚",
    "wait":"⌛",
    "star":"⭐",
    "elephant":"🐘",
    "cat":"🐕",
    "ant":"🐜",
    "cock":"🐔"
}

output = ""

for word in words:
    output += emoji.get(word,word)+" "
print(output)

#creating a functionfor the emoji converter
def emoji_converter():
    personal_message = input("> ")
# we need to separate the input string stream
#here we use the split method split()

words = personal_message.split(" ")
# print(words)

## here we have to define a dictionary in order to be mapping 
#creating an emoji dictionary
emoji = {
    ":)":"😄",
    ":(":"😥",
    "sunshine":"🌞",
    "graduate":"👨‍🎓",
    "copy right":"©",
    "registered":"®",
    "family":"👨‍👩‍👧",
    "love":"👩‍❤️‍💋‍👩",
    "trademark":"™",
    "lovee":"👨‍❤‍👨", 
    "time":"⌚",
    "wait":"⌛",
    "star":"⭐",
    "elephant":"🐘",
    "cat":"🐕",
    "ant":"🐜",
    "cock":"🐔"
}

output = ""

for word in words:
    output += emoji.get(word,word)+" "
print(output)