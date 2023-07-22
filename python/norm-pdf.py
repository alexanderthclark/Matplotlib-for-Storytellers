fig, ax = plt.figure(), plt.axes()
ax.set_xlim(-3.3, 3.3)
x = np.linspace(-4, 4, 200)
ax.plot(x, stats.norm.pdf(x),
        linewidth = 2)
ax.set_title("Normal Distribution")

# Choose a point
z = 0.674
pdfz = stats.norm.pdf(z)
cdfz = stats.norm.cdf(z)

# Indicate point on plot
ax.plot([z, z],
        [0, pdfz],
        color = 'black',
        linestyle = 'dashed')
ax.plot([z], [pdfz],
        color = 'black',
        marker = '.')
ax.text(z + .1, pdfz,
        s = '$z = {:}$'.format(z) )

# Create fill to left
x_vals = np.linspace(-3,z,100)
ax.fill_between(x_vals,
                np.zeros(100),
                stats.norm.pdf(x_vals),
                color = 'gray',
                alpha = .2)

# Area/cumulative density text
ax.text(0, pdfz/2,
        s = "{:.2f}".format(cdfz),
        size = 15,
        ha = 'center')

# Change axes styling
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)