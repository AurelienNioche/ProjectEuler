def f(x):

    if not x % 2:
        return x//2
    else:
        return 3*x + 1


length_dic = {}
max_length = 0
r = - 1

for i in range(1, 10**6):

    starting_n = i
    n = starting_n
    length = 1

    while n != 1:

        if n in length_dic.keys():

            length += length_dic[n] - 1  # Remove the first number that has already been counted.
            break

        else:
            n = f(n)
            length += 1

    length_dic[starting_n] = length

    if length > max_length:
        max_length = length
        r = starting_n

print(r)
