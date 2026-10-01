numbers = [2,3,4,5]

result = list(map(lambda x, y: x ** y,numbers, range(len(numbers))))

print("Original List:",numbers)
print("Result:",result)