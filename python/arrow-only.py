fig, ax = plt.figure(),  plt.axes()

# no arrow, no text
# this does nothing
ax.annotate('',
            xy = (0.1, 0.8),
            xytext = (0.9, 0.9))

# arrow
ax.annotate('', xy = (0.2, 0.2),
            xytext = (0.8, 0.2),
            arrowprops = dict(color = 'black'))