violin_practice = {'Monday': 0,
                'Tuesday': 20,
                'Wednesday': 10,
                'Thursday': 0,
                'Friday': 40,
                'Saturday': 30,
                'Sunday': 0}

pd.Series(violin_practice).plot.bar()
plt.axhline(30)
plt.ylabel('Minutes of Practice')
plt.text(0, 30, 'Goal', color = 'C0')
plt.title('Violin Practice')