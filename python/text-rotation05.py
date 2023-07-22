x = np.linspace(0,10)
fig, ax = plt.figure(), plt.axes()
ax.plot(x,x)
ax.set_aspect(0.5)
ax.text(5,5,
       'Wello, horld!',
       rotation = 45)