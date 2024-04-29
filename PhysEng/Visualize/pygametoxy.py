
def pygame_to_xy(visualize, x, y):
    """
    Converts coordinates from pygame screen space to simulation space.

    Args:
        visualize (object): The visualization object containing simulation and screen dimensions.
        x (float): The x-coordinate in pygame screen space.
        y (float): The y-coordinate in pygame screen space.

    Returns:
        tuple: The converted (x, y) coordinates in simulation space.
    """
    x = x * ((visualize.simulationwidth[1] - visualize.simulationwidth[0]) / visualize.screenwidth) + visualize.simulationwidth[0]
    y = y * ((visualize.simulationheight[1] - visualize.simulationheight[0]) / visualize.screenheight) + visualize.simulationheight[0]
    return (x, y)