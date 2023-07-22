# Create the Plot
scale = 1 # length of the sides
figure, tax = ternary.figure(scale=scale)

# Draw Boundary
tax.boundary(linewidth= 2.0,
             axes_colors = {'l':'red', 'r': 'blue', 'b': 'green'})