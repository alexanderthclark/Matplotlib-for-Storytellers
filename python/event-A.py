fig, ax = plt.figure(), plt.axes()
ax.set_aspect(1)
ax.set_xlim(-1.6,1.6)
ax.set_ylim(-1.1,1.4)
ax.axis('off')

# Add circles with color fill
left_circle = plt.Circle((-0.5, 0), 1,
                        edgecolor = 'black',
                        facecolor = 'gray',
                        linewidth = 2)
right_circle = plt.Circle((0.5, 0), 1,
                        edgecolor = 'black',
                        facecolor = (1, 1, 1, 0), # transparent
                        linewidth = 2,
                        zorder = 5)
ax.add_artist(left_circle)
ax.add_artist(right_circle)

# Labels
ax.text(0, 1.05,
       s = r"$A$",
       va = 'bottom',
       ha = 'center',
       size = 30)
ax.text(-1, 0,
       s = r'$A$',
       ha = 'right',
       va = 'center',
       size = 20)
ax.text(1, 0,
       s = r'$B$',
       ha = 'left',
       va = 'center',
       size = 20)