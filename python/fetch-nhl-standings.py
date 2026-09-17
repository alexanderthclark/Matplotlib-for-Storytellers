import json
from urllib.request import Request, urlopen

import pandas as pd

season_end_dates = {
    '1999-00': '2000-04-09',
    '2000-01': '2001-04-08',
    '2001-02': '2002-04-14',
    '2002-03': '2003-04-06',
    '2003-04': '2004-04-04',
    '2005-06': '2006-04-18',
    '2006-07': '2007-04-08',
    '2007-08': '2008-04-06',
    '2008-09': '2009-04-12'
}
team_order = ['DET', 'TBL', 'NSH', 'WSH', 'PIT', 'CHI']

rows = []
for season, season_end in season_end_dates.items():
    url = 'https://api-web.nhle.com/v1/standings/' + season_end
    request = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    with urlopen(request, timeout = 30) as response:
        standings = json.load(response)['standings']

    selected = {row['teamAbbrev']['default']: row
                for row in standings
                if row['teamAbbrev']['default'] in team_order}

    for abbreviation in team_order:
        team = selected[abbreviation]
        rows.append({
            'season': season,
            'season_end': season_end,
            'team': team['teamName']['default'],
            'team_abbrev': abbreviation,
            'games_played': team['gamesPlayed'],
            'points': team['points'],
            'point_pct': team['pointPctg']
        })

standings = pd.DataFrame(rows)
standings.to_csv('Data/nhl_regular_season.csv',
                 index = False,
                 float_format = '%.6f')
