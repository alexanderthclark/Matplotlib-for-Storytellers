x = np.linspace(-3,5, 100_000)

fig = plt.figure(figsize = (10,5))
ax0 = fig.add_subplot(211, zorder = 99)
ax1 = fig.add_subplot(212)

for center, ax in zip([0, 2], [ax0, ax1]):
  # add normal curve
    norm_pdf = stats.norm.pdf(x, center, 1)
    ax.plot(x, norm_pdf, lw = 3)

    # Clean plot
    for s in 'left', 'right', 'top':
        ax.spines[s].set_visible(False)
    ax.yaxis.set_ticks([])
    ax.set_ylim(0, .42)

# draw rejection region
ax = ax0
alpha = 0.05
critical_value = stats.norm.ppf(1 - alpha) # for one-sided
rejection_x = x[x > critical_value]
ax.fill_between(rejection_x,
                stats.norm.pdf(x, 0, 1)[-len(rejection_x):],
                color = 'C1',
                alpha = 0.2)
# label
ax.text(2.2, stats.norm.pdf(2), 'Type I Error')

# Draw critical value line through both plots
trans = mpl.transforms.blended_transform_factory(ax.transData, fig.transFigure)
ax.plot([critical_value, critical_value],
        [0, 1],
        color='black',
        linestyle = 'dotted',
        lw=2,
        transform = trans,
        clip_on= False,
        zorder = 99)

# Draw type II error region
fail_to_reject_region = x[x <= critical_value]
ax1.fill_between(fail_to_reject_region,
                 stats.norm.pdf(x, 2, 1)[0:len(fail_to_reject_region)],
                 color = 'C4',
                 alpha = 0.2)
ax1.text(.1, stats.norm.pdf(.3, 2, 1), 'Type II Error', ha = 'right')