import numpy as np

a = np.arange(1000)
cond = a % 5 == 0
cond2 = a % 3 == 0
print(np.sum(a[cond + cond2]))
