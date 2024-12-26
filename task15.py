n = int(input("Enter few number: "))
n1 = int(input("second: "))
n2 = int(input("third: "))
n3 = int(input("fourth: "))

num = {n, n1, n2, n3}

for i in num:
    if i % 2 != 0  and i % 3 == 0:
        print(i)
    
