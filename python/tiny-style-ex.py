plt.style.use('../../stylelib/tiny-style.mplstyle')

fig, ax = plt.figure(), plt.axes()
x = np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title('Hello')

# Inspect the updated rcParams
#print(mpl.rcParams)