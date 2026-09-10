def remove_duplicate(d):
    new={}
    for k, v in d.items():
        if v not in new.values():
            new[k]=v
    return new

d = eval(input("Enter dictionary:"))
print("After removing duplicates:", remove_duplicate(d))