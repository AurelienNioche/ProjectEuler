limit = 2 * 10 ** 6
# limit = 10

s = 0

a = 2
pn = []

prime = 1

while a < limit:

    if prime:
        pn.append(a)
        s += a

    prime = 1
    a += 1
    for i in pn:
        if a % i == 0:
            prime = 0
            break
        elif i > a**0.5:
            break
print(s)
