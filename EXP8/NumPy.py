import numpy as np

# Different data types
arr_int = np.array([10,20,30],dtype=np.int32)
arr_float = np.array([10.5,20.5,30.5],dtype=np.float64)
arr_string = np.array(["A","B","C"])

print("Integer Array:",arr_int)
print("Integer Data Type:",arr_int.dtype)

print("Float Array:",arr_float)
print("Float Data Type:",arr_float.dtype)

print("String Array:",arr_string)
print("String Data Type:",arr_string.dtype)


# Structure of NumPy array
arr = np.array([[1,2,3],[4,5,6]])

print("\nArray:")
print(arr)

print("Number of dimensions:",arr.ndim)
print("Shape:",arr.shape)
print("Size:",arr.size)
print("Data type:",arr.dtype)