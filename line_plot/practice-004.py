# color property
# Color property
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
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o',  color='y')

plt.show()
