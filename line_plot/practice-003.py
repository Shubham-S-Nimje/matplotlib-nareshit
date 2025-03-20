# Linestyle property
# Line Styles:
# ------------------
#  character		description
# =========		==========
#     '-'				solid line style
#     '--'				dashed line style
#     '-.'				dash-dot line style
#     ':'				dotted line style


#     '-'				solid line style
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o',linestyle='-')

plt.show()

#     '--'				dashed line style
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o',linestyle='--')

plt.show()

#     '-.'				dash-dot line style
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o',linestyle='-.')

plt.show()

#     ':'				dotted line style
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.title('Square function line plot')
plt.xlabel('N value')
plt.ylabel('Square of N')
plt.plot(x,y,marker='o',linestyle=':')

plt.show()
