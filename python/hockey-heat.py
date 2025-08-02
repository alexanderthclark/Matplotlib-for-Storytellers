import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image

fig, ax = plt.subplots(figsize = (10,10), facecolor = (.98, .98, .98))

# Real NHL teams and data from NHL.com historical standings
teams = ['Detroit', 'Pittsburgh', 'Chicago', 'Tampa Bay', 'Nashville', 'NY Islanders']
years = range(1999,2009)

# Points percentage data (2004-05 was lockout season)
# 99-00, 00-01, 01-02, 02-03, 03-04, 04-05, 05-06, 06-07, 07-08, 08-09
records = {
    'Detroit':      [.604, .622, .634, .683, .585, None, .721, .616, .659, .646],  # Dynasty
    'Pittsburgh':   [.451, .512, .378, .329, .231, None, .354, .524, .585, .549],  # Worst to playoffs
    'Chicago':      [.415, .402, .415, .366, .244, None, .329, .390, .476, .573],  # Rock bottom to rise
    'Tampa Bay':    [.238, .299, .329, .573, .573, None, .659, .537, .451, .549],  # Worst to Cup
    'Nashville':    [.341, .415, .354, .415, .537, None, .573, .549, .622, .537],  # Expansion growth
    'NY Islanders': [.463, .463, .476, .439, .439, None, .451, .488, .463, .317]   # Mediocre to worst
}

ax.set_aspect('equal')
ax.axis('off')

y_pad = -1
for team_key, team in enumerate(teams):
    for year_key, year in enumerate(years):

        year_str = str(year)[-2:] + "-" + str(year+1)[-2:]

        record = records[team][year_key]
        if record is not None:
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
            # Add team logo for Nashville, text for others
            if team == 'Nashville':
                try:
                    img = np.asarray(Image.open('../images/predators.png'))
                    off_img = mpl.offsetbox.OffsetImage(img, zoom=.016)
                    ab = mpl.offsetbox.AnnotationBbox(off_img, (-1, y_pad*team_key),
                                                      xycoords='data',
                                                      frameon = False)
                    ax.add_artist(ab)
                except:
                    ax.text(year_key - 1, y_pad*team_key,
                            s = team,
                            ha = 'right',
                            va= 'center')
            else:
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

# lockout annotation (2004-05 is at index 5)
string = 'No Season Due To Lockout'
ax.text(5, -3.5,
        s = '\n'.join(string),
        va= 'center',
        ha = 'center',
        size = 15)
ax.text(.5, 1.05,
        s = "Hockey Regular Season Records",
        size = 20,
        ha = 'center',
        va = 'bottom',
        transform = ax.transAxes)

plt.tight_layout()
plt.savefig('../figures/poetryplots/hockey-heat.pdf', bbox_inches='tight')
plt.savefig('../figures/poetryplots/hockey-heat.png', bbox_inches='tight', dpi=150)