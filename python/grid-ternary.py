scale = 1
figure, tax = ternary.figure(scale=scale)
tax.set_background_color('orange',
                         alpha = 0.5)

# Add ticks along the triangle edges
tax.ticks(axis = 'lbr',
          multiple = .25,
          tick_formats = '%.2f',
          offset= 0.02,
          linewidth = 0)

tax.gridlines(multiple = .25,
              color = 'gray',
              linewidth = 0.5,
              linestyle = 'solid')

points = [(0.25, 0.25, 0.5)]
tax.scatter(points,
            marker = 'o',
            color = ['black'],
            s = 100)

tax.boundary(linewidth= 2.0)
tax.get_axes().axis('equal')
tax.get_axes().axis('off')