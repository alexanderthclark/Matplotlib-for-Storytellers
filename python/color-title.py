def color_title(labels, colors, textprops ={'size':'large'}, ax = None, y = 1.013,
               precision = 10**-2):

    "Creates a centered title with multiple colors. "

    if ax == None:
        ax = plt.gca()

    plt.gcf().canvas.draw()
    transform = ax.transAxes # use axes coords

    # initial params
    xT = 0 # where the text ends in x-axis coords
    shift = 0 # where the text starts

    # text objects from the previous centering pass
    text = []

    while (np.abs(shift - (1-xT)) > precision) and (shift <= xT) :
        for t in text:
            t.remove()
        text = []

        x_pos = shift

        for label, col in zip(labels, colors):

            t = ax.text(x_pos, y, label,
                        transform = transform,
                        ha = 'left',
                        color = col,
                        **textprops)
            text.append(t)

            x_pos = t.get_window_extent()\
                   .transformed(transform.inverted()).x1

        xT = x_pos # where all text ends

        shift += precision/2 # increase for next iteration

        if x_pos > 1: # guardrail
            break