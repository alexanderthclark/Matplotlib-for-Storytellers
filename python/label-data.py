fig, ax = plt.figure(), plt.axes()
x = np.arange(-10,6,1)
past = x[x<=0]
future = x[x>=0]

y_historical = np.random.normal(0,1,size = len(past))
y_projected = np.concatenate([y_historical[-1:],
                    np.random.normal(0,3, size = len(future)-1)])

z_historical = np.random.normal(1,1,size = len(past))
z_projected = np.concatenate([z_historical[-1:],
                    np.random.normal(3,1, size = len(future)-1)])

ax.plot(past, y_historical)
ax.plot(future, y_projected, linestyle = 'dashed', color = 'C0')

ax.plot(past, z_historical, color = 'C1')
ax.plot(future, z_projected, linestyle = 'dashed', color = 'C1')

# Label Data
ax.text(future[-1], y_projected[-1],
        s = 'Series A',
        va = 'center',
        color = 'C0',
        size = 13)
ax.text(future[-1], z_projected[-1],
        s = 'Series B',
        va = 'center',
        color = 'C1',
        size = 13)

ax.set_xlim(ax.get_xlim()[0], 9)
ax.set_title("Two Lines Zero Legends")