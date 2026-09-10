def merge(d1,d2):
    d1.update(d2)
    return d1

d1 = eval(input("Enter first dictionary:"))
d2 = eval(input("Enter second dictionary:"))

print("Merged dictionary:",merge(d1,d2))