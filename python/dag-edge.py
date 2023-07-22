def directed_edge(c1, c2, ax = None):
    """Draw an arrow from c1 to c2."""

    if ax is None:
        ax = plt.gca()

    center1 = c1.center
    center2 = c2.center

    length = np.linalg.norm(np.array(center1) - np.array(center2))

    r1 = c1.get_radius()
    r2 = c2.get_radius()

    x1, x2 = center1[0], center2[0]
    y1, y2 = center1[1], center2[1]

    # Find start and end of arrow based on circle radii
    # based on linear weights from convex combos
    tail_weight = r1 / length
    tail_x = (1-tail_weight)*x1 + tail_weight*x2
    tail_y = (1-tail_weight)*y1 + tail_weight*y2

    head_weight = r2/ length
    head_x = (1-head_weight)*x2 + head_weight*x1
    head_y = (1-head_weight)*y2 + head_weight*y1

    ax.annotate('', xy = (head_x, head_y),
                xytext = (tail_x, tail_y),
                arrowprops = dict(headwidth = 14,
                                  linewidth = .1,
                                  width = 2))