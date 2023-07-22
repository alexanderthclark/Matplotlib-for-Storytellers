url = 'https://github.com/alexanderthclark/MPL-Data/raw/main/HopperOstromTrends.csv'
df = pd.read_csv(url, index_col = 'Month')
fig, ax = plt.subplots()
ax.axis('off')
n = 10 # how many rows
ax.table(cellText = df.head(n).values,
         rowLabels = df.head(n).index,
         colLabels = list(df),
         loc = 'center')