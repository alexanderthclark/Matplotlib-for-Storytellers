figure, tax = ternary.figure(scale = 20)
# vary scale above for higher resolution
figure.set_size_inches(9, 8)

# Add Heatmap
tax.heatmapf(winning_pct, boundary=True,
             style="triangular",
             cmap = 'Purples',
             colorbar = False)

tax.boundary(linewidth=2.0)

title = 'Net Winning % If I Choose Rock'
tax.set_title(title + " \n")

tax.right_corner_label('Rock',
        position = (.88,0.05,.09), fontsize=10)
tax.top_corner_label('Paper',
        position = (.01,1.11,.005),fontsize=10)
tax.left_corner_label('Scissors',
        position = (.07,0.05,1), fontsize=10)

tax.get_axes().axis('off')
# Workaround for a bug with labels
tax._redraw_labels()