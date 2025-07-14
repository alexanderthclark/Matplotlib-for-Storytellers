# Chapter 3: Plot Elements and Coordinate Systems

This chapter can be skipped by the reader in a hurry. I include it to establish some vocabulary about the basic plot elements and then discuss the different coordinate systems that can be used within a single plot—not polar vs. Cartesian coordinates but data coordinates vs. figure coordinates, for example. Coordinate systems do come up repeatedly in future chapters.

## 3.1 Primitives and Containers

Once you have a your figure and axis objects, you'll want to add actual plot elements to them, lines for a line chart, bars for a bar chart, annotations, etc. We already did that in Chapter 1, creating line plots. In matplotlib, these elements belong to the Artist class, it being a very general base class. Artists objects are basically the water you've been swimming in this whole time—you just might not have noticed it. Artist objects can be either primitives or containers. Containers include background items like the figure and axes objects. Primitives are the meat of the plot, like the line created by a call to `ax.plot()`. Important primitive Artist objects include Line2D, Patches, and Text.

```python
# Make a patch, line, and text.
fig, ax = plt.figure(), plt.axes()

rectangle = Rectangle((.2, .2), width = .3, 
            height = .3, color = 'green')
ax.add_patch(rectangle)

x = np.linspace(0,1,10)
y = x**2
line, = ax.plot(x, y)

ax.text(0.5, 0.8, 'These are artists', 
            ha = 'center', fontsize = 15)

# Get the colors
for artist in rectangle, line:
    print(artist, artist.get_color())
```

![Artists](../images/chapter3/artists.png)

What might be unusual in the above is that we don't simply run `ax.plot(x, y)`. Instead we actually assign the plot call to a variable, `line, = ax.plot(x,y)`. Usually, this isn't necessary, but this allows us to reference the same object later in the program. The plot method creates a tuple of Line2D objects. In this case, that tuple contains only one item and it is assigned to the variable `line`.

Now that we have the object as `line`, we can get properties or make changes. You can obtain the color with the `get_color()` method or change it with `set_color()`. You can even remove the plot element with `line.remove()`. These are all niche uses. However, we will later make use of `remove()` when iteratively centering text. We'll also use the `get_window_extent()` artist method frequently to help space objects in the plot.

### 3.1.1 Ordering with `zorder`

#### Default Ordering

By default, text is plotted over lines and lines are plotted over patches, like the fill created by `fill_between()`. Within each of these three categories, objects created later in the program are plotted over previously created objects. The `zorder` parameter can be used to create a different ordering. Objects with a greater `zorder` value are ordered further to the front.

First, we create and plot without specifying the `zorder` for any object to observe default behavior. We also print the zorder for each object using `get_zorder()`. Text has a `zorder` of 3, lines have a `zorder` of 2, and each patch object will have `zorder = 1`. Note `patch1` and `patch2` have the same `zorder`, but the red `patch2` is added later in the program so it is plotted over the green `patch1`, being as if `patch1` has a lower `zorder`.

```python
fig, ax = plt.figure(), plt.axes()

# Create patches
patch1 = Rectangle((0.1, 0.1), 0.5, 0.5, 
                   facecolor = 'green')
patch2 = Rectangle((0.4, 0.4), 0.5, 0.5, 
                   facecolor = 'red', alpha = 0.7)
ax.add_patch(patch1)
ax.add_patch(patch2)

# Create lines
line1, = ax.plot([0.05, 0.35], [0.1, 0.9], 
                 'violet', linewidth = 10)
line2, = ax.plot([0.65, 0.95], [0.1, 0.9], 
                 'darkviolet', linewidth = 10)

# Create text
text = ax.text(0.5, 0.5, 'Hello World', 
               fontsize = 30, ha = 'center')

# Print out the zorders
for artist in [patch1, patch2, line1, line2, text]:
    print(artist, artist.get_zorder())
```

![Default z-order](../images/chapter3/default-z.png)

#### Custom Ordering

Then, we reverse the ordering.

```python
fig, ax = plt.figure(), plt.axes()

# Create patches
patch1 = Rectangle((0.1, 0.1), 0.5, 0.5, 
                   facecolor = 'green',
                   zorder = 5) # highest
patch2 = Rectangle((0.4, 0.4), 0.5, 0.5, 
                   facecolor = 'red', alpha = 0.7,
                   zorder = 4)
ax.add_patch(patch1)
ax.add_patch(patch2)

# Create lines
line1, = ax.plot([0.05, 0.35], [0.1, 0.9], 
                 'violet', linewidth = 10,
                 zorder = 3)
line2, = ax.plot([0.65, 0.95], [0.1, 0.9], 
                 'darkviolet', linewidth = 10,
                 zorder = 2)

# Create text
text = ax.text(0.5, 0.5, 'Hello World', 
               fontsize = 30, ha = 'center',
               zorder = -1) # Put the text on bottom

# Print out the zorders
for artist in [patch1, patch2, line1, line2, text]:
    print(artist, artist.get_zorder())
```

![Reverse z-order](../images/chapter3/reverse-z.png)

#### Axes and Tick Ordering

Notice that by default, gridlines are ordered below artists added to a plot regardless of where the call to show the gridlines is placed. This can be changed using `ax.set_axisbelow()`, which also reorders the ticks. The `XAxis` and `YAxis` can be ordered independently using the `set_zorder()` axis method.

```python
fig, ax = plt.figure(), plt.axes()

# Create patches
patch1 = Rectangle((0.1, 0.1), 0.5, 0.5, 
                   facecolor = 'green', alpha = 0.7,
                   zorder = 2) 
patch2 = Rectangle((0.4, 0.4), 0.5, 0.5, 
                   facecolor = 'red', alpha = 0.7,
                   zorder = 1)
ax.add_patch(patch1)
ax.add_patch(patch2)

ax.grid(True, zorder = 0.5, linewidth = 2)
ax.set_title("Default axes")
```

![Default axes](../images/chapter3/default-axes.png)

```python
fig, ax = plt.figure(), plt.axes()

# Create patches
patch1 = Rectangle((0.1, 0.1), 0.5, 0.5, 
                   facecolor = 'green', alpha = 0.7,
                   zorder = 2) 
patch2 = Rectangle((0.4, 0.4), 0.5, 0.5, 
                   facecolor = 'red', alpha = 0.7,
                   zorder = 1)
ax.add_patch(patch1)
ax.add_patch(patch2)

ax.grid(True, zorder = 0.5, linewidth = 2)
ax.set_axisbelow(False)
ax.set_title("set_axisbelow(False)")
```

![Front axes](../images/chapter3/front-axes.png)

```python
fig, ax = plt.figure(), plt.axes()

# Create patches
patch1 = Rectangle((0.1, 0.1), 0.5, 0.5, 
                   facecolor = 'green', alpha = 0.7,
                   zorder = 2) 
patch2 = Rectangle((0.4, 0.4), 0.5, 0.5, 
                   facecolor = 'red', alpha = 0.7,
                   zorder = 1)
ax.add_patch(patch1)
ax.add_patch(patch2)

ax.grid(True, zorder = 0.5, linewidth = 2)
ax.set_axisbelow(True)
ax.xaxis.set_zorder(10)
ax.set_title("xaxis set_zorder(10)")
```

![Front x-axis](../images/chapter3/front-xaxis.png)

## 3.2 Coordinate Systems and Transformations

So far we have worked with data coordinates and you might not even realize there could be anything else. When we plotted a line between the points $(0,0)$ and $(1,1)$, we meant those as values in the usual $xy$-plane. But with use of transformations, we might also plot according to axes, figure, and display coordinates. In axes coordinates, $(0,0)$ is the bottom left of the axes and $(1,1)$ is the top right. Similarly, in figure coordinates, $(0,0)$ is the bottom left of the figure and $(1,1)$ is the top right. We won't cover the fourth type, display coordinates, which is the pixel coordinate system (for certain backends). The matplotlib [documentation](https://matplotlib.org/stable/tutorials/advanced/transforms_tutorial.html) cautions that you should rarely work with display coordinates. However, display coordinates are a necessary evil when converting from one system to another. Note, it is important not to manipulate the figure or axes dimensions after referencing the display coordinate system or you might encounter unexpected behavior.

The plot below features a group of plot calls using axes coordinates, then a group using figure coordinates, and then a single call using data coordinates.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_xlim(0,10)
ax.set_ylim(0,10)

# Axes coordinates
ax.plot([0.1, 0.9], [0.2, 0.2], linewidth = 4,
        transform = ax.transAxes, color = 'red')
ax.text(0.5, 0.2, "Axes Coords", ha = 'center', 
        va = 'bottom', transform = ax.transAxes)

# Figure coordinates
ax.plot([0.1, 0.9], [0.5, 0.5], linewidth = 4,
        transform = fig.transFigure, color = 'blue')
ax.text(0.5, 0.5, "Figure Coords", ha = 'center', 
        va = 'bottom', transform = fig.transFigure)

# Data coordinates
ax.plot([1, 9], [8, 8], linewidth = 4,
        color = 'green')
ax.text(5, 8, "Data Coords", ha = 'center', 
        va = 'bottom')
```

![Coordinate systems](../images/chapter3/coords.png)

Axes and figure coordinates are often useful when you would like placement to be independent of the data, perhaps to enforce that something remain in the center of the plot by using an axes coordinate of 0.5. Below, we make use of that to set a vanishing point at the vertical halfway point.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.tick_params(labelbottom = False, 
               labelleft = False)

# Add lines using different coordinates 
# to create a horizon/vanishing point
x = 0.5
y = 0.5

#  Use ax.transAxes
for i in np.arange(0, 1.2, 0.2):
    ax.plot([i, x], [0, y], transform = ax.transAxes, 
            color = 'black', linewidth = 0.5)

# Fill half the plot to give a horizon
ax.fill_between([0,1], [0,0], [y, y], 
                transform = ax.transAxes, 
                color = 'lightyellow')
ax.fill_between([0,1], [y,y], [1, 1], 
                transform = ax.transAxes, 
                color = 'lightblue')

ax.set_title("A Horizon using Axes Transform")
```

![Coordinate horizon](../images/chapter3/coord-horizon.png)

We can convert a point or sequence of points from one coordinate system to another using the appropriate transform object. `ax.transData.transform([x,y])` converts `x,y` from data coordinates to display coordinates. Simply replacing `ax.transData` with `ax.transAxes` or `fig.transFigure` converts from the corresponding coordinate system to display coordinates. The opposite direction is achieved by inverting the transformation—`ax.transData.inverted().transform([x,y])`. To go from data coordinates to figure or axes coordinates, you can make a pit stop in display coordinates. For example, `ax.transData.inverted().transform(ax.transAxes.transform([0.5, 0.5]))` returns the middle of the axes window in data coordinates. The example below breaks this up into two steps. Again, take note that all plotting is done after setting a tight layout and after setting the axes limits to avoid resizing the figure and endangering the reliability of our coordinate transformations.

```python
fig, ax = plt.figure(), plt.axes()
plt.tight_layout()

ax.set_xlim(-10,10)
ax.set_ylim(0,50)

# Transform (0.5, 0.5) from axes to display coords
x_a, y_a = 0.5, 0.5
x_display, y_display = ax.transAxes.transform([x_a, y_a])

# Transform to data coordinates
x_d, y_d = ax.transData.inverted().transform([x_display, y_display])

# These three points should be the same place
ax.plot(x_a, y_a, 'o', transform = ax.transAxes,
        color = 'C0', markersize = 10, label = 'Axes')
ax.text(x_a + 0.1, y_a, f"({x_a}, {y_a})", 
        transform = ax.transAxes)

ax.plot(x_d, y_d, 'x', color = 'C1', markersize = 10,
        label = 'Data')
ax.text(x_d + 2, y_d, f"({x_d}, {y_d})")

ax.legend()
ax.set_title("Transform from Axes Coords to Data Coords")
```

![Coordinate transformations](../images/chapter3/coord-trans.png)

## 3.3 Use Window Extents

Another useful method is `get_window_extent()`, which allows you to find the bounding box (the coordinates for the corners of the enclosing rectangle) for something added to a plot. This can be used to find the display coordinates for where an annotation begins or ends, for example. Like in the previous section, note that the results will not update and be inaccurate if changes are made to the figure size, axes limits, or the canvas used. The method also requires a renderer. The technicalities for why can be put aside. Either include `fig.canvas.draw()` first, so the rendered is already cached, or include the argument `renderer = fig.canvas.get_renderer()` in the call to `get_window_extent()`. Below is a simple example. We create a text object with the axes method `ax.text()` in the normal way, but we take the atypical step of assigning the object to a variable. Below, that variable is named `center_text` and then we call `get_window_extent()` as a Text method, or an Artist method more abstractly.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

# Create a text object
center_text = ax.text(0, 0, 'Centered Text', 
                      ha = 'center', fontsize = 20)

# Draw the canvas so the renderer is cached
fig.canvas.draw()

# Get the bounding box in display coordinates
bbox = center_text.get_window_extent()

# Convert the corner points to data coordinates
corners_display = bbox.corners()
corners_data = ax.transData.inverted().transform(corners_display)

# Draw vertical lines at the text boundaries
for x, y in corners_data:
    ax.axvline(x, color = 'gray', linewidth = 0.5)
ax.set_title("Bounding Box of Text")
```

![Window extent](../images/chapter3/window-extent.png)

So what? A formatted title can stand in for a legend, helping reduce clutter. This helps us heed the call from Schwabish (2021) to label data directly and avoid legends when possible. In the line chart below, a legend is unnecessary given the color-coding in the title. We create a title not with the typical `ax.set_title()` but with a series of `ax.text()` calls. There are several because a single Text object can't have multiple colors. The `ha` parameter is for horizontal alignment, and this is covered in more detail in a later chapter. By using `ha = 'left'`, the text will begin at the given $x$ and $y$ coordinates.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_xlim(0,1)
ax.set_ylim(0,1)

# Plot lines
dates = ['2020', '2021', '2022']
stock_a = [100, 120, 115]
stock_b = [100, 110, 105]

ax.plot(dates, stock_a, color = 'red')
ax.plot(dates, stock_b, color = 'blue')

# Estimate placement for the title
# Place "Stock" at the center
y = 1.02
text1 = ax.text(0.5, y, 'Stock ', 
                transform = ax.transAxes,
                ha = 'center', fontsize = 14)
                
# Cache the renderer
fig.canvas.draw()

# Place the next segment
bbox = text1.get_window_extent()
# Transform to axes coordinates
w = ax.transAxes.inverted().transform(bbox.corners())
# w[0] and w[1] give the bottom left and right corners
# Take the right corner x value
x_next = w[1][0]
text2 = ax.text(x_next, y, 'A', 
                transform = ax.transAxes,
                ha = 'left', fontsize = 14,
                color = 'red')

# Now figure out where to place the rest
del text1, text2 # remove and start again
ax.clear()
ax.plot(dates, stock_a, color = 'red')
ax.plot(dates, stock_b, color = 'blue')
ax.set_ylim(90, 130)

# Actually make the title
text_items = [
    ('Stock ', 'black'),
    ('A', 'red'),
    (' Out-performed ', 'black'),
    ('B', 'blue'),
]

# Start by placing invisible text to find center position
full_text = ''.join([t[0] for t in text_items])
temp_text = ax.text(0.5, y, full_text,
                    transform = ax.transAxes,
                    ha = 'center', fontsize = 14,
                    alpha = 0) # invisible

fig.canvas.draw()
bbox = temp_text.get_window_extent()
start_x = ax.transAxes.inverted().transform(bbox.corners())[0][0]
temp_text.remove()

# Now place each segment
x = start_x
for text, color in text_items:
    t = ax.text(x, y, text, 
                transform = ax.transAxes,
                ha = 'left', fontsize = 14,
                color = color)
    fig.canvas.draw()
    bbox = t.get_window_extent()
    x = ax.transAxes.inverted().transform(bbox.corners())[1][0]
```

![Multicolor title](../images/chapter3/multicolor-title.png)