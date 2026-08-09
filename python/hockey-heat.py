from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import Circle
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "Data" / "nhl_regular_season.csv"
OUTPUT_PATH = ROOT / "figures" / "poetryplots"

TEAM_MARKS = {
    "Detroit Red Wings": ROOT / "images" / "nhl" / "DET.png",
    "Tampa Bay Lightning": ROOT / "images" / "nhl" / "TBL.png",
    "Nashville Predators": ROOT / "images" / "predators.png",
    "New York Islanders": ROOT / "images" / "nhl" / "NYI.png",
    "Pittsburgh Penguins": ROOT / "images" / "nhl" / "PIT.png",
    "Chicago Blackhawks": ROOT / "images" / "nhl" / "CHI.png",
}

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


def bubble_radius(value):
    """Restore the expanding-bubble scale used in the original figure."""
    return 0.25 + value / 2


def load_team_mark(path, max_size=170):
    """Crop transparent padding and normalize marks to a common pixel box."""
    with Image.open(path).convert("RGBA") as mark:
        alpha_bbox = mark.getchannel("A").getbbox()
        if alpha_bbox:
            mark = mark.crop(alpha_bbox)
        mark.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        return np.asarray(mark)

background = (0.98, 0.98, 0.98)
fig, ax = plt.subplots(figsize=(11.5, 5.8), facecolor=background)
ax.set_facecolor(background)
bubble_color = "C0"

lockout = seasons.index("2004-05")
ax.axvspan(lockout - 0.5, lockout + 0.5, color="#eceff1", zorder=0)

for row, team in enumerate(teams):
    for column, season in enumerate(seasons):
        value = matrix.loc[team, season]
        if np.isnan(value):
            continue

        circle = Circle(
            (column, row),
            radius=bubble_radius(value),
            facecolor=bubble_color,
            edgecolor=bubble_color,
            linewidth=1.0,
            alpha=value,
            zorder=2,
        )
        ax.add_patch(circle)

        ax.text(
            column,
            row,
            f"{value:.0%}",
            ha="center",
            va="center",
            color="#102a43",
            fontsize=11,
            fontweight="bold",
            zorder=3,
        )

ax.text(
    lockout,
    (len(teams) - 1) / 2,
    "\n".join("LOCKOUT"),
    rotation=0,
    ha="center",
    va="center",
    color="#607d8b",
    fontsize=9.5,
    fontweight="bold",
    linespacing=0.92,
    zorder=4,
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
        color=bubble_color,
        fontsize=10.5,
        fontweight="bold",
    )

for row, team in enumerate(teams):
    mark = OffsetImage(load_team_mark(TEAM_MARKS[team]), zoom=0.27)
    label = AnnotationBbox(
        mark,
        (-1.30, row),
        frameon=False,
        box_alignment=(0.5, 0.5),
        annotation_clip=False,
        zorder=5,
    )
    ax.add_artist(label)

season_labels = [season[2:] for season in seasons]
ax.set_xticks(range(len(seasons)), labels=season_labels)
ax.set_yticks([])
ax.xaxis.tick_top()
ax.tick_params(axis="both", length=0, pad=8, labelsize=11)

ax.set_xlim(-1.95, 12.0)
ax.set_ylim(len(teams) - 0.38, -0.78)
ax.set_aspect("equal")
ax.set_title(
    "After the lockout, two rebuilds emerge",
    loc="left",
    fontsize=22,
    fontweight="bold",
    pad=72,
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

for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(
    0.14,
    0.015,
    "Source: NHL season-end standings. Team marks: NHL. Points percentage = points / (2 x games played).",
    ha="left",
    va="bottom",
    color="#6c757d",
    fontsize=9.5,
)

fig.savefig(OUTPUT_PATH / "hockey-heat.pdf", bbox_inches="tight")
fig.savefig(OUTPUT_PATH / "hockey-heat.png", bbox_inches="tight", dpi=180)
