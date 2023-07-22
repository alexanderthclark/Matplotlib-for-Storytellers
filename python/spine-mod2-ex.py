x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.figure(), plt.axes()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.set_title('Spine Mods')
%run -i ../../python/spine-mod2.py