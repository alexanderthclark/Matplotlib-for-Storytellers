with plt.style.context("../../stylelib/nyt-helper.mplstyle"):

    fig = plt.figure(figsize = (7,6.5))
    ax = plt.axes(facecolor = (.94, .94, .96))

    # plot the data
    colors = ['orange', 'purple', 'darkred']
    df.T.plot(ax = ax, clip_on = False, color = colors)

    # annotate lines
    right_text_style = dict(ha = 'left',
                            fontsize = 11,
                            fontname = 'Helvetica',
                            va = 'center')
    left_text_style = dict(ha = 'right',
                      fontsize = 12,
                      fontweight = 'bold',
                      fontname = 'Helvetica')

    # alone
    ax.text(2019 - .02, 6, 'Alone',
        color = colors[0],
        va = 'center',
        **left_text_style)
    ax.text(2020.03, 7, '+57 min.',
        **right_text_style)

    # Within household
    ax.text(2019 - .02, 4.2, 'With people\noutside\nhousehold',
            color = colors[1],
            va = 'bottom',
            **left_text_style)
    ax.text(2020.03, 2.7, '-1 hour and 33 min.',
            **right_text_style)

    # Outside household
    ax.text(2019 - .02, 4, 'With\nhousehold\nmembers only',
            color = colors[2],
            va = 'top',
            **left_text_style)
    ax.text(2020.03, 4.4, '+31 min.',
            **right_text_style)


    # Title and sub
    t = 'A lonely year'
    s = 'Average time spent per day during waking hours, May through\nDecember in 2020 vs. 2019'
    title_and_subtitle(t,s, fig = fig, ax = ax, pad = .03)

    # Clean ticks etc
    yticks = range(0,9,2)
    ax.set_yticks(yticks)
    ax.set_ylim(0,8)
    # add custom labels for y ticks
    for tick in yticks:
        label = "{} hours".format(tick)
        if tick == 0:
            label = 'No Time' # custom label
        ax.text(2019.5, tick + .01, label,
              va = 'bottom',
              ha = 'center')

    # move x-tick labels to horizontally align
    ax.legend().set_visible(False)
    x_vals = [2019,2020]
    ax.set_xticks(x_vals)
    ax.set_xlim(x_vals)
    xticks = ax.get_xticklabels()
    xticks[0].set_ha('left')
    xticks[-1].set_ha('right')