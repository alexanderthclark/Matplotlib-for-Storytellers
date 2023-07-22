fig, ax = plt.figure(), plt.axes()
x = np.linspace(0,2*np.pi,100)

# Label in one go
ax.plot(x, np.sin(x), label = 'sine')

# Label as Artist method
cos, = ax.plot(x, np.cos(x))
cos.set_label('cosine')

# Label as Artist method
sine3 = ax.plot(x, np.sin(x)**3)
sine3[0].set_label(r'sine$^3$')

# Construct legend
ax.legend()