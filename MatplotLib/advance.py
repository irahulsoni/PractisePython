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
axes[0].set_ylabel('Y axes')
axes[0].set_xlabel('X axes')

# change color, linewidth/ thickness, transparent / alpha, linestyle/ marker to mark the points on the line
#markerfacecolor: color of the marker, markeredgewidth, markeredgecolor

axes[1].plot(y, x, color='purple',linewidth=3,linestyle='-.',marker = 'o', markerfacecolor='yellow',markeredgewidth=2)
axes[1].set_title('Second box')

# if onlhy wanna show the graph between specific numbers: set xlim or ylim depending which one we need

axes[0].set_xlim([0,1])
plt.tight_layout()
plt.show()


fig.savefig('my.jpg')


# creating a legend, box with labels on the side:
# to change the location just change the loc from ranger 0 to 10: 0 means best, 10 means center

axes.plot(x,x**2, labels=' XSquare')
axes.plot(x, x**3, labels=' X cubed')
axes.legend()
