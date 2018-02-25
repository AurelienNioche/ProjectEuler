import numpy as np
from itertools import product

products = sorted(np.unique([i*j for i, j in product(np.arange(1, 1000), repeat=2)]), reverse=True)

for n in products:

    if str(n) == str(n)[::-1]:
        break
print(n)