# Chapter 12: Artist Objects

Artist objects are the water we've been swimming in this whole time. Everything rendered on a plot is some kind of Artist object. Even the figure and axes objects belong to this base class. Why notice Artist objects now? Because we're leaving the well-worn path of line plots, histograms, and so forth, and some appreciation of our surroundings will help. It will also provide some comfort as you continue to learn more and encounter more technical documentation.

[Chapter 3](../chapter3/index.md) introduced the distinction between primitive Artists, such as lines, text, and patches, and the containers that hold them. Here, we only need to turn that vocabulary into a working habit. The plots in the following chapter are not new chart types. They are compositions assembled from familiar objects.

## A Plot Is a Collection of Objects

Most Axes methods are conveniences that create an Artist, add it to the Axes, and return it. For example, `ax.plot()` creates one or more `Line2D` objects, `ax.text()` creates a `Text` object, and `ax.scatter()` creates a collection. A bar chart is a collection of rectangular patches. Calling a familiar plotting method and constructing an Artist directly are therefore two routes to the same drawing system.

The direct route becomes useful when the mark you want is more specific than a standard plotting method. A circle can be constructed with `plt.Circle()` and added with `ax.add_patch()`. Lines have `add_line()`, collections have `add_collection()`, and the general `add_artist()` method handles objects without a more specific method. The dedicated methods are preferable when they exist because the Axes can register the object correctly and account for its data when appropriate. Matplotlib's [Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html) provides a fuller map of these containers.

Adding an Artist is only part of the job. Its coordinate system determines where it goes, `zorder` determines what it covers, and clipping determines whether it can extend beyond the Axes. Its visible properties—including color, transparency, line width, and size—determine how strongly it speaks. These are the same properties we have already modified through plotting methods; direct construction simply makes the object more apparent.

## A Workflow for Custom Plots

The applications ahead generally follow the same sequence:

1. Decide which visual mark should represent each observation or idea.
2. Create the Figure and Axes and establish their limits or coordinate system.
3. Construct the required lines, patches, images, and text.
4. Add each Artist to the appropriate container and arrange the layers with `zorder`.
5. Inspect the complete composition and adjust spacing, clipping, and emphasis.

This workflow is more laborious than calling `plot()`, but it is not a departure from Matplotlib's ordinary object-oriented interface. It is that interface used one object at a time. The activity calendar, heatmaps, directed graph, and speedometer that follow differ in appearance, but each is built by choosing Artists and placing them deliberately.
