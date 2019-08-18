def make_grid(width, height):
    """
    Creates a grid that will hold of all the tiles
    for a boggle game
    """

    return {
        (row,col): " " 
        for row in range(width)
        for col in range(height)
        }