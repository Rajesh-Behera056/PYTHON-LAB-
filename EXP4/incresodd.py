a = []

for i in range(20):
    a.append(int(input("Enter number: ")))

for i in range(20):
    if a[i] % 2 != 0:
        a[i] = a[i] + 5

print("New list =",a)