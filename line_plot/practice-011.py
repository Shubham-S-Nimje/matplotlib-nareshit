# creation of line plot by passing a single ndarray

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
i = x
s = x**2
c = x**3

# plt.plot(x, i, 'o-r')
# plt.plot(x, s, 'o-b')
# plt.plot(x, c, 'o-g')

# Shortcut way to plot
plt.plot(x,i,'o-r', x,s,'o-b', x,c,'o-g')

plt.title('One Graph, but multiple plots')

plt.show()