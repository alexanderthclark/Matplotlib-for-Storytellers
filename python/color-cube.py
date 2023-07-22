light_gray = [.98]*3
fig = plt.figure(figsize = (6,6),
                 facecolor = light_gray)
ax = plt.axes(projection='3d',
              facecolor = light_gray)

# control how many cubes/color changes
pieces = 10
grid = np.linspace(0, 1, pieces)[:-1]
width = grid[1] - grid[0]

# Make smaller cube units
for x in grid:
    for y in grid:
        for z in grid:
            vertices = list()
            for prod in product([x,x+width],[y,y+width], [z,z+width]):
                vertices.append(list(prod))

            faces = list()
            for key, face in enumerate([x,y,z]):
                # face is 0
                helper0 = [x for x in vertices if x[key] == face]
                helper1 = [x for x in vertices if x[key] == face + width]
                helper0.sort()
                helper0 = helper0[0:2] + helper0[::-1][0:2]
                helper1.sort()
                helper1 = helper1[0:2] + helper1[::-1][0:2]
                faces.append((helper0))
                faces.append(helper1)

            facecolor = (x + width / 2,
                         y + width / 2,
                         z + width / 2)
            pc = Poly3DCollection(faces,
                                  facecolor = facecolor,
                                  edgecolor = 'black')
            ax.add_collection3d(pc)

# Label Axes
ax.set_xlabel("Red")
ax.set_ylabel('Green')
ax.set_zlabel("Blue")

# Set Ticks
ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_zticks([0,1])
# Change padding
ax.xaxis.set_tick_params(pad = 0.1)
ax.yaxis.set_tick_params(pad = 0.1)
ax.zaxis.set_tick_params(pad = 0.1)
# Change azimuth
angle = 45 # + 180 # for second cube
ax.view_init(elev = None, azim = angle)
# Zoom out so labels are not cut off
ax.set_box_aspect([1,1,1], zoom = 0.86)