standings = pd.read_csv('../../Data/nhl_regular_season.csv')

seasons = ['1999-00', '2000-01', '2001-02', '2002-03', '2003-04',
           '2004-05', '2005-06', '2006-07', '2007-08', '2008-09']
teams = ['Detroit Red Wings', 'Tampa Bay Lightning',
         'Nashville Predators', 'Washington Capitals',
         'Pittsburgh Penguins', 'Chicago Blackhawks']

records = (standings.pivot(index = 'team',
                           columns = 'season',
                           values = 'point_pct')
                    .reindex(index = teams,
                             columns = seasons))

cmap = mpl.colormaps['Blues'].copy()
cmap.set_bad('#e9ecef')

fig, ax = plt.subplots(figsize = (10, 4.6))
image = ax.imshow(np.ma.masked_invalid(records),
                  aspect = 'auto',
                  cmap = cmap,
                  vmin = .30,
                  vmax = .76)
