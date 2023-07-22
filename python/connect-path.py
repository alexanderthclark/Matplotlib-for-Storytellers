fig = plt.figure(figsize = (7,6))

# Generate random data
n = 100
x = np.random.normal(size = n)
y = np.random.normal(size = n)
# z is determined by x except for one outlier
z = np.concatenate([np.array([4]), 1- x[1:]**2])

# Add x,y scatter plot
ax12 = fig.add_subplot(2,2,(1,2))
ax12.scatter(x,y, alpha = 0.5)

# Add x,z scatter plot
ax3 = fig.add_subplot(2,2,3)
ax3.scatter(x,z, alpha = 0.5)

# Add y,z scatter plot
ax4 = fig.add_subplot(2,2,4)
ax4.scatter(y,z, alpha = 0.5)

# Draw lines connecting the outlier as it appears in each scatter plot
con = ConnectionPatch(
        xyA = (x[0], y[0]),
        coordsA = ax12.transData,
        xyB = (x[0], z[0]),
        coordsB = ax3.transData,
        arrowstyle = "<->",
        shrinkA = 2,
        shrinkB = 0)
fig.add_artist(con)

con = ConnectionPatch(
        xyA = (x[0],y[0]),
        coordsA = ax12.transData,
        xyB = (y[0], z[0] ),
        coordsB = ax4.transData,
        arrowstyle = "<->",
        shrinkA = 2,
        shrinkB = 0)
fig.add_artist(con)

ax12.set_xlabel("$x$")
ax12.set_ylabel("$y$")
ax3.set_ylabel("$z$")
ax3.set_xlabel("$x$")
ax4.set_ylabel("$z$")
ax4.set_xlabel("$y$")
plt.tight_layout()