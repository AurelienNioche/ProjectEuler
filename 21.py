def d(n):

    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a += [i, n//i]

    a.append(1)

    return a


def main():

    res = {}
    pairs = []

    for i in range(2, 10**4):

        r = sum(d(i))
        if r in res.keys() and res[r] == i:

            res.pop(r)
            pairs += [r, i]

        else:
            res[i] = r

    print(sum(pairs))
main()
