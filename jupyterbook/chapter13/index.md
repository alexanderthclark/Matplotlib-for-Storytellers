# Chapter 13: Applications

## Activity Calendar

Let's start with a prose bar chart and turn it into poetry. Suppose you have a goal to practice the violin for at least 30 minutes every day and you've tracked your practice time for a whole week.

```{literalinclude} ../../python/violin-bar.py
:language: python
```

```{figure} ../images/chapter13/violin-bar.png
:width: 70%
:align: center
```

This creates a chart that is perfectly fine. But a poet might say, why futz with all the numbers and obfuscate the essential meaning? We only need to know if we hit the goal of 30 minutes or not. This kind of simplification might be more motivating. There's probably some psychology research that supports this, but we'll proceed without deferring to any such authority because those studies so often fail to replicate. Let's create a simple activity calendar of sorts.

```{literalinclude} ../../python/violin-cal.py
:language: python
```

```{figure} ../images/chapter13/violin-cal.png
:width: 90%
:align: center
```

You might have in mind ways to spice up this plot even further. Maybe there should be partial credit given to days with some violin practice, but not at least 30 minutes. Perhaps on those days, the circles can be filled with a light gray. The key here is that we're creating a plot that we might think will be more motivating.

Apps like Duolingo or Peloton gamify the user experience, and part of that is rewarding activity streaks over consecutive days. Let's try to enhance the plot so that streaks stand out. We'll accomplish this by adding a yellow edge color and increasing its weight as a streak continues. This adds some visual reward for streaks that was not evident in the previous plot.

```{literalinclude} ../../python/violin-streak.py
:language: python
```

```{figure} ../images/chapter13/violin-streak.png
:width: 90%
:align: center
```

## Heatmaps

### Google Trends

We have some data in a CSV giving Google search trend popularity by month for computer scientist [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper) and Nobel Prize-winning economist [Elinor Ostrom](https://en.wikipedia.org/wiki/Elinor_Ostrom). We'll try visualizing the trends with a few heatmaps.

First, let's import the data. We can even look at the data in a table with Matplotlib if for some sick reason you want to use Matplotlib for such a task.

```{literalinclude} ../../python/mpl-table.py
:language: python
```

```{figure} ../images/chapter13/mpl-table.png
:width: 80%
:align: center
```

A table is capital-B Boring. A `df.plot()` line chart would display these trends very well, but let's move on to making a heatmap. Here we'd have just two lines, but imagine we had several more columns in our dataset. The line chart would become a spaghetti chart. Heatmaps can be useful in avoiding this by giving each data series its own lane. Take this as a toy example of an application that helps when you have that additional clutter.

```{figure} ../images/chapter13/df-plot.png
:width: 80%
:align: center
```

Matplotlib offers the `imshow()` axes method especially for this purpose. Later, we'll create our own heatmap simply by adding our own Artist objects to the plot.

#### Using `imshow()`

First we can call `imshow()` with our transposed dataframe to get a sense of what the method does. The transpose is done so that the time (the rows of the DataFrame) will be on the $x$-axis. The `aspect` argument essentially makes the chart taller. With `aspect` set to 20, each cell is 20 times taller than it is wide. Finally, I change the colormap with `cmap = 'Oranges'` to create a monochromatic map where a darker orange is a higher search volume.

```{literalinclude} ../../python/heat-basic.py
:language: python
```

```{figure} ../images/chapter13/heat-basic.png
:width: 80%
:align: center
```

One obvious problem with this is we have no useful labels or ticks, unlike what we'd get for free with a simple `df.plot()` call. This will be remedied with the tick customizations we learned about in [Chapter 2](../chapter2/index.md). Another problem is that our data is not well behaved. The trends are washed out because of an outlier. In December 2013, Grace Hopper was featured in the Google Doodle, driving a lot of searches. All other months pale in comparison. By default, `imshow()` uses a linear scaling mapping where the lowest value is at the bottom of the colormap and the highest value is at the top of the colormap. As a result, almost all observations are toward the bottom of the colormap. One could transform the data directly or change the behavior of `imshow()`. We can transform the data with the `norm` argument or manually set the top and bottom values of the colormap with `vmin` and `vmax`.

First we use `mpl.colors.LogNorm()` to take a log transform of the data before normalizing. We also thin the $x$-axis ticks manually (instead of using a Formatter) and then relabel the ticks manually.

```{literalinclude} ../../python/heat-log.py
:language: python
```

```{figure} ../images/chapter13/heat-log.png
:width: 80%
:align: center
```

The data transformation helps the trends seen in the original line chart pop more prominently. Elinor Ostrom's search interest has remained steady but for a spike in 2009 when she was awarded the Nobel Prize in Economics, along with Oliver Williamson. The surge in search interest for Grace Hopper because of the 2013 Google Doodle remains noticeable, but the yearly spikes in interest around the Grace Hopper conference (usually held around the beginning of October) are more noticeable. Perhaps you find the transformation makes the heatmap too noisy. We can keep the quiet of the original linearly-scaled heatmap, but make spikes in interest more visible by lowering the point at which the color gradient maxes out. Below we do this by lowering `vmax`. By default, `vmax` uses the maximum data value (100 in our case). Setting `vmax = 50` means values from 50 to 100 are not differentiated by color in the heatmap. We'll also add a colorbar.

```{literalinclude} ../../python/heat-cbar.py
:language: python
```

```{figure} ../images/chapter13/heat-cbar.png
:width: 80%
:align: center
```

### NHL Regular Season Records

The previous examples used `imshow()` to turn a rectangular array into a heatmap. Now we will keep the grid, but draw each observation ourselves. Doing so gives us control over the treatment of missing data, the labels inside the cells, and the story-telling annotations.

The data are final regular-season standings for six NHL teams from 1999–00 through 2008–09, retrieved from the official [NHL standings season manifest](https://api-web.nhle.com/v1/standings-season) and the dated standings endpoints. The accompanying [`fetch-nhl-standings.py`](https://github.com/alexanderthclark/Matplotlib-for-Storytellers/blob/main/python/fetch-nhl-standings.py) script retrieves the same season-end rows used to create the committed CSV. Points percentage is calculated as points divided by twice the number of games played. This puts every team on the same zero-to-one scale. The 2004–05 season was never played because of a league-wide lockout.

The teams are selected to show contrasting paths. Detroit shows a consistently strong benchmark; Tampa Bay rises and falls; Nashville shows gradual growth; and Washington, Pittsburgh, and Chicago trace three different rebuilds.

First, here is the conventional version. We pivot the data into a team-by-season matrix and pass it to `imshow()`. A masked value and a modified “bad” color make the lockout visibly different from a low-performing season.

The data reshaping and `imshow()` call follow the same short figure-module style used throughout the book.

```{literalinclude} ../../python/hockey-heat-basic.py
:language: python
```

```{figure} ../images/chapter13/hockey-heat-basic.png
:width: 95%
:align: center
```

This chart gives a quick overview, but it asks the colorbar to do almost all of the work. Exact values require estimation, the missing season competes visually with the data, and the post-lockout rebuilds are easy to overlook.

For the final version, each data value becomes a `Circle` Artist. Here we deliberately encode points percentage twice. The radius follows the original expanding-bubble rule, `0.25 + value / 2`, so stronger seasons swell into their neighbors (an artistic choice). Every circle uses Matplotlib's first default color, `C0`, while its opacity follows the same value; direct labels provide exact values. The redundant encodings create a rhythm across each row rather than asking a legend to do all of the work. Compact horizontal season labels keep the top of the grid quiet.

Gold edges mark seasons when one of the six won the Stanley Cup: Detroit in 2001–02 and 2007–08, Tampa Bay in 2003–04, and Pittsburgh in 2008–09.

The text labels also become Artists. Each team's mark is loaded with Pillow, placed in an `OffsetImage`, and anchored beside its row with an `AnnotationBbox`. A shaded band reserves space for the cancelled season, where the letters in “LOCKOUT” are stacked downward but kept upright.

Before placement, the code crops transparent padding and fits every mark inside the same 170-by-170-pixel box. Applying one shared zoom then makes the six labels roughly uniform, but some by-hand modifications are required. Washington's wide wordmark may deserve a slightly larger team-specific zoom so the small “capitals” lettering remains legible, whereas the other five logos contain no text.

The Artist-based version is kept in one figure module, just like the other examples in this chapter.

```{literalinclude} ../../python/hockey-heat.py
:language: python
```

```{figure} ../images/chapter13/hockey-heat.png
:width: 100%
:align: center
```

The finished figure now makes a broader claim. Washington, Pittsburgh, and Chicago all sit near the bottom around the lockout and finish 2008–09 at 66, 60, and 63 percent, respectively. Tampa Bay moves in the opposite direction, peaking at 65 percent before the lockout and ending at 40 percent. Detroit's consistently large bubbles keep both patterns in perspective, while Nashville supplies a steadier middle path.

## Directed Graphs

Directed graphs arise in many settings. For plotting a large graph, like follower-following relationships in a social network, you might be best served making use of packages like NetworkX and nxviz. In other cases, you might do better working by hand. The [Graphviz](https://graphviz.readthedocs.io/en/stable/index.html) library is one possible solution. Here, we'll work directly with Matplotlib. One directed graph use case might be in illustrating the directed acyclic graph (or DAG) representing a causal theory. In the directed acyclic graph framework (mostly associated with Judea Pearl's work in causal inference), a directed edge from $X$ to $Y$ means $X$ causes $Y$, at least in part. This lends itself well to plotting. Below we'll make a plot, using `plt.Circle()` to draw nodes and creating edges with `ax.annotate()`.

Here, we create the nodes as circle objects and then draw the edges using `ax.annotate()`. Below, the circular nodes are created with the function `make_node()`. Then, the directed edge is drawn with `directed_edge()`. This doesn't allow for an edge from one node back to itself.

```{literalinclude} ../../python/dag-node.py
:language: python
```

```{literalinclude} ../../python/dag-edge.py
:language: python
```

The DAG plotted below describes the theory that the persuasiveness of an argument is caused by its logical soundness and the decibel level at which it is communicated.

```{literalinclude} ../../python/dag-argue.py
:language: python
```

```{figure} ../images/chapter13/dag-argue.png
:width: 70%
:align: center
```

## Speedometer

There's an allure to control rooms or all the gauges on the dashboard of a vehicle. If you can make your dashboards alluring, your stakeholders will visit them more often. We'll create a simple speedometer-like gauge to add some visual interest to reporting a single percentile value. We'll use what we learned about rotating points in [Chapter 9](../chapter9/index.md).

The gauge will have values running from 0% to 100%, and we'll place these along a half circle. The gauge's hand will point to a particular realized percentile value. We use a rotation matrix to find the correct angle at which to place the hand.

```{literalinclude} ../../python/speedo-functions.py
:language: python
```

```{literalinclude} ../../python/speedometer.py
:language: python
```

```{figure} ../images/chapter13/speedometer.png
:width: 75%
:align: center
```

The helper function accepts an Axes object rather than creating a new Figure. That makes the same drawing reusable in a subplot layout. Below, one loop places three gauges on three Axes. The smaller panels also reveal some crowding in the tick labels, a reminder that a design that works alone may need adjustment when repeated.

```{literalinclude} ../../python/speedometers.py
:language: python
```

```{figure} ../images/chapter13/speedometers.png
:width: 75%
:align: center
```

If the gauges must remain this small, we could label every 20 percentage points instead of every 10, reduce the text size, or increase the space between subplots. Which adjustment is best depends on what the audience needs to compare. The hand and the large value already communicate the approximate percentile, so every tick label may not be earning its space.

The reusable pattern matters more than the speedometer itself. The `speedometer()` function handles the geometry and styling of one gauge, while the calling code decides where it belongs. Functions that accept `ax` can be used alone, repeated in a grid, or inserted into a larger composition without rewriting the drawing instructions.
