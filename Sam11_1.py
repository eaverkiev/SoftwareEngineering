def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

count = 1
for number in fib(210):
    print(f"Число Фибоначчи №{count}: {number}")
    count += 1


