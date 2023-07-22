x = np.linspace(0,10)
fig, ax = plt.figure(), plt.axes()
ax.plot(x,x)
ax.set_aspect(2)
ax.text(5,5,
       'Hello, world!',
       rotation = 45)