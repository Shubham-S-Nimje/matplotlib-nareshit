# Marker property

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o') # o means circle

plt.show()
