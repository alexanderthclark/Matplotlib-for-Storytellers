x1, y1 = 0, 0
x2, y2 = 1, 1
x = (x1, x2)
y = (y1, y2)

# plot
fig, ax = plt.figure(), plt.axes()
ax.plot(x,y)

# Find angles and then insert text
slope = (y2 - y1) / (x2 - x1)
true_angle = math.degrees(math.atan(slope))

# dummy_array is the point where the angles are anchored
dummy_array = np.array([[0,0]]) # doesn't matter what pair you use
# matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform_angles

plot_angle = ax.transData.transform_angles(
                            np.array((true_angle,)),
                            dummy_array)[0]

ax.text(np.mean(x), np.mean(y),
        s = 'label',
        rotation = plot_angle,
        fontsize = 30,
        va = 'top',
        ha = 'center')

ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
print(true_angle, plot_angle)