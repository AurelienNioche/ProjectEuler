str_triangle = ""

n_levels = 0

with open("p067_triangle.txt", 'r') as f:

    for s in f.readlines():
        str_triangle += s + " "
        n_levels += 1

str_triangle = str_triangle[:-1]
print(str_triangle[-1])

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

    for j in range(1, i):  # 'columns'

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













