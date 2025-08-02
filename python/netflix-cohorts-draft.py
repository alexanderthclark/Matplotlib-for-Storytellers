import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (10,8), facecolor = (.98, .98, .98))

# Netflix cohorts by sign-up year
cohorts = ['2016 Cohort', '2017 Cohort', '2018 Cohort', '2019 Cohort', '2020 Cohort', '2021 Cohort']
years = range(2016, 2023)

# Average daily watch time in hours
# Newer cohorts tend to watch more, everyone spikes during COVID (2020-2021)
watch_time = {
    '2016 Cohort': [1.8, 1.9, 2.0, 2.1, 3.2, 2.8, 2.3],
    '2017 Cohort': [None, 2.0, 2.1, 2.2, 3.4, 3.0, 2.4],
    '2018 Cohort': [None, None, 2.2, 2.3, 3.6, 3.2, 2.6],
    '2019 Cohort': [None, None, None, 2.4, 3.8, 3.4, 2.8],
    '2020 Cohort': [None, None, None, None, 4.2, 3.8, 3.2],
    '2021 Cohort': [None, None, None, None, None, 3.6, 3.0]
}

ax.set_aspect('equal')
ax.axis('off')

y_pad = -1
max_hours = 4.5  # Maximum for scaling

for cohort_key, cohort in enumerate(cohorts):
    for year_key, year in enumerate(years):
        
        year_str = str(year)
        
        hours = watch_time[cohort][year_key]
        if hours is not None:
            # Scale radius based on watch time
            radius = 0.15 + (hours / max_hours) * 0.35
            
            # Color based on watch time intensity
            if hours >= 3.5:
                color = '#B71C1C'  # Dark red for heavy viewing
            elif hours >= 3.0:
                color = '#E53935'  # Red for high viewing
            elif hours >= 2.5:
                color = '#FF6F00'  # Orange for moderate-high
            else:
                color = '#1976D2'  # Blue for normal viewing
            
            circ = plt.Circle((year_key, y_pad*cohort_key),
                      radius = radius,
                      color = color,
                      alpha = 0.8)
            ax.add_artist(circ)
            
            # Add hours text
            ax.text(year_key, y_pad*cohort_key,
                    s = f"{hours:.1f}h",
                    va= 'center',
                    ha = 'center',
                    fontsize = 10,
                    fontweight = 'bold' if hours >= 3.5 else 'normal',
                    color = 'white' if hours >= 3.0 else 'black')
        
        # Add cohort labels
        if year_key == 0:
            ax.text(year_key - 0.8, y_pad*cohort_key,
                    s = cohort,
                    ha = 'right',
                    va= 'center',
                    fontsize = 11)
        
        # Add year labels
        if cohort_key == 0:
            ax.text(year_key, y_pad*cohort_key + 0.8,
                    s = year_str,
                    ha = 'center',
                    va = 'bottom',
                    fontsize = 11)

ax.set_ylim(y_pad*5 - 1, 1.5)
ax.set_xlim(-2, len(years))

# COVID annotation
ax.annotate('COVID-19\nPandemic', 
            xy=(4, -2.5), 
            xytext=(4, -0.5),
            ha='center',
            va='bottom',
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='#FFE0B2', alpha=0.8),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

# Title
ax.text(0.5, 1.08,
        s = "Netflix Daily Watch Time by Sign-up Cohort",
        size = 18,
        ha = 'center',
        va = 'bottom',
        transform = ax.transAxes,
        fontweight = 'bold')

# Subtitle
ax.text(0.5, 1.03,
        s = "Average hours watched per day • Bubble size indicates viewing intensity",
        size = 12,
        ha = 'center',
        va = 'bottom',
        transform = ax.transAxes,
        style = 'italic')

# Legend
legend_y = -6.5
for i, (hours, color, label) in enumerate([
    (4.0, '#B71C1C', 'Heavy (3.5+ hrs)'),
    (3.2, '#E53935', 'High (3.0-3.4 hrs)'),
    (2.7, '#FF6F00', 'Moderate (2.5-2.9 hrs)'),
    (2.2, '#1976D2', 'Normal (<2.5 hrs)')
]):
    x_pos = -1.5 + i * 2.1
    radius = 0.15 + (hours / max_hours) * 0.35
    circ = plt.Circle((x_pos, legend_y),
              radius = radius,
              color = color,
              alpha = 0.8)
    ax.add_artist(circ)
    ax.text(x_pos, legend_y - 0.6,
            s = label,
            ha = 'center',
            va = 'top',
            fontsize = 9)

plt.tight_layout()
plt.savefig('../figures/poetryplots/netflix-cohorts.pdf', bbox_inches='tight')
plt.savefig('../figures/poetryplots/netflix-cohorts.png', bbox_inches='tight', dpi=150)