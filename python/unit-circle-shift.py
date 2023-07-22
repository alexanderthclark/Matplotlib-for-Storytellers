angles = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.figure(), plt.axes()
ax.set_aspect('equal')

# Unit Circle
x = np.cos(angles)
y = np.sin(angles)
ax.plot(x, y, color = 'gray', linewidth = 1)

# Shifted
new_radius = 0.5
new_center = np.cos(np.pi/4)/2, np.sin(np.pi/4)/2
shift_x = new_radius*x + new_center[0]
shift_y = new_radius*y + new_center[1]
ax.plot(shift_x, shift_y, linewidth = 2)

%run ../../python/spine-mod.py

ax.set_xticks([-1, 1])
ax.set_yticks([-1, 0, 1])