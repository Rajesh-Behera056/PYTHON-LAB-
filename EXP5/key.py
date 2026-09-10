def max_key(d):
    return max(d,key=d.get)

d = eval(input("Enter dictionary:"))
print("Key with maximum value:",max_key(d))