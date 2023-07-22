# Create a circle of points
angles = np.linspace(0, 2*np.pi, 100)
x_vals = np.cos(angles)
y_vals = np.sin(angles)

# Begin plot
fig, ax = plt.subplots(1,2)

# simplify axes names
ax0, ax1 = ax[0], ax[1]

# Plot a circle
ax0.plot(x_vals, y_vals)

# Mark the y and x directions/axes
# vertical axis
height = 1.2
p1 = np.array([0,-height])
p2 = np.array([0,height])
points = [p1,p2]
x_vertical = [p[0] for p in points]
y_vertical = [p[1] for p in points]
ax0.plot(x_vertical, y_vertical)

# horizontal axis
width = height
p1 = np.array([height,0])
p2 = np.array([-height,0])
points = [p1,p2]
x_horiz = [p[0] for p in points]
y_horiz = [p[1] for p in points]
ax0.plot(x_horiz, y_horiz)

# Make Ellipse
new_points = [transformation * np.matrix(p).T for p in zip(x_vals,y_vals)]

new_x = [np.array(x).flatten()[0] for x in new_points]
new_y = [np.array(x).flatten()[1] for x in new_points]

# new vertical axis
new_vertical = [transformation * np.matrix(p).T for p in zip(x_vertical, y_vertical)]
new_x_vertical = [np.array(x).flatten()[0] for x in new_vertical]
new_y_vertical = [np.array(x).flatten()[1] for x in new_vertical]

# new horizontal axis
new_horiz = [transformation * np.matrix(p).T for p in zip(x_horiz, y_horiz)]
new_x_horiz = [np.array(x).flatten()[0] for x in new_horiz]
new_y_horiz = [np.array(x).flatten()[1] for x in new_horiz]

# Plot ellipse etc
ax1.plot(new_x, new_y)
ax1.plot(new_x_vertical, new_y_vertical)
ax1.plot(new_x_horiz, new_y_horiz)

# Change axes appearance
args = -2,2
for ax_ in ax0, ax1:
    ax_.set_xlim(args)
    ax_.set_ylim(args)
    ax_.set_xticks(np.linspace(*args,5))
    ax_.set_yticks(np.linspace(*args,5))
ax0.set_aspect('equal')
ax1.set_aspect('equal')