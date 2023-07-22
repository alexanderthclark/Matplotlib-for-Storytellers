fig = plt.figure(figsize=(12,6))
spec = gridspec.GridSpec(ncols=4,
                         nrows=2,
                         figure=fig)
x = np.random.normal(0, 10, size = 300)
y = x**2 + np.random.normal(0, 100, size = 300)

ax1 = fig.add_subplot(spec[0, 0:3])
ax1.plot(x, y,
         linestyle='None',
         marker='.',
         alpha=0.5)

ax2 = fig.add_subplot(spec[0, 3:4], sharey = ax1)
ax2.hist(y, orientation='horizontal', bins=40)

ax3 = fig.add_subplot(spec[1, 0:3], sharex = ax1)
ax3.hist(x, bins = 40)
ax3.invert_yaxis()
plt.tight_layout()