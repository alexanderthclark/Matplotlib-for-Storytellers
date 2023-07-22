theta = np.pi / 4
rotation_matrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

x_scale = 0.5
x_stretch = np.matrix([[x_scale, 0], [0, 1]])

y_scale = 2
y_stretch = np.matrix([[1, 0], [0, y_scale]])

transformation = rotation_matrix * y_stretch * x_stretch