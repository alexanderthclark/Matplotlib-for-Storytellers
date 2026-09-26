# Chapter 5: Dates

Matplotlib can handle dates, helping you to create better axis ticks and label formatting. Matplotlib's capabilities are built on the datetime and dateutil modules.

## 5.1 Plotting

Let's import some time series data. Below we use pandas integration and plot from a DataFrame with an index of pandas Timestamp values. Matplotlib recognizes these as dates and handles this reasonably well automatically, though the exact formatting could be improved.

```{literalinclude} ../../python/pd-dates.py
:language: python
```

![Pandas dates](../images/chapter5/pd-dates.png)

Before we try to improve the formatting, see what happens if we try to use the axes plot method.

```{literalinclude} ../../python/ax-dates.py
:language: python
```

![Axes dates](../images/chapter5/ax-dates.png)

You might find older code using `plot_date()`. The method was removed in matplotlib 3.11; pass datetime-like values directly to `plot()` instead.

### 5.1.1 Time Zone Handling

Matplotlib's date converters, locators, and formatters are time-zone aware. If no time zone is specified, Matplotlib uses `rcParams['timezone']`, which is `'UTC'` by default. You can choose the time zone used for tick labels by passing an IANA time-zone name to a formatter, as in `mdates.DateFormatter('%H:%M %Z', tz = 'America/New_York')`. The underlying observations do not move; only their displayed clock times change.

It is important to distinguish conversion from localization. A time-zone-aware timestamp identifies an unambiguous instant and can be converted for different audiences. A naive timestamp has no such information. With pandas, `tz_localize()` attaches a time zone to naive dates, while `tz_convert()` converts dates that are already time-zone aware. Localize only when you know which time zone the recorded clock times represent. Otherwise, the same numbers can be assigned to the wrong instant.

Named zones are preferable to fixed offsets because their rules account for daylight-saving transitions. Python's standard-library [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html) module supplies `tzinfo` objects for these zones. For plotting, a zone name or `tzinfo` object can be passed to Matplotlib's [date locators and formatters](https://matplotlib.org/stable/api/dates_api.html). The practical rule is simple: store an unambiguous time, commonly in UTC, and convert it only when choosing how the audience should read the axis.

## 5.2 Ticks and Formatting

### 5.2.1 Date Formats

The specific format of the displayed dates and times can be modified with `mdates.DateFormatter()`. This takes a format string and creates a formatter that can be passed to an axis method `set_major_formatter()` or `set_minor_formatter()`.

Here are some common format codes, applied to Sunday January 30, 2000, 11:59PM, local to Louisville, Kentucky. These can all be verified with `pd.Timestamp(year = 2000, month = 1, day = 30, hour = 23, minute = 59, tz = 'America/Kentucky/Louisville').strftime()`.

| Code | Output/Example |
|------|----------------|
| `'%Y'` | 4-Digit Year |
| `'%m'` | Month Number |
| `'%d'` | Day of Month |
| `'%B'` | Month Name |
| `'%H'` | 24-Hour Clock Hour |
| `'%M'` | Minute |
| `'%I'` | 12-Hour Clock Hour |
| `'%p'` | AM or PM |
| `'%A'` | Day of Week |
| `'%Z'` | Timezone Name |
| `'%Y-%m'` | `'2000-01'` |
| `'%Y/%m/%d'` | `'2000/01/30'` |
| `'%B %y'` | `'January 00'` |
| `'%H:%M %Z'` | `'23:59 EST'` |
| `'%A %I%p'` | `'Sunday 11PM'` |

A more complete list of format codes can be found in the [Python documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes). Codes that generate actual names, like `'%A'` or `'%B'`, can be made lowercase to produce an abbreviated name. Notice that these formats create zero-padded numbers like `'07'` instead of `'7'`. On Mac or Linux, padding can be eliminated with the `'-'` modifier, using `'%-H'` or `'%-m'` instead of `'%H'` or `'%m'` for example. On Windows, use `'#'`.

```{literalinclude} ../../python/date-fmt.py
:language: python
```

![Date format 1](../images/chapter5/date-fmt.png)

```{literalinclude} ../../python/date-fmt2.py
:language: python
```

![Date format 2](../images/chapter5/date-fmt2.png)
