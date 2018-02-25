def fibonacci():

    a = 1
    b = 1
    while True:
        yield a + b
        a, b = b, a+b

n = 3
fib = fibonacci()
while True:

    f = next(fib)
    if len(str(f)) == 1000:
        print("index", n)
        break
    n += 1
