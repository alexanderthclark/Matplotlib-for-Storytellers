angles = np.linspace(0, 2*np.pi, 101)
x = np.cos(angles)
y = np.sin(angles)

fig, ax = plt.figure(figsize = (5,5)), plt.axes()
ax.set_aspect('equal')

# Make circle
ax.plot(x,y)

# Plot example right triangle
angle = np.pi/3

# make hypotenuse
ax.plot([0,np.cos(angle)], [0,np.sin(angle)],
        linestyle = 'dashed', color ='gray', linewidth = 2)#

# mark point on circle
ax.plot([np.cos(angle)], [np.sin(angle)],
        marker = 'o', color ='gray', markersize = 11)

# dashed lines for opposite and adjacent
ax.plot([0,np.cos(angle)], [0,0],
        linestyle = 'dashed', color ='gray', linewidth = 2)
ax.plot([np.cos(angle),np.cos(angle)], [0,np.sin(angle)],
        linestyle = 'dashed', color ='gray', linewidth = 2)

# Triangle side lengths
fontsize = 14
ax.text(0.5*np.cos(angle) - .02, 0.5*np.sin(angle)+.02,
        '1', rotation = math.degrees(angle), ha = 'center', va = 'bottom', size = fontsize)
ax.text(0.5*np.cos(angle), -.02, r"$\cos(\theta)$",
        rotation = 0, ha = 'center', va = 'top', size = fontsize)
ax.text(np.cos(angle) + .02, 0.5*np.sin(angle), r"$\sin(\theta)$",
        rotation = 0, ha = 'left', va = 'center', size = fontsize)


# make small arc and mark angle
x = np.cos(angles[angles<= angle])
y = np.sin(angles[angles<= angle])
ax.plot(0.2*x,0.2*y, color = 'black')
ax.text(0.2*np.cos(np.pi/10), 0.2*np.sin(np.pi/10),
        r" $\theta$", size = 14)

# clean appearance
%run ../../python/spine-mod.py
ax.set_xticks([-1, 1])
ax.set_yticks([-1, 1])