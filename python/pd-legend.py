# Construct DataFrame
n = 100
sqrts = np.concatenate([np.zeros(1),np.ones(n).cumsum()**0.5] )
ser1 = pd.Series(data = -sqrts, name = 'Lower Bound')
ser2 = pd.Series(data = sqrts, name = 'Upper Bound')
df = pd.DataFrame([ser1,ser2]).T

# Add random walk
df['Walk'] = np.concatenate([np.zeros(1),np.random.normal(size = n).cumsum()])

# Plot
fig, ax = plt.subplots()
df['Lower Bound'].plot(color = 'black', label = 'Boundary')
df['Upper Bound'].plot(color = 'black', label = '_nolegend_')
df['Walk'].plot()

ax.legend()