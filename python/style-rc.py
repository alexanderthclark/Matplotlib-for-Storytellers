# Use rcParams
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False

x = np.linspace(0,1,2)
plt.plot(x,x)
plt.savefig("style1.pdf")
plt.show()

plt.plot(x, 1-x)
plt.savefig("style2.pdf")
plt.show()