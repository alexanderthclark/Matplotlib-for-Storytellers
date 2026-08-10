from PIL import Image

fig, ax = plt.subplots(figsize = (11.5, 5.8),
                       facecolor = (.98, .98, .98))
ax.set_facecolor((.98, .98, .98))

cup_winners = {('Detroit Red Wings', '2001-02'),
               ('Tampa Bay Lightning', '2003-04'),
               ('Detroit Red Wings', '2007-08'),
               ('Pittsburgh Penguins', '2008-09')}

lockout = seasons.index('2004-05')
ax.axvspan(lockout-.5, lockout+.5,
           color = '#eceff1',
           zorder = 0)

for team_key, team in enumerate(teams):
    for season_key, season in enumerate(seasons):
        record = records.loc[team, season]
        if pd.isna(record):
            continue

        won_cup = (team, season) in cup_winners
        if won_cup:
            edgecolor, linewidth = '#D4AF37', 3
        else:
            edgecolor, linewidth = 'C0', 1

        circ = plt.Circle((season_key, team_key),
                          radius = .25 + record/2,
                          facecolor = 'C0',
                          edgecolor = edgecolor,
                          linewidth = linewidth,
                          alpha = record,
                          zorder = 2)
        ax.add_artist(circ)
        ax.text(season_key, team_key,
                s = f'{record:.0%}',
                ha = 'center',
                va = 'center',
                color = '#102a43',
                size = 11,
                weight = 'bold',
                zorder = 3)

ax.text(lockout, (len(teams)-1)/2,
        s = '\n'.join('LOCKOUT'),
        ha = 'center',
        va = 'center',
        color = '#607d8b',
        size = 9.5,
        weight = 'bold',
        linespacing = .92,
        zorder = 4)

team_marks = ['DET', 'TBL', 'NSH',
              'WSH', 'PIT', 'CHI']
for team_key, mark in enumerate(team_marks):
    file = '../../images/nhl/' + mark + '.png'
    img = Image.open(file).convert('RGBA')

    # Crop transparent padding before setting a common maximum size.
    alpha_box = img.getchannel('A').getbbox()
    if alpha_box:
        img = img.crop(alpha_box)
    img.thumbnail((170, 170))

    off_img = mpl.offsetbox.OffsetImage(np.asarray(img), zoom = .27)
    label = mpl.offsetbox.AnnotationBbox(
        off_img, (-1.3, team_key),
        xycoords = 'data',
        frameon = False)
    ax.add_artist(label)
