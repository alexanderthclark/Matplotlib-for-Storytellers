fig, ax = plt.figure(), plt.axes()
ax.set_aspect(1)
ax.set_xlim(-4,4)
ax.set_ylim(-3,3)
ax.axis('off')

persuasive = make_node((0,1.5), 1, 'Persuasiveness')
logic = make_node((2.5,-1.5), 1, 'Logic')
decibels = make_node((-2.5,-1.5), 1, 'Decibels')

directed_edge(logic, persuasive)
directed_edge(decibels, persuasive)