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
a_line, = ax.plot(future, y_projected, linestyle = 'dashed', color = 'C0')
ax.plot(past, z_historical, color = 'C1')
b_line, = ax.plot(future, z_projected, linestyle = 'dashed', color = 'C1')

# Label Data
ax.annotate('Series A',
            xy = (1, y_projected[-1]),
            xycoords = (a_line, 'data'),
            color = 'C0',
            size = 12)

ax.annotate('Series B',
            xy = (1, z_projected[-1]),
            xycoords = (b_line, 'data'),
            color = 'C1',
            size = 12)

ax.set_xlim(ax.get_xlim()[0], 9)
ax.set_title("Two Lines Zero Legends")