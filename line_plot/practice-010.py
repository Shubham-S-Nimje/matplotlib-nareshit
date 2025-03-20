# Sequence of activity of plot function
# how to save line plot to file savefig()

import matplotlib.pyplot as plt
import numpy as np
plt.figure(num=1, figsize=(3,3), facecolor='yellow')
x = np.arange(1,11)
plt.plot(x,x, 'o-.r')

plt.savefig('D:\\Learning\\matplotlib-nareshit\\line_plot\\save-figure\\practice-010.png')
