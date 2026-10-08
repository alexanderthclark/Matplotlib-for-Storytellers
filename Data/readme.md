# Data

This folder contains CSV files used in the examples throughout *Matplotlib for Storytellers*, including Google Trends search interest and NHL regular-season standings. The [Google Trends](https://trends.google.com) files contain normalized search interest values ranging from 0–100. That search interest data is provided here for educational use and remains subject to Google's Terms of Service.

## Google Trends files

- **AristotleSparkNotesTrends.csv** – Weekly U.S. search interest for "Aristotle" and "SparkNotes" from January 2019 through December 2020.
- **SparkNotesFall2019.csv** – Daily U.S. search interest for "SparkNotes" covering August–December 2019.
- **finalFourTrend.csv** – Monthly U.S. search interest for "Final four" from January 2004 through July 2021.
- **HopperOstromTrends.csv** – Monthly U.S. search interest for "Grace Hopper" and "Elinor Ostrom" from January 2004 through July 2021.
- **WeatherAug1415Trends.csv** – Minute-level search interest for "weather" collected August 14–15, 2021 (time zone −04:00).

## NHL data

- **nhl_regular_season.csv** – Final regular-season standings for six NHL teams from 1999–00 through 2008–09, retrieved from the [official NHL standings API](https://api-web.nhle.com/v1/standings-season) using [`fetch-nhl-standings.py`](../python/fetch-nhl-standings.py). Includes season and end date, team name and abbreviation, games played, points, and points percentage (`points / (2 × games played)`, on a 0–1 scale). The cancelled 2004–05 season has no rows because of the league-wide lockout.
