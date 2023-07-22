fig, ax = plt.figure(facecolor = 'lightgray'), plt.axes()
x = np.linspace(0,2*np.pi,100)
ax.plot(x, np.sin(x), label = 'sine')
ax.plot(x, np.cos(x), label = 'cosine')
ax.plot(x, np.sin(x)**3, label = r'sine$^3$')

# Construct legend
ax.legend(bbox_to_anchor = (0.5,0),
          loc = 'lower center',
          bbox_transform = fig.transFigure)