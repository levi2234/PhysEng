
def xy_to_topygame(visualize, x, y):
    """
    Convert x and y coordinates from simulation space to Pygame screen space.

    Parameters:
    visualize (object): The visualization object.
    x (float): The x-coordinate in simulation space.
    y (float): The y-coordinate in simulation space.

    Returns:
    tuple: The converted x and y coordinates in Pygame screen space.
    """
    x = (x - visualize.simulationwidth[0]) * (visualize.screenwidth / (visualize.simulationwidth[1] - visualize.simulationwidth[0]))
    y = (y - visualize.simulationheight[0]) * (visualize.screenheight / (visualize.simulationheight[1] - visualize.simulationheight[0]))
    return (x, y)

