names = ['a', 'b', 'c', 'd']
dissimilarities = np.ones((4, 4)) - np.eye(4)

mds = MDS(n_components = 2,
          dissimilarity = 'precomputed',
          random_state = 7,
          n_init = 8)
locations = mds.fit_transform(dissimilarities)

differences = locations[:, np.newaxis] - locations
fitted_distances = np.sqrt((differences**2).sum(axis = 2))

fig, ax = plt.subplots(figsize = (7, 5.5))

center = locations.mean(axis = 0)
diagonal_number = 0

for first, second in combinations(range(4), 2):
    x = locations[[first, second], 0]
    y = locations[[first, second], 1]
    ax.plot(x, y,
            color = '#9fb3c8',
            linewidth = 1.5,
            zorder = 1)

    is_diagonal = fitted_distances[first, second] > 1
    if is_diagonal:
        fraction = (.35, .65)[diagonal_number]
        diagonal_number += 1
        position = ((1 - fraction) * locations[first]
                    + fraction * locations[second])
    else:
        position = locations[[first, second]].mean(axis = 0)
        outward = position - center
        position += .07 * outward / np.linalg.norm(outward)

    ax.text(position[0], position[1],
            f'{fitted_distances[first, second]:.2f}',
            ha = 'center', va = 'center',
            color = '#52606d', size = 11,
            bbox = {'facecolor': 'white',
                    'edgecolor': 'none',
                    'pad': 1},
            zorder = 2)

ax.scatter(locations[:, 0], locations[:, 1],
           s = 850,
           color = 'C0',
           edgecolor = 'white',
           linewidth = 2,
           zorder = 3)

for name, (x, y) in zip(names, locations):
    ax.text(x, y, f'${name}$',
            ha = 'center', va = 'center',
            color = 'white', size = 16,
            weight = 'bold', zorder = 4)

ax.text(0, 1.02,
        'Every target dissimilarity is 1; labels show fitted distances.',
        transform = ax.transAxes,
        ha = 'left', va = 'bottom',
        color = '#52606d', size = 11)

padding = .34
ax.set_xlim(locations[:, 0].min() - padding,
            locations[:, 0].max() + padding)
ax.set_ylim(locations[:, 1].min() - padding,
            locations[:, 1].max() + padding)
ax.set_aspect('equal')
ax.axis('off')
