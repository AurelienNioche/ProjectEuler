n = 0
s = 0
while True:
    n += 1
    s += n
    d = 2
    for i in range(2, int(s**0.5)):
        if not s % i:
            d += 2
    if d >= 500:
        break
print(s)