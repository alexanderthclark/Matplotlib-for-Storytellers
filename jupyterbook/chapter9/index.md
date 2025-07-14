# Chapter 9: Math

In Part III (Poetry), we'll begin to treat Matplotlib more like a blank canvas. The complexity can evolve any number of ways, and one key complexity is the placement of items in a plot. Doing that well means understanding angles. So this math interlude guides us through trigonometry and some light linear algebra.

Some pieces of this chapter are unnecessary. `plt.Circle()` can be used to create a circle without any knowledge of trigonometry. Instead, we plot circles the old-fashioned way. We create a lot of points that, when connected, form a circle.

Why bother? Indeed, your Python interpreter won't be impressed if you know trigonometry. We shouldn't bother in every case, but math can compensate for a lack of matplotlib knowledge. I'd rather know a lot of math and a little matplotlib than a little math and a lot of matplotlib. Math is durable knowledge, useful in non-plotting contexts. A deeper understanding is also what allows us to create the color gradient in [Circular Arrangements](../chapter10/index.md#circular-arrangements), which can't be fashioned with a simple call to `plt.Circle()`.

## Circles

### The Unit Circle

The unit circle is the gem of pre-calculus. Understanding it is useful for plotting circles or arcs by hand (though one can also use Circle or Arc objects). It tells us how to relate angles to a particular point in the $xy$-plane. For a point on the unit circle at angle $\theta$ from the origin, we can find its coordinates as $(x,y) = (\cos(\theta), \sin(\theta))$.

Tracing a line from the origin to the point on the circle, we can create a right triangle as shown below.

```{figure} ../images/chapter9/unit-circle.png
:width: 70%
:align: center
```

```python
angles = np.linspace(0, 2*np.pi, 101)
x = np.cos(angles)
y = np.sin(angles)

fig, ax = plt.figure(figsize = (5,5)), plt.axes()
ax.set_aspect('equal')

# Make circle
ax.plot(x,y)

# Plot example right triangle
angle = np.pi/3

# make hypotenuse
ax.plot([0,np.cos(angle)], [0,np.sin(angle)],
        linestyle = 'dashed', color ='gray', linewidth = 2)#

# mark point on circle
ax.plot([np.cos(angle)], [np.sin(angle)],
        marker = 'o', color ='gray', markersize = 11)

# dashed lines for opposite and adjacent
ax.plot([0,np.cos(angle)], [0,0],
        linestyle = 'dashed', color ='gray', linewidth = 2)
ax.plot([np.cos(angle),np.cos(angle)], [0,np.sin(angle)],
        linestyle = 'dashed', color ='gray', linewidth = 2)

# Triangle side lengths
fontsize = 14
ax.text(0.5*np.cos(angle) - .02, 0.5*np.sin(angle)+.02,
        '1', rotation = math.degrees(angle), ha = 'center', va = 'bottom', size = fontsize)
ax.text(0.5*np.cos(angle), -.02, r"$\cos(\theta)$",
        rotation = 0, ha = 'center', va = 'top', size = fontsize)
ax.text(np.cos(angle) + .02, 0.5*np.sin(angle), r"$\sin(\theta)$",
        rotation = 0, ha = 'left', va = 'center', size = fontsize)


# make small arc and mark angle
x = np.cos(angles[angles<= angle])
y = np.sin(angles[angles<= angle])
ax.plot(0.2*x,0.2*y, color = 'black')
ax.text(0.2*np.cos(np.pi/10), 0.2*np.sin(np.pi/10),
        r" $\theta$", size = 14)

# clean appearance
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([-1, 1])
ax.set_yticks([-1, 1])
```

We can plot a circle or an arc from $\theta_1$ to $\theta_2$, by connecting the points $(\cos(\theta_1), \sin(\theta_1)), \dots, (\cos(\theta_2), \sin(\theta_2))$, where enough intermediate angles between $\theta_1$ and $\theta_2$ are included so the piecewise-linearity is smoothed out to give the appearance of a curve. In the next subsection, we consider how to do the same, but for non-unit circles.

### Non-unit Circles

The unit circle has a radius of one and it's centered at the origin. How do we obtain coordinates for other circles? There are two steps to change the radius and shift a circle off the origin.

1. **Change the radius.** Multiply the coordinates by the desired radius $r$.
2. **Shift the circle.** Add the desired horizontal and vertical shifts to the $x$ and $y$ coordinates, respectively.

These are ordered because the radius multiplier should not be applied to the added shift term. Below, we shrink the unit circle and move it up and along the 45-degree line.

```python
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

ax.spines[['top', 'right']].set_visible(False)

ax.set_xticks([-1, 1])
ax.set_yticks([-1, 0, 1])
```

```{figure} ../images/chapter9/unit-circle-shift.png
:width: 70%
:align: center
```

### Rotations and Ellipses

Now we jump from trigonometry to linear algebra. Matrices can represent transformations, like rotations or stretching. Applied to each point in a circle, a rotation that stretches $x$ and $y$ coordinates differently creates an ellipse.

A rotation of angle $\theta$ can be represented as
$$\left[ \begin{array}{cc}
    \cos \theta & -\sin \theta \\
    \sin \theta & \cos \theta
\end{array} \right].$$

Stretching the $x$-dimension by a scalar $r$ can be represented with
$$ \left[ \begin{array}{cc}
    r & 0 \\
    0 & 1 
\end{array} \right],$$

and the $y$-dimension is stretched by
$$ \left[ \begin{array}{cc}
    1 & 0 \\
    0 & r 
\end{array} \right].$$

Each of these matrices is applied point by point by left multiplying that point (as a $2\times 1$ column vector) by the transformation matrix,
$$ \begin{pmatrix}
     \tilde{x}  \\
     \tilde{y}
\end{pmatrix} = T \begin{pmatrix}
     x  \\
     y
\end{pmatrix}.$$

Below we take a circle and shrink it horizontally, stretch it vertically, and then rotate it. The $x$ values are multiplied by $\frac{1}{2}$, the $y$ values are multiplied by 2, and the angle of rotation is 45 degrees ($\frac{\pi}{4}$ radians). The transformation is constructed below.

```python
theta = np.pi / 4
rotation_matrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

x_scale = 0.5
x_stretch = np.matrix([[x_scale, 0], [0, 1]])

y_scale = 2
y_stretch = np.matrix([[1, 0], [0, y_scale]])

transformation = rotation_matrix * y_stretch * x_stretch
```

Below we plot a unit circle and then apply the transformation to create an ellipse.

```python
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
```

```{figure} ../images/chapter9/ellipse-tform.png
:width: 70%
:align: center
```

## Right Triangles

Right triangles are important to understand not for plotting right triangles necessarily, but for understanding the angle between any two points. The line segment connecting two points forms the hypotenuse of a right triangle, just as was seen in the unit circle.

For any angle $\theta$ in a right triangle that is not the right angle itself, we can speak of the sides opposite or adjacent to the angle. The side opposite is the side directly across from the angle. The side opposite the right angle is the hypotenuse (of length $c$ in Pythogoras' Theorem). The SOHCAHTOA mnemonic helps us understand how side lengths are related to the angles. More clearly written as SOH-CAH-TOA, as it stands for Sine Opposite Hypotenuse Cosine Adjacent Hypotenuse Tangent Opposite Adjacent and means

$$\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}$$
$$\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}$$
$$\tan \theta = \frac{\text{opposite}}{\text{adjacent}}$$

where $\theta$ is some angle of a triangle in radians and opposite, adjacent, and hypotenuse refer to the lengths of these sides.

By understanding these functions and their inverses, we can recover the angles in a plot. These functions are available from the `math` module as `sin()`, `cos()`, and `tan()`. Their inverses are `asin()`, `acos()`, and `atan()` for $\arcsin$, $\arccos$, and $\arctan$.

`math.atan()` is the most useful. Take two points and the slope $m$ of the line connecting them. Then $\arctan(m) = \theta$ is angle between those points, in radians.

```python
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
```

```{figure} ../images/chapter9/r-triangle.png
:width: 70%
:align: center
```