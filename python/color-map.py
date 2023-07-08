# Set Colors
blue = mpl.colors.ColorConverter().to_rgb('C0')
orange = mpl.colors.ColorConverter().to_rgb('C1')

n_colors = 10
color_strings = dict()
for i in range(n_colors):
    color_strings[i] = 'C'+str(i)
segments = 1000 # How many color changes

fig, ax = plt.subplots(figsize = (14,8))

for c in range(n_colors - 1):
    color1 = mpl.colors.ColorConverter().to_rgb(color_strings[c])
    color2 = mpl.colors.ColorConverter().to_rgb(color_strings[c+1])

    interval_starts = np.linspace(c, c+1, segments)
    colors = dict()
    for i in range(3):
        colors[i] = np.linspace(color1[i], color2[i], segments)

    for i in range(segments-1):

        rgb = colors[0][i], colors[1][i], colors[2][i]

        x = interval_starts[i], interval_starts[i+1]
        y = [0.3,0.5]

        ax.plot(x, y,
                color = rgb,
                linewidth = 20,
                solid_capstyle = 'round')

    ax.text(c, .51,
            s = 'C'+str(c),
            va = 'bottom',
            size = 12,
            ha = 'center')

ax.text(9, .51,
        s = 'C9',
        va = 'bottom',
        size = 12,
        ha = 'center')

ax.set_aspect('equal')
ax.axis('off')