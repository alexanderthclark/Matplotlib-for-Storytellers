white = colorConverter.to_rgba('white', alpha = 0)
grey = colorConverter.to_rgba('gray', alpha = 0.8)

fig, ax = plt.figure(), plt.axes()

# point a
c = plt.Circle((0, 0), radius = 1, facecolor = white, edgecolor = 'black', alpha = 1)
ax.add_artist(c)
ax.plot([0],[0], marker = 'o', markersize = 3)
ax.text(0,0,'$a$', va = 'bottom', ha = 'left')

# point b
c = plt.Circle((0, 1), radius = 1, facecolor = white, edgecolor = grey)
ax.add_artist(c)
ax.plot([0],[1], marker = 'o', markersize = 3)
ax.text(0,1,'$b$', va = 'bottom', ha = 'left')

# Add point c
angle = math.asin(0.5)
c1 = math.cos(angle)
c2 = math.sin(angle)
ax.plot([c1],[c2], marker = 'o', markersize = 3)
ax.text(c1,c2,'$c$', va = 'bottom', ha = 'left')# = 1)
c = plt.Circle((c1, c2), radius = 1, facecolor = white, edgecolor = grey)
ax.add_artist(c)

# Where does d go?
ax.text(1.4,1.4,'$d$?', va = 'bottom', ha = 'left')

ax.axis('off')
ax.set_aspect('equal')

v = 2.1
ax.set_xlim([-1.1,v])
ax.set_ylim([-1.1,v])