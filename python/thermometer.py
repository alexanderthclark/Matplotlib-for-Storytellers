temperature = 68

fig, ax = plt.subplots(figsize = (3,4))
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect('equal')
ax.axis('off')

bottom, height = .2, .6
fill_height = height * temperature/100

stem = plt.Rectangle((.44,bottom), .12, height,
                     facecolor = '.95',
                     edgecolor = '.2', linewidth = 2,
                     zorder = 1)
mercury = plt.Rectangle((.47,bottom), .06, fill_height,
                        facecolor = 'C3',
                        edgecolor = 'none', zorder = 2)
bulb = plt.Circle((.5,.16), .1,
                  facecolor = 'C3',
                  edgecolor = '.2', linewidth = 2,
                  zorder = 3)

for patch in [stem, mercury, bulb]:
    ax.add_patch(patch)

fill_top = bottom + fill_height
level = mpl.lines.Line2D([.57,.66], [fill_top,fill_top],
                         color = 'C3', linewidth = 2)
ax.add_line(level)

label = ax.text(.69, fill_top,
                fr'{temperature}$^\circ$F',
                va = 'center', size = 14)
label.set_color('C3')
