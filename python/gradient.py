# Set Colors
green = 76, 217, 100
green = np.array(green)/255
blue = 90, 200, 250
blue = np.array(blue)/255

# How many color changes
segments = 100
interval_starts = np.linspace(0, 1, segments)

fig, ax = plt.subplots(figsize = (8,8))

colors = dict()
for i in range(3):
    colors[i] = np.linspace(blue[i], green[i], segments)

for i in range(segments-1):
    rgb = colors[0][i], colors[1][i], colors[2][i]
    x = interval_starts[i], interval_starts[i+1]
    y = (0.5, 0.5)
    ax.plot(x, y, color = rgb,
            linewidth = 20,
            solid_capstyle = 'round')

ax.set_aspect('equal')
ax.axis('off')