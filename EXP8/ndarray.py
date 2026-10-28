import numpy as np

# Creating ndarray object
arr = np.array([10,20,30,40,50])

print("Array:",arr)
print("Type:",type(arr))

# Indexing
print("First element:",arr[0])
print("Third element:",arr[2])

# Slicing
print("Elements from index 1 to 3:",arr[1:4])
print("First three elements:",arr[:3])
print("Last two elements:",arr[-2:])