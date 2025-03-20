# color property
# character  color
# ========  ======
#     'b'          blue
#     'g'          green
#     'r'          red
#     'c'          cyan
#     'm'         magenta
#     'y'          yellow
#     'k'          black
#     'w'          white

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
plt.plot(x,x, 'b--')
plt.plot(x,x**2,'o-.g')
plt.plot(x,x**3, 'o-y')
# plt.plot(x,x**4, '#0F0F0F')

plt.show()
