# make a circle gradient
start_color = 255/256, 59/256, 48/256 # red
end_color = 255/256, 255/256, 85/256 # yellow

# How many color changes
segments = 130

# Create figure
fig, ax = plt.figure(figsize = (8,8)), plt.axes()

# Start at 90 degrees and return clockwise
angles = np.linspace(2.5*np.pi, np.pi/2, segments + 1)

# Create the intermediate colors
colors = dict()
for i in range(3):
    colors[i] = np.linspace(start_color[i], end_color[i], segments)

# plot each arc
for i in range(segments):

    start_angle = angles[i]
    end_angle = angles[i+1]
    angle_slice = np.linspace(start_angle, end_angle, 100)

    x_values = np.cos(angle_slice)
    y_values = np.sin(angle_slice)

    rgb = colors[0][i], colors[1][i], colors[2][i]

    ax.plot(x_values, y_values,
            color = rgb,
            linewidth = 20,
            solid_capstyle = 'round')

ax.set_aspect('equal')
ax.axis('off')