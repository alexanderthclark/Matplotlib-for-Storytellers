fig, ax = plt.figure(), plt.axes()
ax2 = ax.twinx()
x = np.linspace(-3,3,200)
pdf_y = stats.norm.pdf(x)
cdf_y = stats.norm.cdf(x)

# Plot Curves
ax2.plot(x, cdf_y,
         color = 'darkgray',
         linestyle = 'dashed',
         linewidth =2)
ax.plot(x, pdf_y,
        linewidth = 3)

ax.set_title("Normal Distribution")

# Change Ticks
# Use LaTeX \mathbf to make ticks bold
bolded_ticks = [r'$\mathbf{'+"{:.2f}".format(x)+r"}$" for x in ax.get_yticks()]
ax.set_yticklabels(bolded_ticks)
ax.tick_params(axis ='y',
               colors = 'C0',
               labelsize = 11)
ax2.tick_params(axis ='y',
                colors = (.25,.25,.25)) # darker gray