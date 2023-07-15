x = np.linspace(0,1,2)

fig1, ax = plt.figure(), plt.axes()
ax.plot(x, x)
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()

fig2, ax = plt.figure(), plt.axes()
ax.plot(x, 1 - x)
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()