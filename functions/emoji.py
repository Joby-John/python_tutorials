def emojiConverter(message):
    emojis = {
        ":(":"😢",
        ":)":"😊"
    }

    words = message.split(" ")
    output = ""
    for word in words:
        output+=emojis.get(word, word)+" "
    
    return output

message1 = emojiConverter(input(">"))

print(message1)
