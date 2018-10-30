from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np


# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=100000)
mean = sum(y) / len(y)
data_range = (min(y), max(y))
x = np.linspace(data_range[0], data_range[1], 100)


fig, ax = plt.subplots()
<<<<<<< HEAD
<<<<<<< HEAD
ax.hist(y, normed=True ,bins=90, range=(min(y) - 1,max(y)+1), color='yellow', label='o', histtype='stepfilled')
=======
ax.hist(y, normed=True ,bins=90, range=(min(y) - 1,max(y)+1), color='black', label='o', histtype='stepfilled')
>>>>>>> d
=======
ax.hist(y, normed=True ,bins=90, range=(min(y) - 1,max(y)+1), color='black', label='o', histtype='stepfilled')
>>>>>>> 105a052fda78670f089a7b8e783f7d88c5a4fd13
# plt.show()
plt.show()