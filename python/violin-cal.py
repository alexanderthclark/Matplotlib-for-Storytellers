fig, ax = plt.figure(figsize = (8,5)), plt.axes()
spacing_scale = 2.5

for idx, day in enumerate(violin_practice):
    hit_target = violin_practice[day] >= 30

    facecolor = 'black' if hit_target else 'white'
    c = plt.Circle((idx*spacing_scale, 1),
                   radius = .4,
                   facecolor = facecolor,
                   edgecolor = 'black')
    ax.add_artist(c)
    ax.text(idx*spacing_scale, 0,
            s = day,
            ha = 'center',
            va = 'center')

# Eliminate Clutter
ax.set_aspect('equal')
ax.axis('off')

# Set plot window
ax.set_xlim([-1, 6*spacing_scale+1])
ax.set_ylim([0, 2])