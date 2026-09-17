def intersection(arr1,arr2):
    common = list(filter(lambda x: x in arr2,arr1))

    print("Intersection =",common)

arr1 = list(map(int,input("Enter first array:").split()))
arr2 = list(map(int,input("Enter second array:").split()))

intersection(arr1,arr2)