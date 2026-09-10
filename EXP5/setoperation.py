def operations(a,b):
    print("Union:",a | b)
    print("Intersection:",a & b)
    print("Difference A-B:",a - b)
    print("Difference B-A:",b - a)
    print("Symmetric Difference:",a ^ b)

a = set(eval(input("Enter first set:")))
b = set(eval(input("Enter second set:")))

operations(a,b)