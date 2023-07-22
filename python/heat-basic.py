fig, ax = plt.figure(figsize = (10,3)), plt.axes()
ax.imshow(df.T,
    aspect = 20,
    cmap = 'Oranges')
ax.set_title("Google Search Trends")