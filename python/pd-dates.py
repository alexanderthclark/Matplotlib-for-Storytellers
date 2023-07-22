url = 'https://github.com/alexanderthclark/MPL-Data/raw/main/WeatherAug1415Trends.csv'
df = pd.read_csv(url, parse_dates = ['Time'])

fig, ax = plt.figure(), plt.axes()
df.set_index("Time").plot(ax = ax)
ax.set_title("Searches for \"weather\" spike in the morning.")
ax.legend().set_visible(False)