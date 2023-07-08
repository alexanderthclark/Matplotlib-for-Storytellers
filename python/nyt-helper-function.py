def title_and_subtitle(title, subtitle = '', pad = 0.01, fig = None, ax = None):
    """Add a centered title and subtitle to a plot."""
    if ax == None:
        ax = plt.gca()
    if fig == None:
        fig = plt.gcf()
    fig.canvas.draw()

    top_of_figure = 1 # axes coords
    # update if there are xticks on the top
    tick0 = ax.get_xticklabels()[0]
    top_of_ticklabels = tick0.get_window_extent().transformed(ax.transAxes.inverted()).y1
    top_of_figure = max([top_of_ticklabels,top_of_figure])

    # Add subtitle
    if subtitle:
        subt = ax.text(0.5, top_of_figure + pad,
                       s = subtitle,
                       ha = 'center',
                       va = 'bottom',
                       size = '11',
                       fontname = 'Helvetica',
                       transform = ax.transAxes)
        # update top of figure to top of the subtitle
        top_of_figure = subt.get_window_extent().transformed(ax.transAxes.inverted()).y1

    # add title
    ax.text(0.5, top_of_figure + pad,
            s = title,
            ha = 'center',
            va = 'bottom',
            size = '18',
            fontname = 'Helvetica',
            fontweight = 'bold',
            transform = ax.transAxes,
            color = 'black')