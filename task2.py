word_count = input("Enter sentence: ")
count = 0

for i in word_count:
    if i == " ":
     count += 1

count += 1        
print(f"The number of words is {count}")