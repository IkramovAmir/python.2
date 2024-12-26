sentence = input("Enter sentence: ")

i = 0

length = len(sentence)

while i < length:
    
    if  sentence[i] == " ":
        print(sentence[i])
        i += 1
        print(sentence[i], end = '')
    else:
        print(sentence[i], end = "")
    i += 1  