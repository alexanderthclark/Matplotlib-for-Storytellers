x = range(101)
# Create a Gaussian random walk starting at 0
start = np.zeros(1)
y1 = np.concatenate( [start,np.random.normal(0,1,100)] ).cumsum()
y2 = np.concatenate( [start,np.random.normal(0,1,100)] ).cumsum()

fig, ax = plt.figure(), plt.axes()
plt.tight_layout()
# Color arguments added to make defaults explicit
ax.plot(x,y1, color = 'C0')
ax.plot(x,y2, color = 'C1')

labels = ['Stock Performance: ', 'GenericCo', ' & ', 'PerfunctoryInc']
colors = ['black', 'C0', 'black', 'C1']
color_title(labels, colors)