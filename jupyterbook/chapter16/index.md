# Chapter 16: Multi-dimensional Scaling

Multi-dimensional scaling (MDS) is a kind of dimensionality reduction, allowing one to translate a set of items and their predetermined pairwise distances into an arrangement of points in Cartesian space, typically in two dimensions. This is not a trivial task. Consider the meme below, which references social distancing guidance from the coronavirus pandemic. We have four individuals, forming six possible pairs, and any two individuals must maintain a six-foot distance. The graphic shows impossible right triangles that violate the Pythagorean Theorem when the distances are all exactly six feet. Indeed, there is no way to arrange four individuals in two-dimensional space so that they are all exactly six feet apart. This highlights one difficulty in multi-dimensional scaling—we must accept some error in our output.

```{figure} ../images/chapter16/calmdownpythag.jpg
:width: 80%
:align: center
```

The following diagram helps show why no alternative arrangement could be perfect. Each point $a,b,c$ is in the middle of a circle of six-foot radius. For $b$ to be six feet away from $a$, $b$ must lie on the circle centered at $a$. Similarly, for $b$ to be six feet away from $c$, $b$ must also lie on the circle centered at $c$. For three points, this arrangement is possible. But if we introduce $d$, $d$ must lie on all three of the circles centered at $a$, $b$, and $c$. But there is no point where all three circles intersect.

```{literalinclude} ../../python/mds-circles.py
:language: python
```

```{figure} ../images/chapter16/mds-circles.png
:width: 96%
:align: center
```

## From Dissimilarities to a Map

We can give that impossible request directly to MDS. The code below constructs a matrix with zeros on the diagonal because each item is identical to itself and ones everywhere else because every distinct pair has a target dissimilarity of one. The matrix is symmetric: the dissimilarity from $a$ to $b$ is the same as the dissimilarity from $b$ to $a$.

The code passes the matrix to scikit-learn's [`MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html) estimator with `dissimilarity = 'precomputed'`. The `n_components` argument requests two output dimensions. MDS begins from an initial arrangement and repeatedly moves the points to improve the fit. We set `random_state` so the example can be reproduced and use several initial arrangements with `n_init`; the estimator keeps the best result.

```{literalinclude} ../../python/mds-four-people.py
:language: python
```

```{figure} ../images/chapter16/mds-four-people.png
:width: 78%
:align: center
```

The result is approximately a square. That is a compromise, not a discovery about the four people. The four sides are about $0.85$ units long while the two diagonals are about $1.21$ units long. MDS makes some pairs too close and others too far away because a perfect two-dimensional arrangement does not exist.

## Reading an MDS Map

The distances are the meaningful part of an MDS map. The horizontal and vertical axes ordinarily have no substantive interpretation. The entire configuration can be translated, rotated, or reflected without changing any pairwise distance, so a second valid fit might appear in a different location or orientation. A fixed `random_state` makes a published example repeatable, but it does not turn either axis into a measured variable.

The input deserves as much attention as the output. State what the dissimilarities mean, how they were calculated, and whether large values represent greater difference. For a substantive application, compare the fitted distances with the original dissimilarities. A polished scatter plot cannot rescue an inappropriate distance measure or a badly distorted two-dimensional solution.
