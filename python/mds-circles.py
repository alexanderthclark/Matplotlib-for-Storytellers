transparent = (1, 1, 1, 0)
grey = (.5, .5, .5, .8)

fig, ax = plt.subplots()

points = {'a': (0, 0),
          'b': (0, 1),
          'c': (np.sqrt(3)/2, .5)}

for label, point in points.items():
    edgecolor = 'black' if label == 'a' else grey
    circle = plt.Circle(point,
                        radius = 1,
                        facecolor = transparent,
                        edgecolor = edgecolor)
    ax.add_artist(circle)
    ax.plot(*point, marker = 'o',
            color = 'black', markersize = 3)
    ax.text(*point, f'${label}$',
            va = 'bottom', ha = 'left')

ax.text(1.4, 1.4, '$d$?',
        va = 'bottom', ha = 'left')

ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-1.1, 2.1)
ax.set_ylim(-1.1, 2.1)
