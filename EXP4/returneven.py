def even_list(a):
    b = []

    for x in a:
        if x % 2 == 0:
            b.append(x)

    return b
a = [1, 2, 3, 4, 5, 6, 7, 8]
print("New list =", even_list(a))