import numpy as np

s = 1000

first_limit = int(s/3) - 1
second_limit = int(s/2) - 1
third_limit = s - 2

for i in range(1, first_limit):
    j = i + 1
    while j <= second_limit and s >= i+j:
        k = j + 1
        while k <= third_limit and s >= i + j + k:

            if sum([i, j, k]) == s and sum(np.power([i, j], 2)) == k**2:

                print(i*j*k)
                break

            k += 1
        j += 1
