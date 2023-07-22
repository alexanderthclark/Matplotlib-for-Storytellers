#data = np.random.normal(size = 30)
fig, ax = plt.figure(), plt.axes()
ax.hist(data, edgecolor = 'black')
ax.set_yticks([])
for s in 'left', 'top', 'right':
    ax.spines[s].set_visible(False)