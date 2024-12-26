n = int(input("Enter number: "))
r = range(1, n)

for i in r:
    if n % i == 0:
        print(i, end = " ")

print(n)