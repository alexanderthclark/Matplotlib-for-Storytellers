x = np.linspace(0,2,2)
fig, ax = plt.figure(), plt.axes()

ax.plot(x,x)
ax.set_title("Title\n(with Padding)",
            fontsize = 'xx-large',
            weight = 'bold',
            color = 'purple',
            loc = 'left',
            pad = 10)