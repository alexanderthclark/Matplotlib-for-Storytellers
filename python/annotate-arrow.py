fig, ax = plt.figure(), plt.axes()

x = np.linspace(0,1,100) # Pr(heads)
x = x[(x!=0) & (x!=1)]
entropy = -x*np.log2(x) - (1-x)*np.log2(1-x)
ax.plot(x,entropy)
ax.annotate('fair coin',
            xy = (0.5,1),
            xytext = (0.5, 0.1),
            arrowprops=dict(facecolor='white',
                            edgecolor = 'black',
                            width = 3,
                            headwidth = 10,
                            linewidth = 1),
           ha = 'center',
           va= 'top', # text alignment around xytext
           size = 12)

ax.set_title("Coin Flip Entropy")