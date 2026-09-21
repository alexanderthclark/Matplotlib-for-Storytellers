# Chapter 14: Ternary Plots

This chapter introduces the [python-ternary package](https://github.com/marcharper/python-ternary). You'll need to install this with pip or conda to follow along. You can use this to make various plots in the two-dimensional simplex. That is, you can make triangle plots where a point in the triangle represents a particular multinomial distribution over three possible outcomes. The triangle is a two-dimensional projection of the space

$$
\left\{ \left(p_1,p_2,p_3 \right)\in \mathbb{R}^3: p_1+p_2+p_3 = 1 \text{ and } p_i \in [0,1] \text{ for }i=1,2,3 \right\}.
$$

```{figure} ../images/chapter14/tikz-simplex-blank.png
:width: 60%
:align: center
```

I encountered these diagrams in a few economics courses. Professor [Bill Sandholm](https://www.ssc.wisc.edu/~whs/) made particularly memorable use of these diagrams in his courses and research in evolutionary game theory. These plots aren't the most natural selection for inclusion in this text. It's a personal indulgence and a favor to other game theorists.

After running `import ternary`, the construction of a plot isn't much different than what we covered in [Chapter 1](../chapter1/index.md). Start with figure and *ternary* axes objects. However, `ternary.figure()` will create both objects. There is no analogue to `plt.axes()` as this more closely imitates `plt.subplots(1,1)` than `plt.figure()`. It's not a perfect replica though. For example, there is no `figsize` parameter, but this can be adjusted with the figure method `set_size_inches()`.

```{literalinclude} ../../python/basic-ternary.py
:language: python
```

```{figure} ../images/chapter14/basic-ternary.png
:width: 50%
:align: center
```

```{literalinclude} ../../python/color-ternary.py
:language: python
```

```{figure} ../images/chapter14/color-ternary.png
:width: 60%
:align: center
```

Next, let's add some points with the `scatter` method, which works as you might expect.

```{literalinclude} ../../python/scatter-ternary.py
:language: python
```

```{figure} ../images/chapter14/scatter-ternary.png
:width: 60%
:align: center
```

The $x$- and $y$-axis ticks above correspond to the bottom and right axes, but this can be confusing since the $x,y$ point of $(0,0)$ is the point $(0,0,1)$ in the ternary plot. Accordingly, you might prettify the plot by removing those ticks and these axes entirely. This can be done with `tax.get_axes().axis('off')`. This works like `ax.axis()` so we can also pass `'equal'` to equalize the axes. Adding gridlines with the `gridlines` method can also help the eye. This is demonstrated below. The horizontal gridlines correspond to the value along the right axis. The negatively sloped gridlines correspond to the left axis. The positively sloped gridlines correspond to the bottom axis. These gridlines are perpendicular to the direction of ascent along each axis and, just as for a typical plot, they show where the particular axis value is constant.

```{literalinclude} ../../python/grid-ternary.py
:language: python
```

```{figure} ../images/chapter14/grid-ternary.png
:width: 60%
:align: center
```

## Application: Rock, Paper, Scissors

Throughout this chapter, we'll analyze the game rock paper scissors. If you need a reminder, there are two players who simultaneously choose an action of either rock, paper, or scissors. Rock beats scissors beats paper beats rock. Choosing the same action results in a tie. Your job is to choose an action based on your expectation of what your opponent will choose.

First, we'll construct a heatmap to show the net winning percentage from choosing a particular action depending on the opponent's probability distribution over the three actions, so that a point in the simplex is that opponent's strategy and the color represents how often you win. The following is a function we'll use in making a heatmap, calculating the net winning percentage of an action against a particular distribution.

```{literalinclude} ../../python/rps-helper.py
:language: python
```

Now, we can create a heatmap using the function `winning_pct` and the `heatmapf` method.

```{literalinclude} ../../python/heat-rps.py
:language: python
```

```{figure} ../images/chapter14/heat-rps.png
:width: 83%
:align: center
```

The natural extension of the above might be to repeat the above, which supposes you choose rock, for the actions paper and scissors. This can be done straightforwardly, by changing the default action in the `winning_pct` function. For the game theorist, the more interesting question is, given my opponent's distribution over actions, what is my best response? The code below plots the regions of pairwise indifference between two actions. Then, we divide up the simplex into three best response regions.

```{literalinclude} ../../python/rps-br-lines.py
:language: python
```

```{figure} ../images/chapter14/rps-br-lines.png
:width: 90%
:align: center
```

We can color best-response zones by using the `heatmap` method, though it will take some work. First, we have some pure Python coding to do. Recall that `heatmap` requires a correspondence of points and the colors you want. We won't use a colormap, but we'll pass the colors in explicitly as RGBA values. This is a bit of a hack since the resulting plot and its colors won't have the ordered interpretation typical of heatmaps.

```{literalinclude} ../../python/rps-br-helper.py
:language: python
```

```{literalinclude} ../../python/rps-br-zones.py
:language: python
```

```{figure} ../images/chapter14/rps-br-zones.png
:width: 90%
:align: center
```

Anyone inspecting what `data` looks like above will note that the points in the triangle aren't proper probability vectors as they add up to our `scale` value of 200 instead of one. That's immaterial for this application. A higher scale is chosen to create a sharper, exact border between the best-response regions.
