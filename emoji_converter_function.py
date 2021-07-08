def emoji_converter(personal_message):
   
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
    # print(output)

    return output


personal_message = input("> ")
print(emoji_converter(personal_message))


