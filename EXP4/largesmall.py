a = []
for i in range(10):
    a.append(int(input("Enter number:")))

largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')

for x in a:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x

    if x < smallest:
        second_smallest = smallest
        smallest = x
    elif x < second_smallest and x != smallest:
        second_smallest = x

print("Second Largest =",second_largest)
print("Second Smallest =",second_smallest)