fig, ax = plt.figure(), plt.axes()
ax2 = ax.twiny()

# Plot PDF
x = np.linspace(-3,3,200)
y = stats.norm.pdf(x)
ax.plot(x,y)

# Set x ticks for bottom x-axis
xticks = np.linspace(-2,2,6)
ax.set_xticks(xticks)

# Get corresponding CDF values for each tick
labels2 = list()
for tick in xticks:
    cumulative = stats.norm.cdf(tick)
    labels2.append(round(cumulative,2))

# Add ticks to top x-axis
ax2.set_xticks(xticks)
ax2.set_xticklabels(labels2, color = 'red')

# Clear y ticks
ax.set_yticks([])

# Set Limits
xlims = -3,3
ax2.set_xlim(xlims)
ax.set_xlim(xlims)

# Label and change color
ax.set_xlabel("Value")
ax2.set_xlabel("Percentile", color = 'red')
ax2.spines['top'].set_color('red')
ax2.tick_params(axis ='x', colors = 'red')