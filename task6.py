sentence = input("Enter sentence: ")

i = 0

length = len(sentence)

while i < length:
    if i == 0:
        print(sentence[i].capitalize(), end = '')
    if  sentence[i] == " ":
        print(sentence[i], end = '')
        i += 1
        print(sentence[i].capitalize(), end = '')
    else:
        print(sentence[i], end = "")
    i += 1    