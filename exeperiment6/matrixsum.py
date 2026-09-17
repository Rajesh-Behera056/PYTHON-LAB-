def sums(a):
    for r in a:
        print(r, "=", sum(r))

    print("Column sums:")
    for j in range(3):
        print(sum(a[i][j] for i in range(3)))

a = [list(map(int, input().split())) for i in range(3)]
sums(a)