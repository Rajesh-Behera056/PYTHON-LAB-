def transpose(a,n):
    for i in range(n):
        for j in range(i + 1,n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

n = int(input("Enter n:"))
a = [list(map(int,input().split())) for i in range(n)]

transpose(a,n)
for row in a:
    print(row)