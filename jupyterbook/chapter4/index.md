# Chapter 4: Text and Titles

## 4.1 Simple Titles

As we learned in Chapter 1, we can add a title with the axes method `set_title()`. Simply pass the string of your choice as the argument. For multi-line titles, recall `\n` can be used in a string to start a new line. Common optional arguments include `color`, `fontsize`, `weight`, and `loc`.

Colors will be addressed in Chapter 6, but to start you can simply use the name of any not-too-exotic color as a string.

`fontsize` (or `size`) can be a number or chosen from `'small'`, `'medium'`, or `'large'`, and `'small'` and `'large'` may be intensified with a `'x-'` or `'xx-'` prefix. Similarly, `weight` (or `fontweight`) can be a number or chosen from options like `'bold'` or `'light'`.

`loc` determines the location of the title, either `'left'`, `'center'`, or `'right'`. In the default style, the default value will be `'center'`. You might prefer using `'left'` to match the Google Sheets default (thus matching the vast majority of plots I've seen in industry).
`pad` controls the space between the title and the top of the axes.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_title("This", fontsize = 24, weight = 'bold', 
             color = 'purple', loc = 'left')
ax.text(0.5, 0.5, 'Using a big pad...', 
        ha = 'center', va = 'center', fontsize = 18)

# set_title returns a text object, get/set methods
title = ax.set_title("This", fontsize = 24, weight = 'bold', 
                     color = 'purple', loc = 'left')
# Using the text object's methods
title.set_pad(50)
# Equivalently...
# ax.set_title(..., pad = 50)
```

![Title with padding](../images/chapter4/title-pad.png)

```python
fig, ax = plt.figure(), plt.axes()
ax.set_title("This", fontsize = 24, weight = 'bold', 
             color = 'purple', loc = 'left')
ax.text(0.5, 0.5, 'Using a normal pad...', 
        ha = 'center', va = 'center', fontsize = 18)
```

![Title with no padding](../images/chapter4/title-no-pad.png)

A plot can actually have one title for every `loc` value as well.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_title("Left Title", loc = 'left')
ax.set_title("Center Title", loc = 'center')
ax.set_title("Right Title", loc = 'right')

ax.text(0.5, 0.5, 'Note center titles overwrite', 
        ha = 'center', va = 'center')
ax.set_title("Center Title 2", loc = 'center', 
             color = 'red')
```

![Title locations](../images/chapter4/title-loc.png)

## 4.2 Text and Placement

Matplotlib offers `text` as both a figure and an axes method. Let's start with some code to understand what they do. Both take $x$ and $y$ positions as the first two arguments and then a string. The figure method method is the same as using the axes method with a transformation to figure coordinates.

```python
fig, ax = plt.figure(facecolor = 'lightyellow'), plt.axes()
ax.set_xlim([0,10])
ax.set_ylim([0,10])
fig.text(0.5, 0.5, 'Figure Text', fontsize = 20, 
         ha = 'center')
ax.text(0.5, 0.5, 'Axes Text', fontsize = 20, 
        ha = 'center')
```

![Text methods](../images/chapter4/text-methods.png)

Immediately, we see that despite passing the same $x$ and $y$ position values, the figure and axes methods place the text differently. By default, the figure method uses "figure" coordinates, where (0,0) is the bottom left and (1,1) is the top right. The axes method uses $x$ and $y$ data coordinates by default. We will modify this shortly.

A more common concern is the alignment of the text. Both figure and axes text methods include parameters `verticalalignment` and `horizontalalignment`, which can be abbreviated as `va` and `ha`. By default, the text is placed so that the given coordinate is at the bottom-left corner of the text.

```python
fig, ax = plt.figure(), plt.axes()
ax.plot(0.5, 0.5, 'rx', markersize = 10, markeredgewidth = 3)
ax.text(0.5, 0.5, 'Default (bottom/left)', fontsize = 20)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
```

![Default text alignment](../images/chapter4/text-default-align.png)

For vertical alignment, the options are `'top'`, `'bottom'`, or `'center'`. For horizontal alignment, the options are `'left'`, `'right'`, or `'center'`. The default demonstrated above was `'bottom'` and `'left'`. It does result in the text being above and to the right of the coordinate point, perhaps confusingly, but the interpretation is that the coordinate point is at the bottom-left of the text. The possible alignments are illustrated below.

```python
fig, ax = plt.figure(figsize = (6, 6)), plt.axes()

vas = ['top', 'center', 'bottom']
has = ['left', 'center', 'right']

for i, va in enumerate(vas):
    for j, ha in enumerate(has):
        x = j / 2
        y = 1 - i / 2
        ax.plot(x, y, 'ko', markersize = 5)
        ax.text(x, y, f'{va}\n{ha}', 
                va = va, ha = ha, fontsize = 12,
                bbox = dict(boxstyle = 'round', 
                           facecolor = 'lightblue'))

ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_title('Text Alignment Options')
```

![Text alignment](../images/chapter4/text-align.png)

Text can be rotated with the `rotation` parameter. By default, a plot isn't square—the aspect ratio (the ratio of $y$-unit to $x$-unit) is not one. That means that the 45 degree line created by $y=x$ is not actually plotted at 45 degrees. Yet according to the `rotation` parameter, text rotated at 45 degrees is plotted at 45 degrees—that angle is not converted based on the aspect ratio. Later in Section 4.6, I go into further detail in how to use some trigonometry to get the exact angle if you'd like to slope text at some angle, accounting for the aspect ratio.

```python
for aspect in 2, 1, 0.5:
    fig, ax = plt.figure(), plt.axes()
    ax.set_aspect(aspect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.plot([0, 1], [0, 1], 'b-')
    ax.text(0.5, 0.5, 'Rotated Text', 
            rotation = 45, ha = 'center', va = 'center')
    ax.set_title(f'Aspect Ratio: {aspect}')
```

![Text rotation aspect 2](../images/chapter4/text-rotation2.png)
![Text rotation aspect 1](../images/chapter4/text-rotation1.png)
![Text rotation aspect 0.5](../images/chapter4/text-rotation05.png)

### 4.2.1 Text Formatting for Numbers

Here I've tucked away a subsection on formatting numbers in Python. This has nothing to do with matplotlib, formally speaking. Still, sometimes you want your text annotations or titles to contain numbers formatted just so and you'll want Python to figure that out instead of doing it by hand. You might want commas as the thousands separator (the more readable 1,000,000 instead of 1000000), you might want leading zeros (01 instead of 1), or you might want a currency symbol ($2 instead of 2). The table below demonstrates by example how to do this with `str.format`.

| Code | Output |
|------|---------|
| `'{:,}'.format(10**6)` | `'1,000,000'` |
| `'${:,.2f}'.format(10**6)` | `'$1,000,000.00'` |
| `'{:0>3.0f}'.format(1)` | `'001'` |
| `'{:>3.0f}'.format(1)` | `'  1'` |
| `'${:0>4.0f}'.format(1)` | `'$0001'` |
| `'{:+,.1f}'.format(1000)` | `'+1,000.0'` |
| `'{:0<+4,.1f}'.format(-1)` | `'-1.0'` |
| `'{:0<5.0f}'.format(1)` | `'10000'` |
| `'{:0<5,.0f}'.format(1)` | `'10000'` |
| `'{:0<8,.0f}'.format(1000)` | `'1,000000'` |
| `'{:.0e}'.format(10.1**6)` | `'1e+06'` |
| `'{:.1f} and {:.1f}'.format(9, 1)` | `'9.0 and 1.0'` |
| `'{1:.1f} and {0:.1f}'.format(9, 1)` | `'1.0 and 9.0'` |
| `'{0:} and {0}'.format(1)` | `'1 and 1'` |
| `'{:} and {:}'.format(1)` | `IndexError` |

Understanding everything above requires some knowledge of [format specifications](https://docs.python.org/3/library/string.html#format-specification-mini-language). A format specifier is a string that can specify fill, align, sign, width, grouping option, precision, and type (`[[fill]align][sign][#][0][width][grouping_option][.precision][type]`). These must be properly ordered but anything can be omitted to accept the default. These arguments go inside curly braces and to the right of a colon, `{:}`. The curly braces tell Python where to place the argument you pass to the `format()` method. You can also pass multiple arguments inside `format()`. By default, they are placed in order (the first argument replaces the first `{}` and so on), but to the left of the colon, you can also specify the index value for the argument to use.

The *fill* is a character that can be used to pad the number. Used with a *align* and *width*, we can add leading zeros. The default is a space if no fill character is provided. Using `'0>4'`, this will create leading zeros (right-aligned) up to a width of 4. So `1` becomes `'0001'` and `10000` is not padded, being simply `'10000'`.

The *grouping option* would come next, allowing for a thousands separator of a comma or an underscore. `'{:,}'.format(10000)` produces `'10,000'`. Note that when used with padded numerals on the right, the padding is ignored in finding the thousands separators, so `'{:0<8,.0f}'.format(1000)` produces the confusing `'1,000000'`.

*Precision* is next with a decimal and then how many digits to display past the decimal place or before and after, depending on the lastly specified *type*. Observe `'{:.2}'.format(np.pi)` produces `'3.1'` and `'{:.2f}'.format(np.pi)` produces `'3.14'`. You'll want type `'f'` for a float. Use `'e'` for scientific notation. You may read up on the many other types, including locale aware types, in the Python documentation.

Whatever we put outside the curly braces is simply concatenated to the text on the left or right. So `'${}'.format(123)` turns 123 into the dollar figure `'$123'`. And `'{} lbs.'.format(123)` would produce `'123 lbs'`.

Perhaps this will come in handy when you'd like figure text or the filename in a certain format. I often use leading zeros in some filenames so that alphabetically ordering the files will be coherent (your file system will likely maintain `'1' < '10' < '2'`). If you are creating many plots that will be frames in an animation, and you'll have some number ticking up as the frames progress, the padding might help the eye.

```python
# Create plots with zero-padded filenames
for i in range(3):
    fig, ax = plt.figure(), plt.axes()
    ax.text(0.5, 0.5, '{:0>4.0f}'.format(i), 
            fontsize = 100, ha = 'center', va = 'center',
            fontname = 'Courier New')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig('proseplots/{:0>4.0f}.pdf'.format(i))
```

![Text formatting 0000](../images/chapter4/0000.png) ![Text formatting 0001](../images/chapter4/0001.png) ![Text formatting 0002](../images/chapter4/0002.png)

## 4.3 Legends

As you should know, legends provide a key to the colors and symbols used in a plot. You can create a legend with `legend()`, as either a figure or axes method. Without any extra customization this is done with `ax.legend()` or `fig.legend()`. Here, we will only cover axes legends. We'll return to figure legends when they are more naturally useful in Chapter 7 on multiple axes and multiple plots.

But first, you need labels for your plot elements (called *artist* objects) before you can create a legend. This can be done with the `label` parameter in methods like `plot()`. Or you can use `set_label()` on the plot element object. Using `set_label()` adds some complication to the code, as seen below in an otherwise simple example. Note the legend needs to be added after the labeled plot elements you want included in the legend.

```python
fig, ax = plt.figure(), plt.axes()

# Three ways to label
# Way 1: Using the label parameter
ax.plot([0, 1], [0, 1], label = 'Method 1: label parameter')

# Way 2: Using set_label() on the line object
line2, = ax.plot([0, 1], [1, 0])
line2.set_label('Method 2: set_label()')

# Way 3: Pass labels directly to legend
line3, = ax.plot([0, 1], [0.5, 0.5])
ax.legend([line3], ['Method 3: legend labels'])
```

![Legend labels](../images/chapter4/legend-labels.png)

If you are using a pandas plot method, the labels will be set automatically according to the column or series names. For such instances where an element is automatically included in a legend and you want to exclude it, you can exclude that element by specifying `label = '_nolegend_'` in the plot call.

```python
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [2, 3, 1],
                   'C': [3, 1, 2]})

fig, ax = plt.figure(), plt.axes()
df.plot(ax = ax)
# Exclude column C from legend
ax.plot(df.index, df['C'] * 2, 
        label = '_nolegend_', color = 'gray')
ax.legend()
```

![Pandas legend](../images/chapter4/pd-legend.png)

A more common concern might be how to customize the placement of the legend and its actual appearance.

To change the placement of the legend, you may use the `loc` parameter. The default value is `'best'`, where best is determined by matplotlib. Other valid values are `'center'` and `'right'` (but not `'left'`) and then modifications like `'upper center'`, `'center right'`, and `'lower left'`.

For further customization of the placement, use the `bbox_to_anchor` parameter. This accepts 2-tuple or 4-tuple, giving the $x$ location, the $y$ location, and the width and height optionally.

By default, $x$ and $y$ are in axes coordinates. So the program below places a legend in the top and center of the axes. The alignment is done according to `loc`. If, for example, `loc = 'lower right'`, then the lower right corner of the legend is placed at the specified $x$ and $y$.

```python
fig, ax = plt.figure(), plt.axes()
ax.plot([0, 1], [0, 1], label = 'Line 1')
ax.plot([0, 1], [1, 0], label = 'Line 2')
ax.legend(bbox_to_anchor = (0.5, 1))
```

![Legend bbox](../images/chapter4/legend-bb.png)

```python
fig, ax = plt.figure(), plt.axes()
ax.plot([0, 1], [0, 1], label = 'Line 1')
ax.plot([0, 1], [1, 0], label = 'Line 2')
ax.legend(bbox_to_anchor = (0.5, 1), 
          loc = 'lower center')
```

![Legend bbox loc](../images/chapter4/legend-bb-loc.png)

If using a 4-tuple, the tuple is interpreted as the plot region in which to put the legend, according to `loc`.

Use `bbox_transform` to use a coordinate system other than the default axes coordinates.

```python
fig, ax = plt.figure(facecolor = 'lightyellow'), plt.axes()
ax.plot([0, 1], [0, 1], label = 'Line 1')
ax.plot([0, 1], [1, 0], label = 'Line 2')
ax.legend(bbox_to_anchor = (0.5, 0.5), 
          bbox_transform = fig.transFigure,
          loc = 'center')
```

![Legend transform](../images/chapter4/legend-transform.png)

There are many parameters to change the appearance of the legend. We won't cover all of them. Two useful parameters are `facecolor` and `ncol`. The former changes the background color of the legend and the latter sets the number of columns, changing the default shape of the legend. I use these and a few other self-explanatory parameters in the program below.

```python
fig, ax = plt.figure(), plt.axes()
for i in range(5):
    ax.plot([0, 1], [i, i], label = f'Line {i+1}')
    
ax.legend(facecolor = 'lightgray',
          ncol = 3,
          title = 'Legend Title',
          fontsize = 10,
          shadow = True,
          framealpha = 0.8)
```

![Legend shape](../images/chapter4/legend-shape.png)

## 4.4 Annotations

Knaflic (2015) and Schwabish (2021) both advise to label data directly and to annotate graphs with explanatory notes when helpful, as this helps convey the meaning of the graph more simply and directly.

You can annotate a chart with `text()` method calls, or you can use the `annotate()` method, for which you specify the text placement and a line segment to the part of the graph the text references.

### 4.4.1 Labeling and Arrows

The following graph is nothing special, but we avoid having to create a legend by labeling the data with the text color matching the line color.

```python
fig, ax = plt.figure(), plt.axes()

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax.plot(x, y1, color = 'blue')
ax.plot(x, y2, color = 'red')

# Label at the end of lines
ax.text(x[-1], y1[-1], 'sin(x)', 
        color = 'blue', va = 'center')
ax.text(x[-1], y2[-1], 'cos(x)', 
        color = 'red', va = 'center')

ax.set_xlim(0, 10.5)
```

![Label data](../images/chapter4/label-data.png)

Next, we use the `annotate()` method. This method comes with the option to include an arrow pointing from `xytext` to the point `xy`.

```python
fig, ax = plt.figure(), plt.axes()

x = np.linspace(0, 1, 100)
y = -x * np.log2(x) - (1-x) * np.log2(1-x)

ax.plot(x, y)
ax.set_xlabel('Probability of Heads')
ax.set_ylabel('Entropy')
ax.set_title('Entropy of a Coin Flip')

# Annotate the maximum
ax.annotate('Maximum entropy at p=0.5',
            xy = (0.5, 1), 
            xytext = (0.7, 0.8),
            arrowprops = dict(arrowstyle = '->'))
```

![Annotate arrow](../images/chapter4/annotate-arrow.png)

If you would like an arrow and no text, simply use the empty string `''`. It is necessary to pass a dictionary to the `arrowprops` property.

```python
fig, ax = plt.figure(), plt.axes()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Arrow only
ax.annotate('', xy = (0.8, 0.8), 
            xytext = (0.2, 0.2),
            arrowprops = dict(arrowstyle = '->', 
                            lw = 2, color = 'red'))
```

![Arrow only](../images/chapter4/arrow-only.png)

Lastly, one can also reference specific artist objects in the annotation instead of coordinates. In the below we place the annotations at the end of `a_line` and `b_line`.

```python
fig, ax = plt.figure(), plt.axes()

x = np.linspace(0, 2*np.pi, 100)
a_line, = ax.plot(x, np.sin(x), label = 'sin')
b_line, = ax.plot(x, np.cos(x), label = 'cos')

# Use the line objects for coordinates
ax.annotate('Peak', xy = (np.pi/2, 1), 
            xytext = (np.pi/2 + 0.5, 1.2),
            arrowprops = dict(arrowstyle = '->'),
            xycoords = a_line)

ax.annotate('Trough', xy = (np.pi, -1), 
            xytext = (np.pi + 0.5, -1.2),
            arrowprops = dict(arrowstyle = '->'),
            xycoords = b_line)
```

![Direct annotation](../images/chapter4/direct-annotation.png)

## 4.5 Fancy Titles

If you'd like to format different parts of the title different, you'll have to move beyond simply using `set_title`. The New York Times, for example, routinely includes a title and a subtitle in a plot. This requires using `text()` and `set_title()` separately, as there can only be one format style applied to a title. A simple example is below.

```python
fig, ax = plt.figure(), plt.axes()

# Main title
ax.set_title('Main Title', fontsize = 16, 
             weight = 'bold')

# Subtitle
ax.text(0.5, 0.95, 'This is a subtitle with additional information',
        transform = ax.transAxes,
        ha = 'center', va = 'top',
        fontsize = 12, color = 'gray')

ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
```

![Subtitle](../images/chapter4/subtitle.png)

### 4.5.1 Multi-colored Titles

In Chapter 3, we created a multi-colored title using the Artist method `get_window_extent()`. The advantage of a multi-colored title is that we can do without a legend. For someone who doesn't want to get into the complications of `get_window_extent()`, the $x$ and $y$ placement of the text could be done by sight.

```python
fig, ax = plt.figure(), plt.axes()

# Data
years = [2020, 2021, 2022]
product_a = [100, 120, 140]
product_b = [100, 110, 105]

ax.plot(years, product_a, color = 'green', linewidth = 2)
ax.plot(years, product_b, color = 'orange', linewidth = 2)

# Multi-colored title by eye
y = 1.05
ax.text(0.3, y, 'Product', transform = ax.transAxes)
ax.text(0.42, y, 'A', transform = ax.transAxes, 
        color = 'green', weight = 'bold')
ax.text(0.48, y, 'vs', transform = ax.transAxes)
ax.text(0.56, y, 'B', transform = ax.transAxes, 
        color = 'orange', weight = 'bold')

ax.set_ylim(90, 150)
```

![Multicolor inexact](../images/chapter4/multicolor-inexact.png)

Greater elegance requires greater complication. If you are (understandably) dissatisfied with the above, invest in the topics covered in Chapter 3.
Below, we build on the solution from Chapter 3 by creating a function that creates a multi-colored title. Note we remove text options with the `remove()` method and work all in a single figure. This replaces the work of tuning the centering by hand that was done previously.

```python
def color_title(ax, text_color_list, y = 1.02, 
                fontsize = 14):
    """
    Create a centered multi-colored title.
    
    Parameters:
    -----------
    ax : matplotlib axes
    text_color_list : list of tuples
        Each tuple contains (text, color)
    y : float
        Vertical position in axes coordinates
    fontsize : int
        Font size for all text
    """
    # First create invisible text to find center
    full_text = ''.join([t[0] for t in text_color_list])
    temp = ax.text(0.5, y, full_text,
                   transform = ax.transAxes,
                   ha = 'center', fontsize = fontsize,
                   alpha = 0)
    
    # Get renderer and bbox
    fig = ax.get_figure()
    fig.canvas.draw()
    bbox = temp.get_window_extent()
    start_x = ax.transAxes.inverted().transform(
        bbox.corners())[0][0]
    temp.remove()
    
    # Place each colored segment
    x = start_x
    for text, color in text_color_list:
        t = ax.text(x, y, text, 
                    transform = ax.transAxes,
                    ha = 'left', fontsize = fontsize,
                    color = color)
        fig.canvas.draw()
        bbox = t.get_window_extent()
        # Move x to end of this text
        x = ax.transAxes.inverted().transform(
            bbox.corners())[1][0]
```

```python
fig, ax = plt.figure(), plt.axes()

# Data
years = [2020, 2021, 2022, 2023]
sales = [100, 120, 115, 130]
costs = [80, 95, 100, 105]

ax.plot(years, sales, color = 'green', linewidth = 2)
ax.plot(years, costs, color = 'red', linewidth = 2)

# Use the color_title function
text_color_list = [
    ('Revenue', 'green'),
    (' and ', 'black'),
    ('Costs', 'red'),
    (' Over Time', 'black')
]

color_title(ax, text_color_list)

ax.set_ylabel('Amount ($)')
ax.set_ylim(70, 140)
```

![Color title example](../images/chapter4/color-title-ex.png)

## 4.6 Fonts

Finally, you might want to customize the fonts. In matplotlib 3.6 and newer, there is a `get_font_names()` method that can be used to display available font names. The code below creates a figure for each font. I get several warnings with messages like "Glyph 105 (i) missing from current font."

```python
import matplotlib.font_manager as fm

# Get list of available fonts
fonts = sorted(fm.get_font_names())

# Display first 5 fonts as example
for i, font in enumerate(fonts[:5]):
    fig, ax = plt.figure(), plt.axes()
    ax.text(0.5, 0.5, f'Font: {font}',
            fontname = font, fontsize = 20,
            ha = 'center', va = 'center')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.show()
```

### 4.6.1 Importing Fonts with Font Manager

If you're unsatisfied with the basic fonts available in matplotlib, just add your own. You can find fonts available for download from [theleagueofmoveabletype.com](https://www.theleagueofmoveabletype.com/) or [fonts.google.com](https://fonts.google.com).

After you've downloaded a font family, you should have folder for that font with otf or ttf files. Matplotlib has a font manager and you just need to tell matplotlib to look for a font in that folder. This is done below using `findSystemFonts()` and `addfont()`. Once the font files are added, you can simply specify the font in the `text()` call like any other in-built font.

```python
import matplotlib.font_manager as font_manager
import urllib.request
import zipfile
import os

# Download Pacifico font from Google Fonts
url = 'https://fonts.google.com/download?family=Pacifico'
urllib.request.urlretrieve(url, 'pacifico.zip')

# Extract the font
with zipfile.ZipFile('pacifico.zip', 'r') as zip_ref:
    zip_ref.extractall('pacifico_font')

# Add the font to matplotlib
font_files = font_manager.findSystemFonts(
    fontpaths=['pacifico_font'])
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# Use the font
fig, ax = plt.figure(), plt.axes()
ax.text(0.5, 0.5, 'Custom Font Example',
        fontname = 'Pacifico', fontsize = 30,
        ha = 'center', va = 'center')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Clean up
os.remove('pacifico.zip')
import shutil
shutil.rmtree('pacifico_font')
```

![Font example](../images/chapter4/font.png)