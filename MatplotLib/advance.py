import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# increase width and height of the graph

# to get more rows and collumns
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(3,2), dpi = 120)
# to take care of overlaps
axes[0].plot(x, y)
axes[0].set_title('First box')

axes[1].plot(y, x)
axes[1].set_title('Second box')
plt.tight_layout()
plt.show()


fig.savefig('my.jpg')
