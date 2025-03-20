# Alpha property
# mfc marker color

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
plt.plot(x,x, 'b--', lw=5)
plt.plot(x,x**2,'o-.g', ms = 8)
plt.plot(x,x**3, 'o-y', lw = 5, ms = 8, mfc='r',alpha=1 )

plt.show()
