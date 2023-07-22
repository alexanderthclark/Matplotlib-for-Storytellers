x = np.linspace(-4, 4, 100_000)
y = stats.norm.pdf(x)
fig, ax = plt.figure(), plt.axes()
ax.set_aspect(5)

ax.plot(x,y, linewidth = 2, color = 'C0')
ax.fill_between(x,y, color = 'C0')

ax.set_yticks([])
for s in 'left', 'top', 'right':
    ax.spines[s].set_visible(False)

ylims = ax.get_ylim()
ax.set_ylim(0, ylims[1])
ax.set_title("Normal Distribution")