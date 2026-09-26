# Chapter 12: Artist Objects

Artist objects are the water we've been swimming in this whole time. Everything rendered on a plot is some kind of Artist object. Even the figure and axes objects belong to this base class. Why notice Artist objects now? Because we're leaving the well-worn path of line plots, histograms, and so forth, and some appreciation of our surroundings will help. It will also provide some comfort as you continue to learn more and encounter more technical documentation.

[Chapter 3](../chapter3/index.md) introduced the distinction between primitive Artists, such as lines, text, and patches, and the containers that hold them. To create more flexible illustrations, like a poet might, we need a little more understanding of Artist objects. We do not need a deeper theory. It is enough to recognize these objects when we create them and know how to add them to an axes object. The plots in the following chapter might look unusual, but they are mostly arrangements of lines, text, patches, and images.

## Adding Artist Objects

Many axes methods quietly create Artist objects for us. For example, `ax.plot()` creates one or more `Line2D` objects, `ax.text()` creates a `Text` object, and `ax.scatter()` creates a collection. A call to `ax.bar()` creates a collection of rectangular patches. You usually do not need to know any of this when the usual plotting method gives you what you want.

But sometimes it is easier to create the Artist directly. A Patch is an Artist used to draw a two-dimensional shape with a face and an edge. `Circle`, `Rectangle`, and `Polygon` are all patches. You can create a circle with `plt.Circle()` and add it to an axes object with `ax.add_patch()`. There are similar methods such as `add_line()` and `add_collection()`, along with the more general `add_artist()`. I would use the more specific method when one exists. Besides making the type of object clearer, some of these methods also allow the axes object to account for the Artist when determining the data limits. Matplotlib's [Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html) goes into more detail.

### A Small Thermometer

A thermometer is not a standard matplotlib plot type, which makes it a useful small example. Below, a temperature determines the height of a red rectangle. A second rectangle creates the stem and a circle creates the bulb. We also add a short line and a text label at the top of the red fill. This is closer to an illustration than a conventional plot, but it is still made with the same objects we have used throughout the book.

```{literalinclude} ../../python/thermometer.py
:language: python
```

```{figure} ../images/chapter12/thermometer.png
:width: 45%
:align: center
```

The two rectangles and the circle are created first, but that does not add them to the plot. The loop passes each one to `ax.add_patch()`. The short horizontal line is a `Line2D` object, so it is added with `ax.add_line()`. The call to `ax.text()` is a convenience: it creates a `Text` object and adds it to the axes in one step. We assign that object to `label` so that its color can be changed afterward with `set_color()`.

The thermometer also shows why it helps to have access to the individual objects. The value controls the height of one rectangle and the locations of the line and label. The `zorder` values keep the fill above the stem and the bulb above both. We could now change or remove any part without redrawing the others.

Creating and adding an Artist does not finish the job. We still need to choose its coordinate system, its `zorder`, and whether it should be clipped by the axes. We might also set its color, transparency, line width, or size. These are not new considerations. We have already made the same choices through plotting methods. Creating the Artist directly just leaves more of those decisions in our hands.

Other Artist classes appear later without requiring much additional theory. `ax.scatter()` returns a `PathCollection`, while `imshow()` returns an `AxesImage`. The hockey example uses `OffsetImage` and `AnnotationBbox` to place team logos. There is no need to memorize the class hierarchy. The important point is that these parts of a plot are objects that can be stored in variables, modified, layered, or removed.

## Building a Plot One Artist at a Time

When I build a custom plot, I usually begin by creating the figure and axes objects and setting the axes limits or coordinate system. Then I create the required lines, patches, images, and text and add them to the axes object. The `zorder` can be used to arrange the layers. Only after seeing everything together will you know whether the spacing, clipping, and sizing work. This is one reason these plots often require some tinkering.

This is more laborious than calling `plot()`, but nothing fundamentally different is happening. We are still using Matplotlib's object-oriented interface, only one object at a time. The reward is flexibility: we are no longer limited to the plot produced by a single method. The activity calendar, heatmaps, directed graph, and speedometer that follow look very different, but each is built by choosing a few Artist objects and placing them on an axes object.
