fig, ax = plt.subplots(figsize = (10,3))
ax.imshow(df.T,
          aspect = 20,
          cmap = 'Oranges',
          norm = mpl.colors.LogNorm())
ax.set_title("Google Search Trends")

thinning = 12 # label every 12th month
ax.set_xticks(range(0,len(df),thinning))
ax.set_xticklabels(list(df.T)[::thinning],
                   rotation = 30)
ax.set_yticks(range(2))
ax.set_yticklabels(df.T.index)