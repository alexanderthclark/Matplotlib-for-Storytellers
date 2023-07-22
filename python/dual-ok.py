fig, ax = plt.figure(), plt.axes()
ax2 = ax.twinx()

x = np.linspace(0,1,2)
ax.plot(x, x, label = 'a')
ax2.plot(x, 10-x,
         label = 'b',
         color = 'C2',
         linestyle = 'dotted',
         linewidth = 2)

ax.set_title("Title")

ax.set_xlabel("A Label")
ax.set_ylabel("Left Y Label\n(a)")
ax2.set_ylabel("Right Y Label\n(b)")

fig.legend(facecolor = 'lightyellow',
           bbox_to_anchor = (.5,.92),
           ncol = 2,
           loc = 'center',
           bbox_transform = ax.transAxes)