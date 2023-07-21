from PIL import Image

fig, ax = plt.subplots(figsize = (10,10), facecolor = (.98, .98, .98))
teams = 'ABCDEF'
years = range(2002,2009)
ax.set_aspect('equal')
ax.axis('off')

y_pad = -1
for team_key, team in enumerate(teams):
    for year_key, year in enumerate(years):

        year_str = str(year)[-2:] + "-" + str(year+1)[-2:]

        record = min(1,np.random.random()**(team_key+1) + .05)
        if year != 2004:
            circ = plt.Circle((year_key, y_pad*team_key),
                      radius = .25 + (record/2),
                      color = 'C0',
                      alpha = record)
            ax.add_artist(circ)
            ax.text(year_key, y_pad*team_key,
                    s = str(round(100*record))+"%",
                    va= 'center',
                    ha = 'center')

        if year_key == 0:
            ax.text(year_key - 1, y_pad*team_key,
                    s = team,
                    ha = 'right',
                    va= 'center')
        if team_key == 0:
            ax.text(year_key, y_pad*team_key + 1,
                    s = year_str,
                    ha = 'center',
                    va= 'bottom')

ax.set_ylim(y_pad*5 - 1, 1)
ax.set_xlim(-1.5, len(years))

# lockout annotation
string = 'No Season Due To Lockout'
ax.text(2, 0,
        s = '\n'.join(string),
        va= 'top',
        ha = 'center',
        size = 15)

# Add Logo
file = '../../images/predators.png'
img = np.asarray(Image.open(file))
off_img = mpl.offsetbox.OffsetImage(img, zoom=.016)
ab = mpl.offsetbox.AnnotationBbox(off_img, (-1, 0),
                                  xycoords='data',
                                  frameon = False)
#ax.add_artist(ab)
ax.text(.5, 1.05,
        s = "Hockey Regular Season Records",
        size = 20,
        ha = 'center',
        va = 'bottom',
        transform = ax.transAxes)