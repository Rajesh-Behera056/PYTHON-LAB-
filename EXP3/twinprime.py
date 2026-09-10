n = int(input("Enter n:"))

for i in range(2,n-1):
    a=0
    b=0

    for j in range(2, i):
        if i % j == 0:
            a = 1
            break

    for j in range(2,i+2):
        if (i+2) % j == 0:
            b = 1
            break

    if a == 0 and b == 0:
        print(i, i+2)