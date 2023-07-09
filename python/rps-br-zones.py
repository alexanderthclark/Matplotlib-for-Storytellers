# Adapted from https://github.com/marcharper/python-ternary/blob/master/README.md RGBA section
def generate_heatmap_data(scale=10):
    from ternary.helpers import simplex_iterator
    d = dict()
    for (i, j, k) in simplex_iterator(scale):
        d[(i, j, k)] = color_point(i, j, k)
    return d

# Scale should be chosen high enough for sharp resolution
scale = 200
data = generate_heatmap_data(scale)
figure, tax = ternary.figure(scale=scale)
figure.set_size_inches(9, 8)

tax.heatmap(data, style="hexagonal",
    use_rgba=True, colorbar = False)
tax.boundary()
tax.set_title("Best Response Zones")


# Label the corners
labels = 'Rock', 'Paper', 'Scissors'
tax.right_corner_label(labels[0],
    position = (.88,0.05,.09), fontsize=10)
tax.top_corner_label(labels[1],
    position = (.01,1.11,.005),fontsize=10)
tax.left_corner_label(labels[2],
    position = (.07,0.05,1), fontsize=10)

# Label best response zones
tax.annotate("Play Rock",
    (.1* scale,.1 * scale,.8 * scale), weight = 'bold')
tax.annotate("Play Paper",
    (.8*scale, .1*scale, .1*scale), ha = 'right',  weight = 'bold')
tax.annotate("Play Scissors",
    (.15*scale, .7*scale, .15*scale), ha = 'center',
    color = 'white',  weight = 'bold')

# Clear background and axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')
tax._redraw_labels()