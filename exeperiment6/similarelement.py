def group(a):
    x = sorted(sum(a,[]))
    n = len(a)
    return [x[i:i+n] for i in range(0, n*n,n)]

n = int(input("Enter n:"))
a = [list(map(int, input().split())) for i in range(n)]

print("Grouped Matrix:")
for r in group(a):
    print(r)