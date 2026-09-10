s = input("Enter a string:")

print("Reverse =", s[::-1])

v = 0
c = 0

for ch in s.lower():
    if ch in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1

print("Vowels =", v)
print("Consonants =", c)