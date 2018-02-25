import numpy as np


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


n = 600851475143
# n = 13195

pn_gen = prime_number()

resp_dic = []

while True:

    pr = pn_gen.__next__()
    if pr > n:
        break

    pw = 1
    while True:

        if not n % pr ** pw:
            pw += 1
        else:
            pw -= 1
            if pw:
                resp_dic.append(pr**pw)
            break
    if np.product(resp_dic) == n:
        break

print(max(resp_dic))
#
# x = n
#
# while True:
#
#     n -= 1
#     if x % n == 0:
#         print(n)
#         break