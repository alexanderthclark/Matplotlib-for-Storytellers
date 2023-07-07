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

ax.text(0.4, 1.05, ' GenericCo',
        transform = ax.transAxes,
        ha = 'left',
        fontsize = 13,
        color = 'C0')

ax.text(0.4, 1.05, 'Stock Performance:',
        transform = ax.transAxes,
        ha = 'right',
        fontsize = 13,
        color = 'black')

ax.text(0.64, 1.05, '&',
        transform = ax.transAxes,
        ha = 'right',
        fontsize = 13,
        color = 'black')

ax.text(0.64, 1.05, ' PerfunctoryInc',
        transform = ax.transAxes,
        ha = 'left',
        fontsize = 13,
        color = 'C1')