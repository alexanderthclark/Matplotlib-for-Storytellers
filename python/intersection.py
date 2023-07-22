fig, ax = plt.figure(), plt.axes()
ax.set_aspect(1)
ax.set_xlim(-1.6,1.6)
ax.set_ylim(-1.1,1.4)
ax.axis('off')

# Add Circles
k = 10_000
angles = np.linspace(0, 2*np.pi, k)
x = np.cos(angles)
y = np.sin(angles)
ax.plot(x - 0.5, y, color = 'black')
ax.plot(x + 0.5, y, color = 'black')

# fill circles in two pieces
x = np.cos(angles) - 0.5
t = 0
while x[t] > 0:
    t += 1
ax.fill_between(x[:t], -y[0:t], y[0:t],
                color = 'gray', zorder = -1)
ax.fill_between(-x[:t] , -y[0:t], y[0:t],
                color = 'gray', zorder = -1)

# Label
ax.text(0, 1.05,
       s = r"$A \cap B$",
       va = 'bottom',
       ha = 'center',
       size = 30)