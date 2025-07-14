# Chapter 6: Colors

Methods like `plot` and `text` include a color parameter, which we've already made use of. While you can get pretty far simply using `color = 'blue'`, you might also make use of colormaps or set your own colors using hex strings or RGB(A) tuples.

## 6.1 Colormaps

According to the style sheet you are using, there will be some colormap and you will cycle through those colors by default when plotting (but not for text). The colors can be identified by the strings `'C0'`, `'C1'`, ... If, as in the default, your color map has only 10 distinct colors, then the eleventh color `'C10'` is valid, but simply refers to `'C0'` and the colors cycle from there. You'll notice that with successive plot calls on the same axes, the colors will automatically move through the colormap. This is not the case with text, as is demonstrated in the program below.

```python
fig, ax = plt.figure(), plt.axes()
for i in range(12):
    # Plot color automatically cycles through color map
    ax.plot([0,1], np.ones(2)*i)

    # Text with default color on the left
    ax.text(0, i, 'C' + str(i),
    va = 'center', ha = 'right')

    # Text with variable color on the right
    ax.text(1, i, 'C' + str(i),
    va = 'center', ha = 'left',
    color = 'C'+str(i))
ax.axis('off')
```

![Colors](../images/chapter6/colors.png)

## 6.2 Red, Green, Blue, Alpha

An RGB color is given by three values, specifying the amount of red, green, and blue. In matplotlib, these values are between zero and one (you might also see RGB values between zero and 255 elsewhere). These colors live inside a cube, as a particular color is a triple $(r,g,b) \in [0,1]^3$.

![Color cube front](../images/chapter6/color-cube.png) ![Color cube back](../images/chapter6/color-cube-back.png)

I like working with RGB tuples because they can be manipulated with mathematical operations. Two colors can easily be averaged or we can create a gradient between two.

```python
# Set Colors
green = 76, 217, 100
green = np.array(green)/255
blue = 90, 200, 250
blue = np.array(blue)/255

# How many color changes
segments = 100
interval_starts = np.linspace(0, 1, segments)

fig, ax = plt.subplots(figsize = (8,8))

colors = dict()
for i in range(3):
    colors[i] = np.linspace(blue[i], green[i], segments)

for i in range(segments-1):
    rgb = colors[0][i], colors[1][i], colors[2][i]
    x = interval_starts[i], interval_starts[i+1]
    y = (0.5, 0.5)
    ax.plot(x, y, color = rgb,
            linewidth = 20,
            solid_capstyle = 'round')

ax.set_aspect('equal')
ax.axis('off')
```

![Gradient](../images/chapter6/gradient.png)

Any color can be made lighter by averaging it with white, $(1,1,1)$, or darker by averaging it with black $(0,0,0)$. We can also find the inverse of an RGB color by simply subtracting that triple from $(1,1,1)$. RGBA tuples are very similar, adding a fourth *a*lpha value for the opacity.

With RGB and RGBA colors being so handy, you might want to convert strings like `'C0'` into RGB. `ColorConverter()` lets us do this, with the `to_rgb()` and `to_rgba()` methods. Below, we create another color gradient between the default `'C0'` blue, to `'C1'` orange, and on to light blue `'C9'`.

```python
# Set Colors
blue = mpl.colors.ColorConverter().to_rgb('C0')
orange = mpl.colors.ColorConverter().to_rgb('C1')

n_colors = 10
color_strings = dict()
for i in range(n_colors):
    color_strings[i] = 'C'+str(i)
segments = 1000 # How many color changes

fig, ax = plt.subplots(figsize = (14,8))

for c in range(n_colors - 1):
    color1 = mpl.colors.ColorConverter().to_rgb(color_strings[c])
    color2 = mpl.colors.ColorConverter().to_rgb(color_strings[c+1])

    interval_starts = np.linspace(c, c+1, segments)
    colors = dict()
    for i in range(3):
        colors[i] = np.linspace(color1[i], color2[i], segments)

    for i in range(segments-1):

        rgb = colors[0][i], colors[1][i], colors[2][i]

        x = interval_starts[i], interval_starts[i+1]
        y = [0.3,0.5]

        ax.plot(x, y,
                color = rgb,
                linewidth = 20,
                solid_capstyle = 'round')

    ax.text(c, .51,
            s = 'C'+str(c),
            va = 'bottom',
            size = 12,
            ha = 'center')

ax.text(9, .51,
        s = 'C9',
        va = 'bottom',
        size = 12,
        ha = 'center')

ax.set_aspect('equal')
ax.axis('off')
```

![Color map](../images/chapter6/color-map.png)

### Color Cube Code

Here is the code for one of the RGB color cubes.

```python
from itertools import product
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

light_gray = [.98]*3
fig = plt.figure(figsize = (6,6),
                 facecolor = light_gray)
ax = plt.axes(projection='3d',
              facecolor = light_gray)

# control how many cubes/color changes
pieces = 10
grid = np.linspace(0, 1, pieces)[:-1]
width = grid[1] - grid[0]

# Make smaller cube units
for x in grid:
    for y in grid:
        for z in grid:
            vertices = list()
            for prod in product([x,x+width],[y,y+width], [z,z+width]):
                vertices.append(list(prod))

            faces = list()
            for key, face in enumerate([x,y,z]):
                # face is 0
                helper0 = [x for x in vertices if x[key] == face]
                helper1 = [x for x in vertices if x[key] == face + width]
                helper0.sort()
                helper0 = helper0[0:2] + helper0[::-1][0:2]
                helper1.sort()
                helper1 = helper1[0:2] + helper1[::-1][0:2]
                faces.append((helper0))
                faces.append(helper1)

            facecolor = (x + width / 2,
                         y + width / 2,
                         z + width / 2)
            pc = Poly3DCollection(faces,
                                  facecolor = facecolor,
                                  edgecolor = 'black')
            ax.add_collection3d(pc)

# Label Axes
ax.set_xlabel("Red")
ax.set_ylabel('Green')
ax.set_zlabel("Blue")

# Set Ticks
ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_zticks([0,1])
# Change padding
ax.xaxis.set_tick_params(pad = 0.1)
ax.yaxis.set_tick_params(pad = 0.1)
ax.zaxis.set_tick_params(pad = 0.1)
# Change azimuth
angle = 45 # + 180 # for second cube
ax.view_init(elev = None, azim = angle)
# Zoom out so labels are not cut off
ax.set_box_aspect([1,1,1], zoom = 0.86)
```