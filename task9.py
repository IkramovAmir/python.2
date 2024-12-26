n = int(input("Enter number: "))

n += 1 #range gets n - 1 as last number , that is why 1 is added to take n also

count = 0
i = 0
r = range(0,n)
for i in r:
    count += i
    
print(count)    