fig, ax = plt.figure(), plt.axes()

a = (1,2)
b = (7,6)

# rise over run
slope = (a[1] - b[1]) / (a[0] - b[0])
angle = math.atan(slope) # radians
degrees = math.degrees(angle)

top_angle = math

## add angle semi-circle
x = np.linspace(0, angle, 100)
ax.plot(0.5 * np.cos(x) + a[0],
         0.5 * np.sin(x) + a[1],
         color = 'black')
ax.text(0.5*np.cos(angle/2) + 1.1, 0.5*np.sin(angle/2) + 2,
        s = r"${:.1f}".format(degrees) + r"^{\circ}$")

# top slope measured relative to a 90-deg rotation
top_slope = (b[0]-a[0])/(b[1]-a[1])
top_angle = math.atan(top_slope)
x = np.linspace(1.5*np.pi, 1.5*np.pi - top_angle, 100)
ax.plot(0.5*np.cos(x) + b[0],
         0.5*np.sin(x) + b[1],
         color = 'black')
label_angle = 1.5*np.pi - top_angle/2
ax.text(0.5*np.cos(label_angle) + b[0] - 0.13, 0.5*np.sin(label_angle) + b[1] - 0.2,
        s = r"${:.1f}".format(math.degrees(top_angle)) + r"^{\circ}$",
       ha = 'center')


# points on left and top
ax.plot([a[0], b[0]], [a[1], b[1]], linestyle = '', marker = 'o', color = 'black')

# make a right triangle
ax.plot([a[0], b[0]], [a[1], b[1]], linestyle = 'dashed', marker = 'o', color = 'gray', zorder = -1)
ax.plot([a[0], b[0]], [a[1], a[1]], linestyle = 'dashed', color = 'gray', zorder = -1)
ax.plot([b[0], b[0]], [a[1], b[1]], linestyle = 'dashed', color = 'gray', zorder = -1)
ax.axis('off')