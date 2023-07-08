fig = plt.figure(facecolor = 'lightgray')

for i in range(1,7):
    ax = fig.add_subplot(2,3,i)
    ax.text(0.5, 0.5,
            s = str(i),
            ha = 'center',
            va = 'center',
            fontsize = 30)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title("Title",
                 fontsize = 12,
                 fontname = 'Times New Roman')

fig.suptitle('SupTitle')
fig.tight_layout(rect = (0,0,1,1)) # no change