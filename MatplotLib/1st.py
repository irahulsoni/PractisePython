import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 5, 11)
y = x ** 2

print(x)

# functional methord to do ploting:
# to add colour we added r-, r for red, g for green, so on..
# plt.plot(x,y, 'g-')
# to add labels to x and y
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')
# plt.show()
# plt.subplot(1,2,1)
# plt.plot(x,y,'r-')
#
# plt.subplot(1,2,2)
# plt.plot(y,x,'b-')
#

## object oriented methord:

# fig = plt.figure()
#
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)

fig = plt.figure()
            #bottom left, up from bottom, width, height,  must be betwwen 0 and 1
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.7, 0.1, 0.2, 0.2])
axes2.set_xlabel('X Label')
axes1.plot(x,y,'r')
axes2.plot(y,x,'b')
plt.show()


