def fibonacci(n):
    a = 0
    b = 1

    fib = lambda x,y:x + y

    for i in range(n):
        print(a,end=" ")

        c = fib(a, b)
        a = b
        b = c

n = int(input("Enter number of terms:"))
fibonacci(n)