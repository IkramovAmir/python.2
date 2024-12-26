s = input("Enter sentence: ")

length = len(s)
i = 0
count = 1
while i < length - 1:
    count = 1
    if s[i] == s[i + 1]:
        while i < length - 1:
            if s[i] == s[i + 1]:
                count += 1
                i +=  1
            else:
                break
    
        print(count, s[i])
            
    i += 1         
    
    


        
    