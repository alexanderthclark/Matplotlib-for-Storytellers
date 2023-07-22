fig, axx = plt.subplots(1,3, figsize = (10,3))

for ax, p in zip(axx, [20, 50, 80]):
    speedometer(p, ax = ax, fsize = 33)