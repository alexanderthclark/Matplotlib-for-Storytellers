plt.plot([0,1], [0,1])
plt.text(0.65, 0.5,
         s = 'label',
         size = 30)

ax = plt.gca()
# Cosmetics
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])