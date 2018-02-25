import numpy as np


def len_seq(d):
    remainders = []
    r = 10 % d
    remainders.append(r)

    while True:

        r = (r * 10) % d
        if r not in remainders:
            remainders.append(r)

        else:
            dec = len(remainders) - np.where(np.asarray(remainders) == r)[0][0]
            break

    return dec


def main():

    longest_recurring_cycle = 0

    max_len = 0

    d_with_max_len = -1

    for d in range(1000, 2, -1):

        if d < longest_recurring_cycle:
            break

        l = len_seq(d)

        if l > max_len:
            d_with_max_len = d
            max_len = l

    print(d_with_max_len, max_len)

main()