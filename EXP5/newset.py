def copy_set(s):
    new = set()
    for x in s:
        new.add(x)
    return new

s = set(eval(input("Enter set:")))

print("Original set:",s)
print("New set:",copy_set(s))