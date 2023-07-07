fig, ax = plt.figure(), plt.axes()

x1, x2, y = 0.49, 0.51, 0.5
ax.scatter([x1,x2], [y,y])

va_options = ['top', 'bottom', 'center']
ha_options = ['left', 'right', 'center']

counter = 0 # for color cycling
for va in va_options:
    for ha in ha_options:
        # first letter of each option
        label = va[0] + "-" + ha[0]

        # assign label to point
        x = x1
        if 'c' in label:
            x = x2

        ax.text(x, y,
                label,
                va = va,
                ha = ha,
                fontsize = 20,
                color = 'C'+str(counter))
        counter += 1

ax.axis('off')