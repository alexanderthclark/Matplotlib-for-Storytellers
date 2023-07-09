scale = 1
figure, tax = ternary.figure(scale = scale)
# vary scale above for higher resolution
figure.set_size_inches(9, 8)

# Rock > Paper
# s - p > r - s
# 2s > r + p
p1 = (2/3, 0, 1/3) # rps ordering
p1 = scale * np.array(p1)
p2 = (0, 2/3, 1/3)
p2 = scale * np.array(p2)

tax.line(p1, p2,
         linewidth=3.,
         marker='s',
         color='green',
         linestyle=":")
tax.annotate('  R < P', (.75*p1 + .25*p2),
             color = 'green',
             ha = 'left',
             va = 'top')
tax.annotate('R > P  ', (.75*p1 + .25*p2),
             color = 'green',
             ha = 'right',
             va= 'bottom')

# Rock > Scissors
# s - p > p - r
# s + r > 2p
p1 = (2/3, 1/3, 0) # rps ordering
p1 = scale * np.array(p1)
p2 = (0, 1/3, 2/3)
p2 = scale * np.array(p2)

tax.line(p1, p2,
         linewidth = 3.,
         marker = 's',
         color = 'blue',
         linestyle = ":",
         label = 'RockScissors')
tax.annotate('R > S', (.75*p1 + .25*p2),
             color = 'blue',
             ha = 'left',
             va = 'top')
tax.annotate('R < S', (.75*p1 + .25*p2),
             color = 'blue',
             ha = 'right',
             va= 'bottom')

# Paper > Scissors
# r - s > p - r
# 2r > p + s
p1 = (1/3, 2/3, 0) # rps ordering
p1 = scale * np.array(p1)
p2 = (1/3, 0, 2/3)
p2 = scale * np.array(p2)

tax.line(p1, p2,
         linewidth = 3,
         marker = 's',
         color = 'red',
         linestyle = ":")


tax.annotate('S > P ', (.75*p1 + .25*p2),
             color = 'red',
             ha = 'left',
             va = 'top')
tax.annotate(' S < P', (.75*p1 + .25*p2),
             color = 'red',
             ha = 'right',
             va= 'bottom')

tax.boundary(linewidth=2.0)

# Make pretty as desired
title = 'Pairwise Comparisons'
tax.set_title(title + " \n")

tax.right_corner_label('Rock',
                       position = (.88,0.05,.09),
                       fontsize=10)
tax.top_corner_label('Paper',
                     position = (.01,1.11,.005),
                     fontsize=10)
tax.left_corner_label('Scissors',
                      position = (.07,0.05,1),
                      fontsize=10)

tax.get_axes().axis('off')
tax._redraw_labels()