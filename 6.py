import numpy as np

a = np.arange(1, 101)
b = np.sum(np.power(a, 2))
c = np.sum(a) ** 2
print(c-b)