font_list = font_manager.get_font_names()
for f in font_list:
    plt.plot()
    plt.gcf().text(0.5, 0.5,
                   s = f,
                   size = 20,
                   ha = 'center',
                   fontname = f)
    plt.axis('off')
    plt.show()