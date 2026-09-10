n = int(input("Enter a 3 digit number:"))

print("Prime factors:")

for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n = n // i