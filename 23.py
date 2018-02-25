import numpy as np
import itertools as it

def d(n):

    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a += [i, n//i]

    a.append(1)

    return np.unique(a)


def sum_d(n):

    assert n > 1

    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            other = n//i
            if other != i:
                s += other

    return s


def main():

    abundants = []

    s = 0

    print("find abundants")
    for i in range(2, 28124):

        if sum_d(i) > i:

            abundants.append(i)

    print("find possible sums")
    possible_s = []
    for j, k in it.combinations_with_replacement(abundants, r=2):
        possible_s.append(j+k)

    not_sum_of_two_abundants = np.setdiff1d(np.arange(28125), possible_s)
    print(sum(not_sum_of_two_abundants))

main()