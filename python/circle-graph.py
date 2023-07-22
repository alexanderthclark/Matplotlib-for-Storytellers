fig, ax = plt.figure(), plt.axes()

n_points = 4

# Draw vertices
angles = np.linspace(0, 2*np.pi, n_points + 1)[0:n_points]
x = np.cos(angles)
y = np.sin(angles)
ax.plot(x, y,
        marker = 'o',
        linestyle = '',
        markersize = 13)

# Draw Edges
points = [p for p in zip(x,y)]
counter = 1
for point, other in combinations(points,2):

    x = [p[0] for p in (point, other)]
    y = [p[1] for p in (point, other)]
    ax.plot(x, y, zorder = -1)

    # add a label
    label_point = .65*np.array(point) + .35*np.array(other)

    run = x[1]-x[0]
    rotation = 90
    ha = 'left'
    if run != 0:
        line_slope = (y[1]-y[0])/(x[1]-x[0])
        rotation = math.atan(line_slope)
        rotation = math.degrees(rotation)
        ha = 'center'
    else:
        print(point, other, rotation)

    # get rgb then blend with white
    line_color = mpl.colors.to_rgb("C"+str(counter))
    lighter = .8*np.ones(3) + .2*np.array(line_color)
    ax.text(label_point[0], label_point[1],
            'label', rotation = rotation,
            bbox = dict(facecolor = lighter),
            va = 'center',
            ha = 'center'
           )
    counter += 1

ax.axis('off')
ax.set_aspect('equal')