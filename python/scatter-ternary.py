scale = 1
figure, tax = ternary.figure(scale=scale)

# Draw Boundary
tax.boundary(linewidth= 2.0)

# Scatter Points
points = [(1,0,0), (0,1,0), (0,0,1), (1/3, 1/3, 1/3)]
tax.scatter(points,
            marker = 'o',
            color = ['red', 'yellow', 'green', 'blue'],
            s = 100)