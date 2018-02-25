digit = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

tens_digit = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

first_two_digits = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

res = ""

for n in range(1, 1000):

    str_n = str(n)
    written_n = ""
    while True:

        if len(str_n) == 2:

            if str_n[0] == "1":
                written_n += first_two_digits[int(str_n)]
                break
            else:
                written_n += tens_digit[int(str_n[0])]
                str_n = str_n[-1]

        if len(str_n) == 1:
            written_n += digit[int(str_n)]
            break

        elif len(str_n) == 3:

            written_n += digit[int(str_n[0])] + "hundred"
            str_n = str_n[1:]

            if str_n == "00":
                break

            else:
                written_n += "and"

        else:
            break

    res += written_n
res += "onethousand"
print(len(res))