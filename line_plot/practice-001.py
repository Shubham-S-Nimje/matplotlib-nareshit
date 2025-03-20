import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = x**2
plt.plot(x,y) #(1,1),(2,4),(3,9),.........
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.legend()

plt.show()
