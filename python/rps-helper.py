def winning_pct(p, action = 'rock'):

    """What is the net winning percentage given a choice of action and an opponent's strategy p, where p is a probability distribution over rock, paper, and scissors."""

    if action.lower() == 'rock':

        winning_pct = p[2] # pr win
        net = p[2] - p[1] # pr win - pr lose

    elif action.lower() == 'paper':

        winning_pct = p[0]
        net = p[0] - p[2]

    elif action.lower() == 'scissors':

        winning_pct = p[1]
        net = p[1] - p[0]
    else:
        raise ValueError("Input is not a valid action")

    return net