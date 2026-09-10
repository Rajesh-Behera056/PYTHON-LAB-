import math

a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))

d = b*b - 4*a*c

if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)

    print("Root 1 =",r1)
    print("Root 2 =",r2)
else:
    print("Roots are imaginary")