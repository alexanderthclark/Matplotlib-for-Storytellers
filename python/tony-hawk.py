thetas = np.linspace(0,2*np.pi,8)[0:-1]
fig = plt.figure(figsize = (12,3))

# Set radius for skateboard wheels
radius = 0.1

# Make individual subplots
for key, theta in enumerate(thetas):
    rotation_matrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    # Create panel for one frame
    ax = fig.add_subplot(1, len(thetas), key+1)
    ax.set_aspect('equal')

    # Plot the loop itself
    angles = np.linspace(0, 2*np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    ax.plot(x,y)

    # Make skateboard wheels at bottom of the ramp
    # and then rotate them counter-clockwise according to theta
    centers = list()
    for ang in 1.5*np.pi, 1.6*np.pi:
        center = (1-radius)*np.cos(ang), (1-radius)*np.sin(ang)

        # rotate
        point = np.matrix(center).T
        rotated_point = rotation_matrix*point
        rotated_point = np.array(rotated_point).flatten()
        centers.append(rotated_point)

        # make wheel around new center
        wheel_x = radius*x + rotated_point[0]
        wheel_y = radius*y + rotated_point[1]

        ax.plot(wheel_x, wheel_y)

    # connect the two wheel centers
    c1, c2 = centers
    ax.plot([c1[0],c2[0]], [c1[1],c2[1]])

    ax.axis('off')

    xlim = ax.get_xlim()
    ax.plot(xlim, [-1,-1],
            color = 'C0',
            zorder = -1)