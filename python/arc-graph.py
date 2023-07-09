fig, ax = plt.figure(), plt.axes()
x = np.linspace(0,1,4)
ax.plot(x, np.zeros(4),
        marker = 'o',
        linestyle = '',
        markersize = 13)

angles = np.linspace(0,np.pi,100)
for point in x:
    # connect other points
    other_x = x[x > point]
    # construct a half circle
    unit_x, unit_y = np.cos(angles), np.sin(angles)
    for other in other_x:
        # arc is centered between the two points
        shift = np.mean([point,other])
        r = (other - point)/2
        new_x = r*unit_x + shift
        new_y = r*unit_y
        ax.plot(new_x, new_y, zorder = -1)

ax.axis('off')
ax.set_aspect(1.5)