n = int(input("Enter number: "))
r = range(1, n)

for i in r:
    count = 0
    for j in r:
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end = " ")        
            
            