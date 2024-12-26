sent = input("Enter sentence: ")

sent = sent.split()
longest = ""

for i in sent:
    
    if len(i) > len(longest):
        longest = i

print(longest)        