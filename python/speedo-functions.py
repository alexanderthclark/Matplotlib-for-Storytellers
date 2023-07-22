def rotation(theta):
    """Construct rotation matrix for angle theta in radians."""
    rotation_matrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return rotation_matrix


def speedometer(percentile, ax = None, fsize = 20):
    """Constructor speedometer plot along the half circle from 0 to pi."""
    # Make half circle from 0 to pi
    angles = np.linspace(0, np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    if ax is None:
        ax = plt.gca()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.plot(x,y, linewidth = 3, color = 'black')

    # Calculate angle for percentile
    theta = -np.pi * (percentile/100)

    # Draw hand initialized at 180 degrees
    length = 0.8
    base = np.matrix([0,0])
    tip = np.matrix([-length,0])
    points = [base,tip]
    new_points = [rotation(theta)*p.T for p in points]
    x = [np.array(p).flatten()[0] for p in new_points]
    y = [np.array(p).flatten()[1] for p in new_points]

    ax.plot(x,y, color = 'darkred',
            linewidth = 4, solid_capstyle = 'round')
    ax.plot(0,0, marker = 'o',
            color = 'darkred', markersize = 10)

    # Mark every 10pp
    ticks = np.linspace(0,180, 11)
    for angle in ticks: #np.arange(0,181, step = step):
        radians = math.radians(angle)

        # tick line
        x1, y1 = np.cos(radians), np.sin(radians)
        x2, y2 = .95*x1, .95*y1
        ax.plot([x1,x2], [y1,y2],
                color = 'black', zorder = -1)

        # place text label by tick
        raw = 180 - angle
        ptile = raw/180 * 100
        s = "{:.0f}%".format(ptile)
        ax.text(.9*x2, .9*y2, s,
                ha = 'center', zorder = -1)

    # ghost in the value bc why not
    # edit to include raw value or whatever desired
    ax.text(0.04, .15, '{:.0f}%'.format(percentile),
            va= 'bottom',
            ha = 'center',
            size = fsize,
            alpha = 0.2)