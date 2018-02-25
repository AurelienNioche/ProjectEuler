import itertools as it

n = 1
for i in it.permutations(range(10)):
    if n == 10**6:
        print("".join([str(j) for j in i]))

    n += 1