s = input("Enter a string:")
new = ""

for ch in s:
    if ch not in new:
        new += ch

print("After removing duplicates:",new)