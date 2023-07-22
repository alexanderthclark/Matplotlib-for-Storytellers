def color_point(x, y, z):
    """Given an opponent plays rock at chance x, paper at y, and scissors at z, what is the best response?
    Best responses are mapped to RGB colors."""

    # winning pcts for possible responses
    rock_net = z - y
    paper_net = x - z
    scissors_net = y - x

    # get best response as highest net winning pct
    list_  = [rock_net, paper_net, scissors_net]
    best = list_.index(max(list_))

    # map into RGB color weights
    colors = [0, 0, 0]
    colors[best] = 1

    # return RGB tuple with fourth value for opacity (alpha)
    return (*tuple(colors), 1.)