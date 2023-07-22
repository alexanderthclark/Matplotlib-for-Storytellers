fig, ax = plt.figure(), plt.axes()
for i in range(12):
    # Plot color automatically cycles through color map
    ax.plot([0,1], np.ones(2)*i)

    # Text with default color on the left
    ax.text(0, i, 'C' + str(i),
    va = 'center', ha = 'right')

    # Text with variable color on the right
    ax.text(1, i, 'C' + str(i),
    va = 'center', ha = 'left',
    color = 'C'+str(i))
ax.axis('off')