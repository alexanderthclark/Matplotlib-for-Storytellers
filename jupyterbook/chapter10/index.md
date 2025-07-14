# Chapter 10: Applications

## Sloping Text

Suppose you'd like to label a line.

For a sloped line, you might rather the text sit parallel to the line instead of suffering the below.

```{literalinclude} ../../python/no-slope.py
:language: python
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

```{literalinclude} ../../python/slope-label.py
:language: python
```

```{figure} ../images/chapter10/slope-label.png
:width: 60%
:align: center
```

## Circular Arrangements

With our knowledge of the unit circle, we can arrange some points in a circle with no additional help beyond the math package. This might be useful if you want to avoid mixing polar and Cartesian axes.

```{literalinclude} ../../python/circle.py
:language: python
```

This code produces the following.

```{figure} ../images/chapter10/circle.png
:width: 60%
:align: center
```

The below makes similar use of trigonometry to create a circle colored according to a gradient, like in [Chapter 6](../chapter6/index.md). I make use of `solid_capstyle = 'round'` to round the endpoints of the plotted line, creating a cleaner look compared to the default.

```{literalinclude} ../../python/circle-grad.py
:language: python
```

```{figure} ../images/chapter10/circle-grad.png
:width: 80%
:align: center
```

## Network Graphs

Networks are represented mathematically as graphs—a set of vertices and edges between them. In drawing a graph, there are many drawing algorithms available. For large networks or sophisticated algorithms, you should use something off the shelf in a package like [nxviz](https://nxviz.readthedocs.io/en/latest/index.html). For a small network, you might avoid dealing with NetworkX and nxviz and do the drawing yourself. We will work through two simple layouts: arc diagrams and a circular layout for an undirected graph.

An arc diagram places all points on a straight line. The links are drawn as arcs from one point to another.

Let's consider the complete graph with four vertices, where every pair is connected.

```{literalinclude} ../../python/arc-graph.py
:language: python
```

```{figure} ../images/chapter10/arc-graph.png
:width: 70%
:align: center
```

Next we move on to a circular layout. This layout places each vertex along a circle. Spaced evenly and with just four vertices in our graph, this will in fact produce a square. We also label each edge.

```{literalinclude} ../../python/circle-graph.py
:language: python
```

```{figure} ../images/chapter10/circle-graph.png
:width: 83%
:align: center
```

## Tony Hawk's Vertical Loop

Tony Hawk became the first skateboarder to skate a vertical loop in 1998. We honor that accomplishment in two dimensions with the help of a rotation matrix. The unit circle is our vertical loop and we add two smaller circles to represent a skateboard. This is trigonometry. The small circles are placed along a ray from the origin of the unit circle to ensure they will lie tangent inside in the loop. In the first subplot, we place the skateboard at the bottom of the ramp. Though the same figure could be produced without using a rotation matrix, we use one so that the first subplot is essentially reused over and over by rotating the skateboard wheels up and around the loop.

```{literalinclude} ../../python/tony-hawk.py
:language: python
```

```{figure} ../images/chapter10/tony-hawk.png
:width: 100%
:align: center
```