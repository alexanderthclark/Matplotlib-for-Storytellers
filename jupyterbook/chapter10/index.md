# Chapter 10: Applications

## Sloping Text

Suppose you'd like to label a line.

For a sloped line, you might rather the text sit parallel to the line instead of suffering the below.

```python
plt.plot([0,1], [0,1])
plt.text(0.65, 0.5,
         s = 'label',
         size = 30)

ax = plt.gca()
# Cosmetics
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
```

```{figure} ../images/chapter10/no-slope.png
:width: 60%
:align: center
```

The `rotation` argument can help if you know the right angle in degrees. Here the angle is 45 degrees or $\frac{\pi}{4}$ radians. So we modify the second line to be `plt.text(0.65, 0.5, 'label', size = 30, rotation = 45)`.

But this doesn't do what we want! The plot coordinate system is stretched, because we didn't call `ax.set_aspect('equal')` and `text` doesn't recalculate the text angle to make it align.

```{figure} ../images/chapter10/bad-slope.png
:width: 60%
:align: center
```

Now let's solve it for good in the general case, using trigonometry and then `transform_angles`. This is a method that we'll use with the transformation `ax.transData`. Try experimenting by replacing the `x2,y2` values to see this works for any angle.

```python
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
```

```{figure} ../images/chapter10/slope-label.png
:width: 60%
:align: center
```

## Circular Arrangements

With our knowledge of the unit circle, we can arrange some points in a circle with no additional help beyond the math package. This might be useful if you want to avoid mixing polar and Cartesian axes.

```python
n_points = 10
pie_angle = 360/n_points # angle of each slice
starting_angle = 90

fig, ax = plt.subplots()

for i in range(n_points):

    angle = starting_angle + i*pie_angle
    angle = math.radians(angle)
    x = math.cos(angle)
    y = math.sin(angle)

    ax.plot([x],[y], 'o', markersize = 17 - i)

ax.set_aspect('equal')
ax.axis('off')
```

This code produces the following.

```{figure} ../images/chapter10/circle.png
:width: 60%
:align: center
```

The below makes similar use of trigonometry to create a circle colored according to a gradient, like in [Chapter 6](../chapter6/index.md). I make use of `solid_capstyle = 'round'` to round the endpoints of the plotted line, creating a cleaner look compared to the default.

```python
# make a circle gradient
start_color = 255/256, 59/256, 48/256 # red
end_color = 255/256, 255/256, 85/256 # yellow

# How many color changes
segments = 130

# Create figure
fig, ax = plt.figure(figsize = (8,8)), plt.axes()

# Start at 90 degrees and return clockwise
angles = np.linspace(2.5*np.pi, np.pi/2, segments + 1)

# Create the intermediate colors
colors = dict()
for i in range(3):
    colors[i] = np.linspace(start_color[i], end_color[i], segments)

# plot each arc
for i in range(segments):

    start_angle = angles[i]
    end_angle = angles[i+1]
    angle_slice = np.linspace(start_angle, end_angle, 100)

    x_values = np.cos(angle_slice)
    y_values = np.sin(angle_slice)

    rgb = colors[0][i], colors[1][i], colors[2][i]

    ax.plot(x_values, y_values,
            color = rgb,
            linewidth = 20,
            solid_capstyle = 'round')

ax.set_aspect('equal')
ax.axis('off')
```

```{figure} ../images/chapter10/circle-grad.png
:width: 80%
:align: center
```

## Network Graphs

Networks are represented mathematically as graphs—a set of vertices and edges between them. In drawing a graph, there are many drawing algorithms available. For large networks or sophisticated algorithms, you should use something off the shelf in a package like [nxviz](https://nxviz.readthedocs.io/en/latest/index.html). For a small network, you might avoid dealing with NetworkX and nxviz and do the drawing yourself. We will work through two simple layouts: arc diagrams and a circular layout for an undirected graph.

An arc diagram places all points on a straight line. The links are drawn as arcs from one point to another.

Let's consider the complete graph with four vertices, where every pair is connected.

```python
fig, ax = plt.figure(), plt.axes()
x = np.linspace(0,1,4)
ax.plot(x, np.zeros(4),
        marker = 'o',
        linestyle = '',
        markersize = 13)

angles = np.linspace(0,np.pi,100)
for point in x:
    # connect other points
    other_x = x[x > point]
    # construct a half circle
    unit_x, unit_y = np.cos(angles), np.sin(angles)
    for other in other_x:
        # arc is centered between the two points
        shift = np.mean([point,other])
        r = (other - point)/2
        new_x = r*unit_x + shift
        new_y = r*unit_y
        ax.plot(new_x, new_y, zorder = -1)

ax.axis('off')
ax.set_aspect(1.5)
```

```{figure} ../images/chapter10/arc-graph.png
:width: 70%
:align: center
```

Next we move on to a circular layout. This layout places each vertex along a circle. Spaced evenly and with just four vertices in our graph, this will in fact produce a square. We also label each edge.

```python
fig, ax = plt.figure(), plt.axes()

n_points = 4

# Draw vertices
angles = np.linspace(0, 2*np.pi, n_points + 1)[0:n_points]
x = np.cos(angles)
y = np.sin(angles)
ax.plot(x, y,
        marker = 'o',
        linestyle = '',
        markersize = 13)

# Draw Edges
points = [p for p in zip(x,y)]
counter = 1
for point, other in combinations(points,2):

    x = [p[0] for p in (point, other)]
    y = [p[1] for p in (point, other)]
    ax.plot(x, y, zorder = -1)

    # add a label
    label_point = .65*np.array(point) + .35*np.array(other)

    run = x[1]-x[0]
    rotation = 90
    ha = 'left'
    if run != 0:
        line_slope = (y[1]-y[0])/(x[1]-x[0])
        rotation = math.atan(line_slope)
        rotation = math.degrees(rotation)
        ha = 'center'
    else:
        print(point, other, rotation)

    # get rgb then blend with white
    line_color = mpl.colors.to_rgb("C"+str(counter))
    lighter = .8*np.ones(3) + .2*np.array(line_color)
    ax.text(label_point[0], label_point[1],
            'label', rotation = rotation,
            bbox = dict(facecolor = lighter),
            va = 'center',
            ha = 'center'
           )
    counter += 1

ax.axis('off')
ax.set_aspect('equal')
```

```{figure} ../images/chapter10/circle-graph.png
:width: 83%
:align: center
```

## Tony Hawk's Vertical Loop

Tony Hawk became the first skateboarder to skate a vertical loop in 1998. We honor that accomplishment in two dimensions with the help of a rotation matrix. The unit circle is our vertical loop and we add two smaller circles to represent a skateboard. This is trigonometry. The small circles are placed along a ray from the origin of the unit circle to ensure they will lie tangent inside in the loop. In the first subplot, we place the skateboard at the bottom of the ramp. Though the same figure could be produced without using a rotation matrix, we use one so that the first subplot is essentially reused over and over by rotating the skateboard wheels up and around the loop.

```python
thetas = np.linspace(0,2*np.pi,8)[0:-1]
fig = plt.figure(figsize = (12,3))

# Set radius for skateboard wheels
radius = 0.1

# Make individual subplots
for key, theta in enumerate(thetas):
    rotation_matrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    # Create panel for one frame
    ax = fig.add_subplot(1, len(thetas), key+1)
    ax.set_aspect('equal')

    # Plot the loop itself
    angles = np.linspace(0, 2*np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    ax.plot(x,y)

    # Make skateboard wheels at bottom of the ramp
    # and then rotate them counter-clockwise according to theta
    centers = list()
    for ang in 1.5*np.pi, 1.6*np.pi:
        center = (1-radius)*np.cos(ang), (1-radius)*np.sin(ang)

        # rotate
        point = np.matrix(center).T
        rotated_point = rotation_matrix*point
        rotated_point = np.array(rotated_point).flatten()
        centers.append(rotated_point)

        # make wheel around new center
        wheel_x = radius*x + rotated_point[0]
        wheel_y = radius*y + rotated_point[1]

        ax.plot(wheel_x, wheel_y)

    # connect the two wheel centers
    c1, c2 = centers
    ax.plot([c1[0],c2[0]], [c1[1],c2[1]])

    ax.axis('off')

    xlim = ax.get_xlim()
    ax.plot(xlim, [-1,-1],
            color = 'C0',
            zorder = -1)
```

```{figure} ../images/chapter10/tony-hawk.png
:width: 100%
:align: center
```