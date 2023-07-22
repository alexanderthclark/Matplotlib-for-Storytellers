x = np.linspace(0,2,2)
fig, ax = plt.figure(), plt.axes()
ax.plot(x,x)

ax.set_title("Title",
             weight = 'bold',
             color = 'purple',
             pad = 24)

ax.text(0.5, 1.05,
        s = '(Parenthetical)',
        transform = ax.transAxes,
        ha = 'center')