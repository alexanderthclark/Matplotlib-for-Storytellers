fig, ax = plt.subplots(figsize = (10,5))
s = ax.imshow(df.T,
              aspect = 20,
              cmap = 'Oranges',
              vmax = 50)

thinning = 12
ax.set_xticks(range(0,len(df),thinning))
ax.set_xticklabels(list(df.T)[::thinning],
                   rotation = 30,
                   ha = 'left')

ax.set_yticks(range(2))
ax.set_yticklabels(df.T.index)
ax.xaxis.set_tick_params(labeltop = True,
                         labelbottom = False,
                         labelsize = 10,
                         tick2On= True,
                         tick1On = True)
cbar = fig.colorbar(mappable = s,
                    ax = ax,
                    orientation = 'horizontal',
                    pad = 0.04,
                    extend = 'max')

ax.set_title("Google Search Trends",
             size = 18,
             pad = 12,
             loc = 'center')