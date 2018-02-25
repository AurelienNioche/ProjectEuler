def prime_number():

    a = 2
    pn = []
    while True:
        yield a
        pn.append(a)
        while True:
            prime = 1
            a += 1
            for i in pn:
                if a % i == 0:
                    prime = 0
                    break
            if prime:
                break

p = prime_number()
for i in range(10000):

    next(p)

print(next(p))