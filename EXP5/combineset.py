def combine(a,b):
    return a | b

a = set(eval(input("Enter first set:")))
b = set(eval(input("Enter second set:")))

print("New set:",combine(a,b))