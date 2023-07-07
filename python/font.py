# font download
# https://fonts.google.com/specimen/Pacifico
# access font and add to font manager
font_dirs = ['Downloads/Pacifico'] # change depending on where you downloaded it
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

# Make Figure
fig, ax  = plt.figure(), plt.axes()
t = fig.text(0.5,0.5,'Live Laugh Love', #fontname = 'DancingScript',# font = 'DancingScript',
        ha = 'center', va = 'center')
ax.axis('off')
t.set_size(50)
t.set_name("Pacifico")

t.set_color('yellow')
#t.set_weight('bold')
fig.set_facecolor('brown')