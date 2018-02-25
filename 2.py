import numpy as np

i = 0
n = [1, 2]
while True:
    i = sum(n[-2:])
    if i > 4*10**6:
        break
    else:
        n.append(i)

n = np.asarray(n)
print(np.sum(n[n % 2 == 0]))
