fig, ax = plt.figure(), plt.axes()
ax2 = ax.twinx()

x = np.linspace(0,1,2)
ax.plot(x, x, label = 'a')
ax2.plot(x, 10-x, label = 'b')

ax.set_xlabel("A Label")

# This does nothing
ax2.set_xlabel("Label Attempt")

ax.set_ylabel("Left Y Label")
ax2.set_ylabel("Right Y Label")

ax.set_title("Positive Slope")
ax2.set_title("Negative Slope")

ax.legend()
ax2.legend()
fig.legend(facecolor = 'lightyellow')