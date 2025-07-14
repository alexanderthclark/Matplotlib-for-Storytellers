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

```{literalinclude} ../../python/unit-circle.py
:language: python
```

We can plot a circle or an arc from $\theta_1$ to $\theta_2$, by connecting the points $(\cos(\theta_1), \sin(\theta_1)), \dots, (\cos(\theta_2), \sin(\theta_2))$, where enough intermediate angles between $\theta_1$ and $\theta_2$ are included so the piecewise-linearity is smoothed out to give the appearance of a curve. In the next subsection, we consider how to do the same, but for non-unit circles.

### Non-unit Circles

The unit circle has a radius of one and it's centered at the origin. How do we obtain coordinates for other circles? There are two steps to change the radius and shift a circle off the origin.

1. **Change the radius.** Multiply the coordinates by the desired radius $r$.
2. **Shift the circle.** Add the desired horizontal and vertical shifts to the $x$ and $y$ coordinates, respectively.

These are ordered because the radius multiplier should not be applied to the added shift term. Below, we shrink the unit circle and move it up and along the 45-degree line.

```{literalinclude} ../../python/unit-circle-shift.py
:language: python
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

```{literalinclude} ../../python/tform-matrix.py
:language: python
```

Below we plot a unit circle and then apply the transformation to create an ellipse.

```{literalinclude} ../../python/ellipse-tform.py
:language: python
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

```{literalinclude} ../../python/r-triangle.py
:language: python
```

```{figure} ../images/chapter9/r-triangle.png
:width: 70%
:align: center
```