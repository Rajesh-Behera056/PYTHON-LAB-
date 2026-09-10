s = input("Enter a string:")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

n = len(s)

if n % 2 == 0 and s[:n//2] == s[n//2:]:
    print("Symmetric")
else:
    print("Not Symmetric")