# Alpha property
# line width

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
plt.plot(x,x, 'b--', lw=10)
plt.plot(x,x**2,'o-.g', ms = 15)
plt.plot(x,x**3, 'o-y', lw = 10, ms = 15)

plt.show()
