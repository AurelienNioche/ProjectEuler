def fact(x):

    y = 1
    while x > 1:
        y *= x
        x -= 1
    return y


def sum_of_digits(x):

    return sum([int(i) for i in str(x)])

print(sum_of_digits(fact(100)))