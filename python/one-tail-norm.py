# One-sided test
from statsmodels.stats.proportion import proportions_ztest
z_oneside, pval_oneside = proportions_ztest(
                                count = 18,
                                nobs = 30,
                                value = .5,
                                prop_var = 0.5,
                                alternative = 'larger')

# one tail norm
x = np.linspace(-4,4, 100_000)
norm_pdf = stats.norm.pdf(x)

# Make empty figure
fig, axx = plt.subplots(2, 1,
                        figsize = (10,5),
                        sharey = True)

for ax in axx:
      # add normal curve
    ax.plot(x, norm_pdf, lw = 3)

    # add z stat
    ax.axvline(z_oneside, linestyle = 'dashed')
    ax.text(z_oneside, 0.3, ' $z$', ha = 'left', size = 12, color = 'C0')

    # Clean plot
    for s in 'left', 'right', 'top':
        ax.spines[s].set_visible(False)
    ax.yaxis.set_ticks([])
    ax.set_ylim(0,.42)
    ax.set_xlim(-3.1, 3.1)

# draw rejection region
ax = axx[0]
alpha = .05
critical_value = stats.norm.ppf(1 - alpha) # for one-sided
rejection_x = x[x>critical_value]
ax.fill_between(rejection_x, norm_pdf[-len(rejection_x):],
                color = 'red',
                alpha = 0.2)
ax.text(3.1, .14,
        s = 'Rejection Region',
        fontsize = 19,
        color = (.6, .2, .2),
        ha = 'right')

# shade p-value
ax = axx[1]
more_extreme_x = x[x>z_oneside]
ax.fill_between(more_extreme_x, norm_pdf[-len(more_extreme_x):],
                color = (.2, .2, .2),
                alpha = 0.2)
ax.text(3.1, .13,
        s = 'P-Value',
        fontsize = 19,
        color = (.3, .3, .3),
        ha = 'right')