fig, ax = plt.figure(), plt.axes()
x, y = 0.5, 0.5
ax.scatter([x], [y])
ax.text(x,y, 'text', fontsize = 20)
ax.axis('off')