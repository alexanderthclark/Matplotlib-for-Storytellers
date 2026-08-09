from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "Data" / "nhl_regular_season.csv"
OUTPUT_PATH = ROOT / "figures" / "poetryplots"

seasons = [
    "1999-00", "2000-01", "2001-02", "2002-03", "2003-04",
    "2004-05", "2005-06", "2006-07", "2007-08", "2008-09",
]
teams = [
    "Detroit Red Wings", "Tampa Bay Lightning", "Nashville Predators",
    "New York Islanders", "Pittsburgh Penguins", "Chicago Blackhawks",
]

standings = pd.read_csv(DATA_PATH)
matrix = (
    standings.pivot(index="team", columns="season", values="point_pct")
    .reindex(index=teams, columns=seasons)
)

cmap = mpl.colormaps["Blues"].copy()
cmap.set_bad("#e9ecef")

fig, ax = plt.subplots(figsize=(10, 4.6))
image = ax.imshow(
    np.ma.masked_invalid(matrix.to_numpy()),
    aspect="auto",
    cmap=cmap,
    vmin=0.30,
    vmax=0.76,
)

ax.set_xticks(range(len(seasons)), labels=seasons, rotation=35, ha="left")
ax.set_yticks(range(len(teams)), labels=teams)
ax.xaxis.tick_top()
ax.tick_params(length=0, pad=7)
ax.set_title(
    "NHL regular-season points percentage",
    loc="left",
    fontsize=18,
    fontweight="bold",
    pad=22,
)

ax.text(
    seasons.index("2004-05"),
    (len(teams) - 1) / 2,
    "\n".join("LOCKOUT"),
    rotation=0,
    ha="center",
    va="center",
    color="#6c757d",
    fontsize=9,
    fontweight="bold",
    linespacing=0.92,
)

cbar = fig.colorbar(image, ax=ax, orientation="horizontal", pad=0.13,
                    fraction=0.07, aspect=40)
cbar.set_label("Points percentage")
cbar.ax.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
cbar.outline.set_visible(False)

for spine in ax.spines.values():
    spine.set_visible(False)

fig.tight_layout()
fig.savefig(OUTPUT_PATH / "hockey-heat-basic.pdf", bbox_inches="tight")
fig.savefig(OUTPUT_PATH / "hockey-heat-basic.png", bbox_inches="tight", dpi=180)
