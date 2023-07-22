n_points = 10
pie_angle = 360/n_points # angle of each slice
starting_angle = 90

fig, ax = plt.subplots()

for i in range(n_points):

    angle = starting_angle + i*pie_angle
    angle = math.radians(angle)
    x = math.cos(angle)
    y = math.sin(angle)

    ax.plot([x],[y], 'o', markersize = 17 - i)

ax.set_aspect('equal')
ax.axis('off')