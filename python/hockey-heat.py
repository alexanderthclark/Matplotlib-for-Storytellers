from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle

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
expected = standings["points"] / (2 * standings["games_played"])
np.testing.assert_allclose(standings["point_pct"], expected, atol=1e-6)

matrix = (
    standings.pivot(index="team", columns="season", values="point_pct")
    .reindex(index=teams, columns=seasons)
)

fig, ax = plt.subplots(figsize=(11.5, 5.8), facecolor="white")
norm = mpl.colors.Normalize(vmin=0.30, vmax=0.76)
cmap = mpl.colormaps["Blues"]
accent = "#1565c0"

lockout = seasons.index("2004-05")
ax.axvspan(lockout - 0.5, lockout + 0.5, color="#eceff1", zorder=0)

for row, team in enumerate(teams):
    for column, season in enumerate(seasons):
        value = matrix.loc[team, season]
        if np.isnan(value):
            continue

        color = cmap(norm(value))
        circle = Circle(
            (column, row),
            radius=0.38,
            facecolor=color,
            edgecolor="white",
            linewidth=1.4,
            zorder=2,
        )
        ax.add_patch(circle)

        red, green, blue = color[:3]
        luminance = (
            0.2126 * red
            + 0.7152 * green
            + 0.0722 * blue
        )
        if luminance < 0.55:
            text_color = "white"
        else:
            text_color = "#102a43"
        ax.text(
            column,
            row,
            f"{value:.0%}",
            ha="center",
            va="center",
            color=text_color,
            fontsize=11,
            fontweight="bold",
            zorder=3,
        )

ax.text(
    lockout,
    (len(teams) - 1) / 2,
    r"NO SEASON  $\bullet$  LOCKOUT",
    rotation=90,
    ha="center",
    va="center",
    color="#607d8b",
    fontsize=9.5,
    fontweight="bold",
)

callouts = [
    (
        "Pittsburgh Penguins",
        "35%  $\\rightarrow$  64%\nby 2006-07",
    ),
    (
        "Chicago Blackhawks",
        "36%  $\\rightarrow$  63%\nby 2008-09",
    ),
]
for team, label in callouts:
    row = teams.index(team)
    ax.text(
        10.25,
        row,
        label,
        ha="left",
        va="center",
        color=accent,
        fontsize=10.5,
        fontweight="bold",
    )

ax.set_xticks(range(len(seasons)), labels=seasons, rotation=35, ha="left")
ax.set_yticks(range(len(teams)), labels=teams)
ax.xaxis.tick_top()
ax.tick_params(axis="both", length=0, pad=8, labelsize=11)
for label in ax.get_yticklabels():
    if label.get_text() in {"Pittsburgh Penguins", "Chicago Blackhawks"}:
        label.set_color(accent)
        label.set_fontweight("bold")

ax.set_xlim(-0.65, 11.75)
ax.set_ylim(len(teams) - 0.45, -0.7)
ax.set_aspect("equal")
ax.set_title(
    "After the lockout, two rebuilds emerge",
    loc="left",
    fontsize=22,
    fontweight="bold",
    pad=90,
)
ax.text(
    0,
    1.18,
    "Regular-season points percentage for six selected NHL teams, 1999-00 to 2008-09",
    transform=ax.transAxes,
    ha="left",
    va="bottom",
    color="#52606d",
    fontsize=11.5,
)

sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
cbar = fig.colorbar(sm, ax=ax, orientation="horizontal", pad=0.11,
                    fraction=0.045, aspect=45, shrink=0.62, anchor=(0, 0.5))
cbar.set_label("Points percentage", color="#52606d")
cbar.ax.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1.0))
cbar.outline.set_visible(False)
cbar.ax.tick_params(length=0, colors="#52606d")

for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(
    0.16,
    0.015,
    "Source: NHL season-end standings. Points percentage = points / (2 x games played).",
    ha="left",
    va="bottom",
    color="#6c757d",
    fontsize=9.5,
)

fig.savefig(OUTPUT_PATH / "hockey-heat.pdf", bbox_inches="tight")
fig.savefig(OUTPUT_PATH / "hockey-heat.png", bbox_inches="tight", dpi=180)
