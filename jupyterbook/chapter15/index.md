# Chapter 15: Intro Statistics

Since the fall of 2022, I've been teaching intro stats and I've been very particular about my graphs. According to my college ethics professor, the experience of beauty is a human good and statistics is not.[^gomez-lobo] That doesn't provide a good prioritization for developing an intro stats syllabus, but as an instructor, I've at least tried to make my slides and notes a kind of beautiful. Watching a student pinch to zoom on her iPad without a particular graph pixelating or otherwise revealing any defect was a beautiful moment.

[^gomez-lobo]: Shoutout to the late Alfonso Gómez-Lobo.

I make all of the figures for my class materials in Python. Working in Python offers the advantage of, well, working in Python. We are able to mix statistical functions from Python in our code, so we gain more precision than is available from anything hand-drawn (whether on pencil and paper or by dragging a cursor). We can also create high-quality images in a vector format like PDF or SVG, meaning we can zoom without the image quality degrading.

It's true that you might achieve the same goals using languages like R or Ti*k*Z. Indeed, for probability trees, I still use Ti*k*Z. Otherwise, I offer no apology for choosing Python. In this chapter, I include a few common applications that arise in statistics.

```{figure} ../images/chapter15/errors-stacked.png
:width: 95%
:align: center
```

## Probability Diagrams

Below, we produce Venn diagrams to consider set operations for two sets, $A$ and $B$. These sets are outlined as circles, either by plotting the outline or by using the Circle Artist object. The result of the set operation will be filled with gray. This can be tricky because I insist that the circle outlines (the Artist object's edge) are always visible, meaning we have to be mindful of how one circle overlapping another could obscure the other's outline.

First, we plot $A$ and $B$, filling only $A$. $A$ and $B$ are Circle objects and I plot $B$ second so that it is in front of $A$. This means that the outline of $B$ is not lost underneath $A$. We want the opposite from the fill color of $B$—we do not want it to overlap $A$. To prevent this, $B$ is filled with `facecolor = (1, 1, 1, 0)`, which is the RGBA color for white (RGB 1,1,1) and an alpha or opacity of 0%, leaving it transparent. We could also have used an alpha parameter, but this would apply to both the `facecolor` and `edgecolor` arguments, which we want to treat separately.

```{literalinclude} ../../python/event-A.py
:language: python
```

```{figure} ../images/chapter15/event-A.png
:width: 70%
:align: center
```

Next, we consider the union of $A$ and $B$. This presents a similar challenge in not having the fill of one circle cover the outline of the other circle. First, we create two Circle objects, filled gray and with a black outline. If we stopped there, we would have a visible overlap. To recover the outline of $A$, we add a third circle with a black outline but a transparent fill.

```{literalinclude} ../../python/union.py
:language: python
```

```{figure} ../images/chapter15/union.png
:width: 70%
:align: center
```

To plot the intersection of $A$ and $B$, we abandon Circle objects for the `plot()` and `fill_between()` Axes methods. Filling the intersection is done in two pieces.

```{literalinclude} ../../python/intersection.py
:language: python
```

```{figure} ../images/chapter15/intersection.png
:width: 70%
:align: center
```

Finally, we plot $A \cap B^C$ or $A \setminus B$. For this, we again need a third transparent circle. We allow a white-filled $B$ to cover $A \cap B$, essentially removing the fill from that region. Then, we use the Circle `left_circle_helper` to restore the outline of $A$.

```{literalinclude} ../../python/A-minus-B.py
:language: python
```

```{figure} ../images/chapter15/A-minus-B.png
:width: 70%
:align: center
```

## Distributions

We use the `hist()` Axes method to create a histogram. Beautifying the plot is only a matter of modifying the background elements, like the spines and labels, and then choosing the right number of bins and colors for the histogram. A histogram includes Patch objects, meaning we can specify both an `edgecolor` and `facecolor`. Below, we create a histogram using the defaults.

```{literalinclude} ../../python/default-hist.py
:language: python
```

```{figure} ../images/chapter15/default-hist.png
:width: 70%
:align: center
```

When you are only interested in the shape of the data, you will find the $y$-axis information unimportant. Accordingly, we'll remove the $y$-axis to (repeat after me) reduce clutter.

```{literalinclude} ../../python/clean-hist.py
:language: python
```

```{figure} ../images/chapter15/clean-hist.png
:width: 70%
:align: center
```

The last modification considered is the simple use of the `bins` parameter to adjust the number of bins in the histogram.

```{literalinclude} ../../python/bins-hist.py
:language: python
```

```{figure} ../images/chapter15/bins-hist.png
:width: 70%
:align: center
```

Next, density plots can be produced with the SciPy package and its statistics module, which has been imported already with `import scipy.stats as stats`. Below is a simple plot for a normal distribution.

```{literalinclude} ../../python/normal-pdf.py
:language: python
```

```{figure} ../images/chapter15/normal-pdf.png
:width: 70%
:align: center
```

To motivate sampling distributions, it might be useful to label the $x$-axis not with numeric quantities but with $\mu$ and $\bar{x}$ for the true mean and the observed sample mean. This is done with the `set_xticklabels()` Axes method, aligning the strings with ticks that are also manually set with `set_xticks()`.

```{literalinclude} ../../python/sampling-dist.py
:language: python
```

```{figure} ../images/chapter15/sampling-dist.png
:width: 70%
:align: center
```

Next, we conduct and illustrate a one-tailed $z$-test for a proportion,

$$
\begin{aligned}
H_0: p &= \frac{1}{2} \\
H_a: p &> \frac{1}{2}.
\end{aligned}
$$

We set $\alpha = 0.05$ and suppose we observed 18 successes from 30 trials. The test statistic and $p$-value are calculated with the help of the statsmodels library and the [`proportions_ztest()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportions_ztest.html) function.

```{literalinclude} ../../python/one-tail-norm.py
:language: python
```

```{figure} ../images/chapter15/one-tail-norm.png
:width: 70%
:align: center
```

In the above, the two plots share the same $x$-axis scaling and I'd prefer the vertical line for the test statistic extend from one graph to the other, emphasizing that the two distributions are identical. We again face this challenge when using stacked plots to illustrate Type I and Type II error, and it is in that context that we solve the problem. This can be solved by using a Transform object. The $x$-axis coordinates are naturally expressed in data coordinates. Because we want the vertical line extending from one subplot Axes to the other, we should work in Figure coordinates. This requires just two special lines in the code below. The blended transformation is created with the `blended_transform_factory()` function and then we use the `transform` parameter in the Axes plotting method.

```{literalinclude} ../../python/error-stack.py
:language: python
```

```{figure} ../images/chapter15/error-stack.png
:width: 70%
:align: center
```
