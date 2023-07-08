ig = plt.figure(figsize = (7,6.5))
ax = plt.axes(facecolor = (.94, .94, .96))

## Add data and annotations
plot_style = dict(marker = 'o',
        clip_on = False, # don't clip markers at axes boundary
        linewidth = 3,
        markersize = 8)
right_text_style = dict(ha = 'left', fontsize = 11,
                      fontname = 'Helvetica',
                      color = (.3,.3,.3),
                      va = 'center')
left_text_style = dict(ha = 'right',
                      fontsize = 12,
                      fontweight = 'bold',
                      fontname = 'Helvetica')
x_vals = [2019,2020]
# alone
col = 'orange'
ax.plot(x_vals, [6,7],
        color = col,
        **plot_style)
ax.text(2019 - .02, 6, 'Alone',
        color = col,
        va = 'center',
        **left_text_style)
ax.text(2020.03, 7, '+57 min.',
        **right_text_style)

# within household
col = 'purple'
ax.plot(x_vals, [4.3,2.7],
        color = col,
        **plot_style)
ax.text(2019 - .02, 4.2, 'With people\noutside\nhousehold',
        color = col,
        va = 'bottom',
        **left_text_style)
ax.text(2020.03, 2.7, '-1 hour and 33 min.',
        **right_text_style)

# outside household
col = 'darkred'
ax.plot(x_vals, [3.9,4.4], color = col,
        **plot_style)
ax.text(2019 - .02, 4, 'With\nhousehold\nmembers only', color = col,
        va = 'top',
       **left_text_style)

ax.text(2020.03, 4.4, '+31 min.',
        **right_text_style)


# Label Gridlines
text_style = dict(color = (.3,.3,.3),
                 va = 'bottom',
                 ha = 'center',
                 fontname = 'Helvetica',
                 fontsize = 11)

ax.text(2019.5, 0.01, "No Time", **text_style)
for y in [2,4,6,8]:
    ax.text(2019.5, y+.04, "{} hours".format(y),
            **text_style)

# Label 2020/2021 for x-axis
year_text_style = dict(color = (.3,.3,.3),
                 va = 'bottom',
                 fontname = 'Helvetica',
                 fontsize = 12)
ax.text(2019, 8.05, '2019',
                ha = 'left', **year_text_style)
ax.text(2020, 8.05, '2020',
                ha = 'right', **year_text_style)

# set main title
ax.set_title("A lonely year", pad = 55, fontweight = 'bold',
             fontname = 'Helvetica',
            fontsize = 18)

# set subtitle
s = 'Average time spent per day during waking hours, May through\nDecember in 2020 vs. 2019'
ax.text(2019.5, 8.5, s, **text_style)

# x axis
ax.set_xticks([])
ax.set_xlim(2019,2020)

# y axis
ax.yaxis.grid(True, color = 'white')
ax.set_yticks([0,2,4,6,8])
ax.set_yticklabels([])
ax.set_ylim([-.02,8])
ax.yaxis.set_tick_params(length = 0, grid_linewidth = 2)

# spines
for i in ['top','left','right']:
    ax.spines[i].set_visible(False)
ax.spines['bottom'].set_color('darkgray')
ax.spines['bottom'].set_linewidth(2)