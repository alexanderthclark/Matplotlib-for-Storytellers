for i in range(3):
    fig, ax = plt.figure(), plt.axes()
    label = '{:0>4}'.format(i)
    ax.set_title("Plot " + label,
                 fontname = 'Courier New',
                 weight = 'bold',
                 fontsize = 30)
    fig.tight_layout()
    fig.savefig(label + ".pdf")
    plt.show()