# cutomize title

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
s = x**2

# Shortcut way to plot
plt.plot(x,s,'o-r')

# plt.title('Square Fuction Plot', {'color': 'b'})
# plt.title('Square Fuction Plot', color = 'b')
# plt.title('Square Fuction Plot', color = 'b', size=20)
# plt.title('Square Fuction Plot', color = 'r', size=20, backgroundcolor = 'yellow')
# plt.title('Square Fuction Plot', color = 'r', size=20, backgroundcolor = 'yellow', alpha = 1)
plt.title('Square Fuction Plot', color = 'b', size=20, fontdict='serif')

plt.show()
