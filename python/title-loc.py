x = np.linspace(0,2,2)
fig, ax = plt.figure(), plt.axes()

ax.plot(x,x)
ax.set_title("Left Title",
            loc = 'left')
ax.set_title("Right Title",
            loc = 'right')
ax.set_title("I won't be long for this world.",
            loc = 'center')

# This only overwrites the center title above
ax.set_title("Center Title")