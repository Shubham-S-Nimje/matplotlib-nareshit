# Sequence of activity of plot function
# size of figure default 8 inch width and  6 inch height

import matplotlib.pyplot as plt
import numpy as np
plt.figure(num=1, figsize=(3,3), facecolor='yellow')
x = np.arange(1,11)
plt.plot(x,x, 'o-.r')

plt.show()
