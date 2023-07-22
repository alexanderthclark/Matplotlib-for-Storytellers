fig, ax = plt.figure(edgecolor = 'black'), plt.axes()
ax.set_aspect(1)
ax.set_xlim(-1.6,1.6)
ax.set_ylim(-1.1,1.4)
ax.axis('off')

# Add circles with color fill
left_circle = plt.Circle((-0.5, 0), 1,
                        edgecolor = 'black',
                        facecolor = 'gray',
                        linewidth = 2)
left_circle_helper = plt.Circle((-0.5, 0), 1,
                        edgecolor = 'black',
                        facecolor = (1,1,1,0),
                        linewidth = 2)
right_circle = plt.Circle((0.5, 0), 1,
                        edgecolor = 'black',
                        facecolor = 'white',
                        linewidth = 2)
ax.add_artist(left_circle)
ax.add_artist(right_circle)
ax.add_artist(left_circle_helper)

# Label
ax.text(0, 1.05,
       s = r"$A \cap B^C$",
       va = 'bottom',
       ha = 'center',
       size = 30)