fig, ax = plt.figure(), plt.axes()
x = np.linspace(-4,4, 100_000)
norm_pdf = stats.norm.pdf(x)
ax.plot(x, norm_pdf)
ax.set_title("Sampling Distribution")

# Clean background elements
ax.set_yticks([])
for s in 'left', 'top', 'right':
    ax.spines[s].set_visible(False)

# Start y-axis at 0
ylims = ax.get_ylim()
ax.set_ylim(0, ylims[1])

# Set x-axis ticks and labels
ax.set_xticks([-1, 0,1])
ax.set_xticklabels([r"$-\bar{x}$", r'$\mu$', r'$\bar{x}$'])

# Vertical dashed line
x0 = 0,0
y0 = [0,stats.norm.pdf(0)]
ax.plot(x0, y0, linestyle = 'dashed', color = 'gray')

# Fill area for a more extreme sample mean
x_right = x[x > 1]
y_right = norm_pdf[-len(x_right):]
ax.fill_between(x_right, y_right)

x_left = x[x < -1]
y_left = norm_pdf[:len(x_left)]
ax.fill_between(x_left, y_left, color = 'C0')