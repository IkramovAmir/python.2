sentence = input("Enter sentence: ")

length = len(sentence)
i = 0
length -= 1
sent2= ""
while i <= length:
    # print(sentence[i])
    sent2 += sentence[length]
    length -= 1

if sent2 == sentence:
    print(True)
else:
    print(False)    
    