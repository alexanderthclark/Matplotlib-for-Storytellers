fig = plt.figure()
for i in range(1,7):
    ax = fig.add_subplot(2,3,i)
    ax.text(0.5, 0.5,
            s = str(i),
            ha = 'center',
            va = 'center',
            fontsize = 30)
    ax.set_yticks([])
    ax.set_xticks([])
fig.tight_layout()