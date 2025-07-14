# Chapter 8: Style Configuration

This is a brief chapter that might provide a sigh of relief. So many of the parameters we have tweaked so far, sometimes laboriously, can be altered in one go with `plt.style.use`. Try out the [many style sheets already available](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html). You may also define your own or simply change certain parameters directly in your code to apply that styling for your entire session.

## 8.1 rcParams

Change the matplotlib parameters directly by updating the dictionary-like variable `mpl.rcParams`. A full list of the available parameters can be found in the [documentation](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams) or you may simply print `mpl.rcParams` to inspect it directly. Note the above line is `mpl.rcParams` and not `plt.rcParams`, because we are not working within the pyplot submodule. Accordingly, you'll have to run `import matplotlib as mpl` first. Because this is like a Python dictionary, you can adjust the settings by simply updating the dictionary value, `mpl.rcParams['axes.grid'] = True` for example.

Working with `rcParams`, directly or through a custom style sheet, provides value that compounds as you add more and more plots to your code. Consider the two programs below. Without `rcParams`, we update each plot.

```python
x = np.linspace(0,1,2)

fig1, ax = plt.figure(), plt.axes()
ax.plot(x, x)
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()

fig2, ax = plt.figure(), plt.axes()
ax.plot(x, 1 - x)
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
```

Now let's update `rcParams` just once for a standard style.

```python
# Use rcParams
mpl.rcParams['axes.grid'] = True
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False

x = np.linspace(0,1,2)
plt.plot(x,x)
plt.savefig("style1.pdf")
plt.show()

plt.plot(x, 1-x)
plt.savefig("style2.pdf")
plt.show()
```

![Style 1](../images/chapter8/style1.png)

![Style 2](../images/chapter8/style2.png)

This is a significant step, nearing us to a dramatic close of Part I. In the second program, we not only save on redundant code, we also revert back to pyplot functions. The object-oriented approach was useful in offering greater customization. But, at least in this case, that's a ladder we can kick away now that we've climbed it to the top.

## 8.2 Defining Your Own Style

Once you understand rcParams, you can define your own style for repeated use. Schwabish (2021) counsels organizations to adopt a data visualization style guide. Practically, that also means matplotlib-using organizations should choose or create a standard matplotlib style.

To define your own style, create a file with the `.mplstyle` extension, specifying a value for the various rcParams you wish to customize. Note that a colon separates the key and the default like in a dictionary, but that we do not separate key-value pairs by commas and each pair is on a separate line. Further, none of these values are formatted as strings, even though you would, for example, use a string `'Times'` when updating the font from rcParams dictionary. You only need to specify values you wish to change relative to the default.

```
# tiny-style.mplstyle
axes.spines.left : True
axes.spines.right : False
axes.spines.bottom : True
axes.spines.top : False
xtick.labelsize : large
font.family : Times
```

After saving the above as a file `tiny_style.mplstyle` and placing it in the working directory, we can use our custom style with the program below. Note the colormap, among many other things, has not changed relative to the default because we did not alter that in the style file.

```python
plt.style.use('../../stylelib/tiny-style.mplstyle')

fig, ax = plt.figure(), plt.axes()
x = np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title('Hello')

# Inspect the updated rcParams
#print(mpl.rcParams)
```

![Tiny style example](../images/chapter8/tiny-style-ex.png)

You can also just save direct modifications to the rcParams dictionary and run that before plotting.

```python
import matplotlib as mpl
mpl.rcParams['axes.spines.left'] = True
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.bottom'] = True
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.titlesize'] = 25
mpl.rcParams['xtick.labelsize'] = 'large'
mpl.rcParams['font.family'] = 'Times'
```

Then add this code to ahead of creating your plot. I saved the above as `style_changes.py` and below I use the Jupyter `%run` magic command to run `style_changes.py` without having to copy and paste.

```python
plt.style.use('default')
%run ../../python/style-changes.py

x = np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title('Hello')
```

The result is

![Python styled](../images/chapter8/py-styled.png)

### 8.2.1 Temporary Configurations

With some creativity, you can also avoid modifying rcParams by defining a function or writing a Python file that makes certain standardized plot modifications and then run that after you've created your figure and axes objects, using the IPython `%run` magic command.

We save the following as `spine-mod.py` and then use it below to modify a plot.

```python
import matplotlib.pyplot as plt

plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
```

```python
x = np.linspace(0,2*np.pi,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title('Spine Mods')

%run ../../python/spine-mod.py
```

![Spine mod example](../images/chapter8/spine-mod-ex.png)

In the plot program, we use pyplot functions instead of using the OOP approach. Note that even if we created an `ax` variable, we must still use `plt.gca()` instead of `ax` in the file, because there is no `ax` to reference in `spine_mod.py`. We can instead use `%run -i` to let the file access our global variables. Also, `%run -i` eliminates the need to import matplotlib again—we could delete the import statement from `spine-mod.py` and use `%run -i spine-mod.py`.

We save the following file as `spine-mod2.py` and can create the same plot with the program further below.

```python
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

```python
x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.figure(), plt.axes()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
ax.set_title('Spine Mods')
%run -i ../../python/spine-mod2.py
```

![Spine mod 2 example](../images/chapter8/spine-mod2-ex.png)

A further complication arises if our figure contains multiple subplots. In this case, we can access all the axes objects as an attribute of the figure object.

```python
for ax in fig.axes:
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
```

## 8.3 A Final Prose Example

In this section, we'll integrate much of what we've learned so far to create a line chart that, though simple, is far from the default. We'll imitate a chart from the New York Times article, *The Pandemic Changed How We Spent Our Time*, by Ben Casselman and Ella Koeze. Below is the original.

![NYT ATUS Original](../images/nytATUS.png)

Imitating this graphic will take a lot of code, as demonstrated in Section 8.3.1. In Section 8.3.2, we invest in reconfiguring the style and creating functions that help reduce the tedium that would otherwise be required to make several plots of this style.

### 8.3.1 A First Go

The program below would be even longer if not for the use of dictionaries like `plot_style`, which pairs keyword arguments and specific values for the `plot()` method. This can be passed to `plot()` after being unpacked with the `**` operator.

```python
# Modified to save space - see full code in book
# This creates the NYT-style plot with manual styling

# Data
data = {2019: [6, 4.3, 3.9],
        2020: [7, 2.7, 4.4]}
df = pd.DataFrame(data = data,
                  index = ['Alone',
                         'With people outside household',
                         'With household members only'])

# Style dictionary
style_changes = {'axes.linewidth': 2,
                 'axes.facecolor': (.94, .94, .96),
                 'axes.grid.axis': 'y',
                 'axes.grid': True,
                 'grid.color': 'white',
                 'grid.linewidth': 2,
                 'axes.spines.bottom': True,
                 'axes.spines.top': False,
                 'axes.spines.left': False,
                 'axes.spines.right': False,
                 'axes.edgecolor': 'darkgray',
                 'xtick.bottom': False,
                 'xtick.top': False,
                 'ytick.left': False,
                 'xtick.labeltop':True,
                 'xtick.labelbottom':False,
                 'ytick.labelleft':False,
                 'xtick.color': (.3,.3,.3),
                 'text.color': (.3,.3,.3),
                 'font.size': 12,
                 'lines.marker': 'o',
                 'lines.markersize': 8,
                 'lines.linewidth': 3,
                 'axes.titlesize': 18,
                 'axes.titleweight': 'bold', 
                 'axes.formatter.useoffset': False}

# Apply style and create plot
mpl.rcParams.update(style_changes)

fig, ax = plt.figure(figsize = (8,6)), plt.axes()
x = [2019, 2020]

# Plot lines with custom styles
plot_style = {'linewidth': 3, 'markersize': 8, 'marker': 'o'}
ax.plot(x, [df[2019]['Alone'], df[2020]['Alone']], 
        color = (.1, .5, .4), **plot_style)
ax.plot(x, [df[2019]['With people outside household'], 
             df[2020]['With people outside household']], 
        color = (1, .6, .2), **plot_style)
ax.plot(x, [df[2019]['With household members only'], 
             df[2020]['With household members only']], 
        color = (.7, .2, .3), **plot_style)

# Annotations and labels
ax.set_ylim(0, 8)
ax.set_ylabel('HOURS PER DAY')
ax.set_xlim(2018.75, 2020.25)

# Labels on lines
ax.text(2019, df[2019]['Alone'] + 0.05, 'Alone',
        fontname = 'Helvetica', weight = 'bold',
        color = (.1, .5, .4), fontsize = 11)

ax.text(2019, df[2019]['With people outside household'] + 0.05,
        'With people',
        fontname = 'Helvetica', weight = 'bold',
        color = (1, .6, .2), fontsize = 11)

ax.text(2019, df[2019]['With people outside household'] - 0.15,
        'outside household',
        fontname = 'Helvetica', weight = 'bold',
        color = (1, .6, .2), fontsize = 11)

ax.text(2019, df[2019]['With household members only'] + 0.05,
        'With household',
        fontname = 'Helvetica', weight = 'bold',
        color = (.7, .2, .3), fontsize = 11)

ax.text(2019, df[2019]['With household members only'] - 0.15,
        'members only',
        fontname = 'Helvetica', weight = 'bold',
        color = (.7, .2, .3), fontsize = 11)

# Add COVID annotation
ax.annotate('COVID-19',
            xy = (2020, df[2020]['With people outside household']),
            xytext = (2020, 1.7),
            ha = 'center',
            fontname = 'Helvetica',
            arrowprops = dict(arrowstyle = '-', 
                            connectionstyle="angle3,angleA=0,angleB=-90",
                            color = (.3,.3,.3)))

# Title and subtitle
ax.text(0.5, 1.15, 'Americans are spending more time at home,',
        ha = 'center', transform = ax.transAxes,
        fontname = 'Helvetica', fontsize = 11)
ax.text(0.5, 1.19, 'The Pandemic Changed How We Spent Our Time',
        ha = 'center', transform = ax.transAxes,
        fontname = 'Helvetica', fontsize = 18, fontweight = 'bold',
        color = 'black')

plt.tight_layout()
```

![NYT replication 1](../images/chapter8/nyt-rep1.png)

### 8.3.2 Reconfigured, Refactored, and Reusable

```
# nyt-helper.mplstyle
axes.linewidth: 2
axes.facecolor: (.94, .94, .96)
axes.grid.axis: y
axes.grid: True
grid.color: white
grid.linewidth: 2
axes.spines.bottom: True
axes.spines.top: False
axes.spines.left: False
axes.spines.right: False
axes.edgecolor: darkgray
xtick.bottom: False
xtick.top: False
ytick.left: False
xtick.labeltop: True
xtick.labelbottom : False
ytick.labelleft: False
xtick.color: (.3,.3,.3)
text.color: (.3,.3,.3)
font.size: 12
lines.marker: o
lines.markersize: 8
lines.linewidth: 3
axes.titlesize: 18
axes.titleweight: bold
axes.formatter.useoffset: False
```

```python
def title_and_subtitle(title, subtitle = '', pad = 0.01, fig = None, ax = None):
    """Add a centered title and subtitle to a plot."""
    if ax == None:
        ax = plt.gca()
    if fig == None:
        fig = plt.gcf()
    fig.canvas.draw()

    top_of_figure = 1 # axes coords
    # update if there are xticks on the top
    tick0 = ax.get_xticklabels()[0]
    top_of_ticklabels = tick0.get_window_extent().transformed(ax.transAxes.inverted()).y1
    top_of_figure = max([top_of_ticklabels,top_of_figure])

    # Add subtitle
    if subtitle:
        subt = ax.text(0.5, top_of_figure + pad,
                       s = subtitle,
                       ha = 'center',
                       va = 'bottom',
                       size = '11',
                       fontname = 'Helvetica',
                       transform = ax.transAxes)
        # update top of figure to top of the subtitle
        top_of_figure = subt.get_window_extent().transformed(ax.transAxes.inverted()).y1

    # add title
    ax.text(0.5, top_of_figure + pad,
            s = title,
            ha = 'center',
            va = 'bottom',
            size = '18',
            fontname = 'Helvetica',
            fontweight = 'bold',
            transform = ax.transAxes,
            color = 'black')
```

```python
data = {2019: [6, 4.3, 3.9],
        2020: [7, 2.7, 4.4]}
df = pd.DataFrame(data = data,
                  index = ['Alone',
                         'With people outside household',
                         'With hosehould members only'])
```

```python
# Refactored version using style file and helper function
plt.style.use('../../stylelib/nyt-helper.mplstyle')

fig, ax = plt.figure(figsize = (8,6)), plt.axes()
x = [2019, 2020]

# Color palette
colors = [(.1, .5, .4), (1, .6, .2), (.7, .2, .3)]

# Plot lines
for activity, color in zip(df.index, colors):
    ax.plot(x, [df[2019][activity], df[2020][activity]], 
            color = color)

# Y-axis
ax.set_ylim(0, 8)
ax.set_ylabel('HOURS PER DAY', fontname = 'Helvetica',
              color = 'black', fontsize = 11)

# X-axis  
ax.set_xlim(2018.75, 2020.25)
ax.set_xticks([2019, 2020])

# Labels
label_info = [('Alone', df[2019]['Alone'], 0.05, colors[0]),
              ('With people', df[2019]['With people outside household'], 
               0.05, colors[1]),
              ('outside household', df[2019]['With people outside household'], 
               -0.15, colors[1]),
              ('With household', df[2019]['With household members only'], 
               0.05, colors[2]),
              ('members only', df[2019]['With household members only'], 
               -0.15, colors[2])]

for text, y_base, y_offset, color in label_info:
    ax.text(2019, y_base + y_offset, text,
            fontname = 'Helvetica', weight = 'bold',
            color = color, fontsize = 11)

# COVID annotation
ax.annotate('COVID-19',
            xy = (2020, df[2020]['With people outside household']),
            xytext = (2020, 1.7),
            ha = 'center',
            fontname = 'Helvetica',
            arrowprops = dict(arrowstyle = '-', 
                            connectionstyle="angle3,angleA=0,angleB=-90",
                            color = (.3,.3,.3)))

# Title and subtitle
title_and_subtitle(title = 'The Pandemic Changed How We Spent Our Time',
                  subtitle = 'Americans are spending more time at home,',
                  pad = 0.02)

plt.tight_layout()
```

![NYT refactor](../images/chapter8/nyt-refactor.png)