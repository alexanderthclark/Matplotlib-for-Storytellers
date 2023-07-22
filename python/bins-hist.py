#data = np.random.normal(size = 30)
fig, ax = plt.subplots(1,4, figsize = (9,3))

for key, b in enumerate([4, 8, 10, 15]):
    ax[key].hist(data, edgecolor = 'black', bins = b)
    ax[key].set_yticks([])
    for s in 'left', 'top', 'right':
        ax[key].spines[s].set_visible(False)