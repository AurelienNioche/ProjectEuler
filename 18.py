import numpy as np

str_triangle = \
    "75 " \
    "95 64 " \
    "17 47 82 " \
    "18 35 87 10 " \
    "20 04 82 47 65 " \
    "19 01 23 75 03 34 " \
    "88 02 77 73 07 63 67 " \
    "99 65 04 28 06 16 70 92 " \
    "41 41 26 56 83 40 80 70 33 " \
    "41 48 72 33 47 32 37 16 94 29 " \
    "53 71 44 65 25 43 91 52 97 51 14 " \
    "70 11 33 28 77 73 17 78 39 68 17 57 " \
    "91 71 52 38 17 14 91 43 58 50 27 29 48 " \
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31 " \
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

n_levels = 15

# str_triangle = \
#     "3 " \
#     "7 4 " \
#     "2 4 6 " \
#     "8 5 9 3"


# Conceive the triangle as a list of lists

list_triangle = [int(i) for i in str_triangle.split(" ")]

triangle = []

n = 0
for i in range(n_levels):

    triangle.append(
        list_triangle[n: n + (i+1)]
    )
    n += (i+1)


# Compute the max you can have for each node beginning from the top

summed_triangle = [[triangle[0][0]]]

for i in range(1, n_levels):  # 'lines'

    summed_triangle.append(
        []
    )

    # if j == 0 (if that you are on the left border)
    summed_triangle[-1].append(
        summed_triangle[i - 1][0] + triangle[i][0]
    )

    for j in range(1, i):

        # Just keep a trace of the best solution
        summed_triangle[-1].append(
            max(summed_triangle[i - 1][j-1] + triangle[i][j],
                summed_triangle[i - 1][j] + triangle[i][j])
        )
    # if j == i (if that you are on the right border)
    summed_triangle[-1].append(
        summed_triangle[i - 1][-1] + triangle[i][i]
    )

print(max(summed_triangle[-1]))













