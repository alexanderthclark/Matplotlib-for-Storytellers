def make_node(center, radius = 'auto', label = '', ax = None):
    """Plot labeled circle object to represent a node.
    Rrun after any changes to axes limits, aspect changes, etc if using radius = 'auto'."""
    if ax is None:
        ax = plt.gca()
    t = ax.text(center[0], center[1], label, ha = 'center', va = 'center')
    if radius == 'auto':
        plt.gcf().canvas.draw()
        box = t.get_window_extent().transformed(ax.transData.inverted())
        width = box.x1 - box.x0
        radius = (width/2)*1.2
    c = plt.Circle(center, radius,
                   facecolor = (.9,.99,.9),
                   edgecolor = 'black')
    ax.add_artist(c)
    return c