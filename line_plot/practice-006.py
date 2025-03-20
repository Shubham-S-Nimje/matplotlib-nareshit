# Alpha property
# transperency  color 0 to 0.1

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
plt.plot(x,x, 'b--', alpha = 1.0)
plt.plot(x,x**2,'o-.g', alpha = 0.2)
plt.plot(x,x**3, 'o-y', alpha = 0.5)

plt.show()
