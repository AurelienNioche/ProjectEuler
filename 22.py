alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.upper()
print(alphabet)

letters_values = dict()

v = 1
for l in alphabet:

    letters_values[l] = v

    v += 1

with open("p022_names.txt", 'r') as f:

    names = sorted([i for i in f.read().replace('"', "").split(",")])

print(names)

s = 0
w = 1

for name in names:

    s += w*sum([letters_values[i] for i in name])

    w += 1

print(s)