def check_value(numbers, value):
    check = lambda x: x in numbers

    if check(value):
        print("Value is present in the list")
    else:
        print("Value is not present in the list")


numbers=list(map(int, input("Enter list elements:").split()))
value=int(input("Enter value to search:"))
check_value(numbers,value)