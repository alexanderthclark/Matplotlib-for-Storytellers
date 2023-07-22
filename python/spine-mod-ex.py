x = np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title('Spine Mods')

%run ../../python/spine-mod.py