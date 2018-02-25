n = 2520

while True:
    success = 1
    for i in range(20, 0, -1):
        if n % i:
            n += 1
            success = 0
            break
    if success:
        break
print(n)